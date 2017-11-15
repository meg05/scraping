import urllib2
import xlsxwriter


#fetching data of afaqs.com

categ = "http://resources.afaqs.com/index.html?id=919&category=AD+Agencies&alpha=A"
page4 = urllib2.urlopen(categ)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page4,"html.parser")
print "Title of the this page is:" + soup.title.string

#data from the final block
#all_table=soup.find_all('table')
right_table=soup.find('table', class_='space-top20')
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