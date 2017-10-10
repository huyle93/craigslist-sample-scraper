#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:28:25 2017

@author: huyle
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

mylist = []
html = urlopen("https://newyork.craigslist.org/search/sub")
soup = BeautifulSoup(html, "html.parser")
#x = soup.find("div",{"id": "sortable-results"})
for i in soup.find_all("li", {"class":"result-row"})[1:]:
    for n in i.find_all("time", {"class":"result-date"}):
        time = (n['title'])
    for a in i.find_all('a', {"class":"result-title"}, href=True):
        href = a['href']
    a = i.find_all("a")
    data = time, a[1].text, "https://newyork.craigslist.org/"+href
    mylist.append(data)
for i in mylist:
    print(i, "\n")



# export items in mylist to csv file if uncommented belowed code

#with open('myfile.csv', 'a') as outcsv:   
#    writer = csv.writer(outcsv, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
#    for item in mylist:
#        writer.writerow(item)