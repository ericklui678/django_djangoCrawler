from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from urllib import urlopen

# set a url, first try Coding Dojo, then try pulling from a few of your favorite sites!
url = 'http://www.codingdojo.com'
# ask beautiful soup to open the below url and parse html
soup = BeautifulSoup(urlopen(url), 'html.parser')

def makeUrlList():
    urlArr = []
    for i in range(len(soup('a'))):
        urlArr.append(soup('a')[i]['href'])
    return urlArr

def makeUrlDictionary():
    urlDict = {}
    for i in range(len(soup('a'))):
        if urlDict.has_key(soup('a')[i]['href']):
            urlDict[soup('a')[i]['href']] += 1
        else:
            urlDict[soup('a')[i]['href']] = 1
    return urlDict


def index(request):

    context = {
        'data': soup
    }
    return render(request, 'djangoCrawler_app/index.html', context)
