import urllib2
import xlsxwriter
import sys
import os
import fcntl

#code to invoke a function to stop and save the code in db when pree enter or other command
fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)

#creating worksheet
workbook = xlsxwriter.Workbook('afaqs_work.xlsx')
worksheet = workbook.add_worksheet()

#expoting data to worksheet
worksheet.write("A1", "Agencies")
worksheet.write("B1", "Name/Head")
worksheet.write("C1", "Head Office")
worksheet.write("D1", "Place")
worksheet.write("E1", "Phone No.")
worksheet.write("F1", "Email id")
worksheet.write("G1", "Website")

i=2
#fetching data of afaqs.com
#this for loop is for all the matter in A to Z
from string import ascii_uppercase
for c in ascii_uppercase:
	
	try:
		stdin = sys.stdin.read() ##code continue to invoke a function to stop and save the code in db when press enter or other command
		if "\n" in stdin:
			break
	except IOError:
			pass

	#this url will open the all A starting name
	A_categ = "http://resources.afaqs.com/index.html?category=AD+Agencies"+"&alpha="+c
	print "hey I am priting !! " + A_categ
	page3 = urllib2.urlopen(A_categ)

	from bs4 import BeautifulSoup

	soup = BeautifulSoup(page3,"html.parser")
	print "Title of the this page is:" + soup.title.string

	#this is the table where all particular elements(a/b/c/d/....z) are present is 
	#all ad agencies of "A"
	
	tb = soup.find('table' , class_="agency big_btmargin")
	link = tb.find_all ('a')
	for l in link:
		try:
			stdin = sys.stdin.read() ##code continue to invoke a function to stop and save the code in db when press enter or other command
			if "\n" in stdin:
				break
		except IOError:
			pass

		try:
			print "Grabbing {} of {}".format(str(i-1),str(len(link)))

			ind_categ = l.get("href")
			ind_cate_name = l.string
			worksheet.write('A' + str(i), ind_cate_name)

			full_url = "http://resources.afaqs.com/"+ind_categ
			page2 = urllib2.urlopen(full_url)		#to open page of indivial a..z categ
			page2_url = BeautifulSoup(page2,"html.parser")
			print "Title of the this page is:" + page2_url.title.string
			#worksheet.write('A'+str(i), page2_url.title.string)
			print "I am opening a url :)"

			#code of main_page is copied here
		
			#data from the final block
			#all_table=soup.find_all('table')
			right_table=page2_url.find('table', class_='space-top20')
			#print right_table.text


			name=right_table.find('td', itemprop="name")	#NAME
			print "name=" +name.string
			worksheet.write('B' + str(i), name.string)

			address=right_table.find('td', itemprop="streetAddress")	#Head Office
			if address is not None:
				print "Head Office =" +address.string
				worksheet.write('C' + str(i), address.string)
		
			
			f_city=right_table.find('td', itemprop="addressLocality")	#City
			if f_city is not None:
				print "full city =" + f_city.text
				worksheet.write('D' +str(i), f_city.text)
		
			tel=right_table.find('span', itemprop="telephone")		#phone
			if tel is not None:
				print "telephone no- " + tel.string
				worksheet.write('E' +str(i), tel.string)

																#email
			em=right_table.find('span', itemprop="email")
			if em is not None:
				ema= em.find('a')
				print "email= " + ema.text
				worksheet.write('F'+str(i), ema.text)

																#website
			ur=right_table.find('span', itemprop="url")
			if ur is not None:
				we = ur.find('a')
				print "website= " + we.text
				worksheet.write('G'+ str(i), we.text)
			i+=1
		except Exception as e:
			print str(e)
		
workbook.close()			