import requests
from bs4 import BeautifulSoup
import csv
#csv module gives the Python programmer the ability to parse CSV (Comma Separated Values) files --> human readable files

URL = "https://codewithharry.com/"

# GET the HTML

r = requests.get(URL)
#The requests module allows you to send HTTP (herpertext transfer protocol) requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
#print(r.content)
# basicaly content is a property of requests -->response object would be used to access certain features such as content, headers, etc.
#print("\n\n\n\n\n\n\n\n\n###############################################################################################################################\n\n\n\n\n\n\n\n\n\n")
#It can parse almost all the elements of an HTML doc,
# breaking it down into different tags and pieces which can be filtered out for various use cases.

# Parse the HTML

soup = BeautifulSoup(r.content , "html5lib")
#Beautiful Soup is a Python package for parsing HTML(hypertext markup language) and XML(extensible markup language) documents
# (including having malformed markup,
# i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used
# to extract data from HTML, which is useful for web scraping.
print(soup.prettify())
#Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document.
#print("\n\n\n\n\n\n\n\n\n###############################################################################################################################\n\n\n\n\n\n\n\n\n\n")
title = soup.title()
# commonly use type of objects in
# print(type(title))# 1 = tag
# print(type(title.string))# 2 = NavigableString
# print(type(soup))# 3 = BeautifulSoup
# 4 = Comment
# markup = "<p><!----this is a comment ----></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p.string)

#print(title)
# get all the paragraph from website
#paras = soup.find_all('p')
#print(paras)
# get all the anchor tags from website
#anchor = soup.find_all('a')
#print(anchor)
# get first element from the HTML PAGE
#print(soup.find('p'))
# get first classes from the HTML PAGE
#print(soup.find('p'),['class'])
# get element of all class lead
#print(soup.find(('p'), class_='lead'))
#print(soup.find(('p'), class_='text-muted'))
#print(soup.get_text())

# get all link from the html page
#for link in anchor:
 #   print(link.get('href'))


# get all the link of the HTML page
#all_links = set()
# for links in anchor:
#     if(links.get("href") != '#'):
#         linktext = "https://codewithharry.com" +links.get('href')
#         all_links.add(links)
#         print(linktext)
navbarsupportedcontent =soup.find(id="navbarSupportedContent")
print(navbarsupportedcontent)
for em in navbarsupportedcontent.children():
    print(em)

for item in navbarsupportedcontent.string():
    print(item)
##############------Maam Tahreem -----------########################

# # images = []
# # table = soup.find("div", attrs={"id": "unsupported_banner"})
# # for row in table.findAll("div", attrs={"class": "p_b_8291c style:transition-duration:300 ms;height:auto"}):
# #     ## here attrs is pakage ha py mn use  to write concise and correct software without slowing down your code.
# #     image = {}
# #     image['theme'] = row.h5.text
# #     image['url'] = row.a['href']
# #     image['img'] = row.img['src']
# #     image['lines'] = row.img['alt'].split("#")[0]
# #     image['author'] = row.img['alt'].split('#')[1]
# #     images.append(image)
# #
# #
# # file_name = ("C:\\Users\\Ms\\Desktop\\Inspirational_File_Book1.csv")
# # with open(file_name,'w',newline="")as f:
# #     w = csv.DictWriter(f,['theme','url','img','lines','author'])
# #     #DictWriter class operates like a regular writer but maps Python dictionaries into CSV rows.
# #     w.writeheader()
# #     # The fieldnames parameter is a sequence of keys that identify the order in which values in the dictionary
# #     # passed to the writerow()writeheader() method writes the headers to the CSV file
# #     for image in images:
# #         w.writerow(image)
# #         #The writerow() method writes a row of data into the specified file. It is possible to write all data in one shot