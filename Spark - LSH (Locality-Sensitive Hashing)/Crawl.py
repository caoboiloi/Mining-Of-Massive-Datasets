import multiprocessing as mp
import requests
from bs4 import BeautifulSoup
from IPython.display import clear_output
import numpy as np
import itertools
import json
def vnexpress_crawler(category):
    res = requests.get('https://vnexpress.net'+category)
    doc = BeautifulSoup(res.content, 'html.parser')
    article = doc.select('a[data-medium*=Item-]')
    data=[]
    for i in article:
        link = i['href']
        if link not in data:
            data.append(link)
    crawl_data = []
    success = 0
    for i in range(len(data)):
        try:
            res = requests.get(data[i])
            doc = BeautifulSoup(res.content, 'html.parser')
            content = doc.find_all('p',{'class','Normal'})
            datacontent = ''.join(j.text for j in content)
            datacontent = datacontent.replace("\n",'')
            crawl_data.append(datacontent)
        except:
            continue
        success += 1
    print(len(crawl_data))
    return crawl_data

def vnexpress():
    data = []
    res = requests.get('https://vnexpress.net/')
    doc = BeautifulSoup(res.content, 'html.parser')
    articles = doc.select('ul[class=parent]>li>a[data-medium]')
    category = []
    del articles[0]
    del articles[4]
    del articles[-1]
    articles = list(map(lambda x: x['href'],articles))

    pool = mp.Pool(processes=len(articles))

    result = pool.map(vnexpress_crawler, articles)
    result =list(itertools.chain.from_iterable(result))
    f = open("data3.txt", "a", encoding="utf-8")
    for i in result:
        if(len(i.split(" ")) < 20 ) : continue
        f.write(i+"\n")
    f.close()
def vietnamnet_crawler(category):
    crawl_data = []
    res1 = requests.get("https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=300&a=0".format(category))

    if(res1.status_code ==200):
        result =json.loads(res1.text.replace("retvar =",""))
        data =list(map(lambda x : x['link'],result))
        print(len(data))
        for i in range(len(data)):
            if(i%50 == 0 ):
                print("category : {} bai thu{}".format(category,i))
            
            try:
                res = requests.get(data[i])
                doc = BeautifulSoup(res.content, 'html.parser')
                content = doc.select('div[class=ArticleContent]>p')
                crawl_data.append(''.join(j.text for j in content))
            except:
                continue
    return crawl_data
def getAllCategoryVietnamnet():
    data = []
    res = requests.get('https://vietnamnet.vn/')
    doc = BeautifulSoup(res.content, 'html.parser')
    articles = doc.select('ul[class=menu-top]>li[class=item]>a[href]')
    category = []


    articles = list(map(lambda i : i['href'].replace("/","-").replace("-vn-","")[:-1], articles))
    pool = mp.Pool(processes=len(articles))
    result = pool.map(vietnamnet_crawler, articles)
    result =list(itertools.chain.from_iterable(result))

    f = open("data3.txt", "a", encoding="utf-8")
    for i in result:

        if(len(i.split(" ")) < 20 ) : continue
        f.write(i+"\n")
    f.close()

def thanhnien_crawler(category):
    res = requests.get('https://thanhnien.vn/'+category)
    doc = BeautifulSoup(res.content, 'html.parser')
    article = doc.find_all('a',{'class':'story__title'})
    data=[]
    for i in article:
        link = i['href']
        if link not in data:
            if 'https://thanhnien.vn/' not in link:
                data.append('https://thanhnien.vn/'+link)
            else:
                data.append(link)
    crawl_data = []
    success = 0
    for i in range(len(data)):
        try:
            res = requests.get(data[i])
            doc = BeautifulSoup(res.content, 'html.parser')
            title = doc.find('h1' ,{'class': 'details__headline'}).text
            content = doc.select('div[itemprop=articleBody]>div[class!= details__morenews]')
            content = ''.join(j.text for j in content)
            content.replace("\n",'')
            regex = re.compile(r'[\n\r\t]')
            content = regex.sub(" ", content)
            content = re.sub(' +', ' ', content)
            crawl_data.append(content)
            if(i%20 == 0):
                print(i, category)
        except:
            continue
        success += 1
    
    print(len(crawl_data))
    return crawl_data
def getAllCategoryThanhNien():
    data = []
    res = requests.get('https://thanhnien.vn/')
    doc = BeautifulSoup(res.content, 'html.parser')
    articles = doc.select('ul[class=site-header__menu]>li>ul>li>a')
    category = []
   
    articles = list(map(lambda x :x['href'],articles))
    articles = articles[:30]
    pool = mp.Pool(processes=(7))
    result = pool.map(thanhnien_crawler, articles)
    result =list(itertools.chain.from_iterable(result))
    f = open("data4.txt", "w", encoding="utf-8")
    for i in result:
        if(len(i.split(" ")) < 20 ) : continue
        f.write(i+"\n")
    f.close()


import re

if __name__ == "__main__":
    # vnexpress()
    getAllCategoryVietnamnet()
    # getAllCategoryThanhNien()
