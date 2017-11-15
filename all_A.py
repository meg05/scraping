import urllib2
import xlsxwriter

#fetching data of afaqs.com
from string import ascii_uppercase
for c in ascii_uppercase:
	#this url will open the all A starting name
	A_categ = "http://resources.afaqs.com/index.html?category=AD+Agencies"+"&alpha="+c
	print "hey i am priting !! " + A_categ
	page3 = urllib2.urlopen(A_categ)

	from bs4 import BeautifulSoup

	soup = BeautifulSoup(page3,"html.parser")
	print "Title of the this page is:" + soup.title.string

	#this is the table where all particular elements(a,b,....z) are present
	tb = soup.find('table' , class_="agency big_btmargin")
	link = tb.find_all ('a')
	for l in link:
		try:
			ind_categ =  l.get("href")
			full_url = "http://resources.afaqs.com/"+ind_categ
			page2 = urllib2.urlopen(full_url)		#to open page of indivial a..z categ
			page2_url = BeautifulSoup(page2,"html.parser")
			print "Title of the this page is:" + page2_url.title.string
			print "I am opening a url :)"

		except Exception as e:
			print str(e)