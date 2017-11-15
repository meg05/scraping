import urllib2
import xlsxwriter

#fetching data of afaqs.com
#this for loop is for all the matter in A to Z
from string import ascii_uppercase
for c in ascii_uppercase:
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
			ind_categ = l.get("href")
			full_url = "http://resources.afaqs.com/"+ind_categ
			page2 = urllib2.urlopen(full_url)		#to open page of indivial a..z categ
			page2_url = BeautifulSoup(page2,"html.parser")
			print "Title of the this page is:" + page2_url.title.string
			print "I am opening a url :)"

			#code of main_page is copied here
			#categ = "http://resources.afaqs.com/index.html?id=919&category=AD+Agencies&alpha=A"
			#page4 = urllib2.urlopen(categ)

			#soup = BeautifulSoup(page4,"html.parser")
			#print "Title of the this page is:" + soup.title.string

			#data from the final block
			#all_table=soup.find_all('table')
			right_table=page2_url.find('table', class_='space-top20')
			#print right_table.text

			name=right_table.find('td', itemprop="name")	#NAME
			print "name=" +name.string

			address=right_table.find('td', itemprop="streetAddress")	#Head Office
			print "Head Office =" +address.string

			f_city=right_table.find('td', itemprop="addressLocality")	#City
			print "full city =" + f_city.text

			tel=right_table.find('span', itemprop="telephone")
			print "telephone no- " + tel.string
			fax=right_table.find('span', itemprop="faxNumber")
			print "fax= " + fax.string 
			em=right_table.find('span', itemprop="email")
			print "em= " + em.string
			ur=right_table.find('span', itemprop="url")
			print "ur= " + ur.string
		except Exception as e:
			print str(e)




			