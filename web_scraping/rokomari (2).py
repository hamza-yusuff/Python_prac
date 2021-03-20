import requests
from bs4 import BeautifulSoup
from csv import writer
query={'page':'2'}
res=requests.get('https://www.rokomari.com/book/category/90/%E0%A6%87%E0%A6%9E%E0%A7%8D%E0%A6%9C%E0%A6%BF%E0%A6%A8%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE%E0%A6%B0%E0%A6%BF%E0%A6%82?ref=mm_p13')
soup=BeautifulSoup(res.content,'html5lib')
titles=[]
author=[]
available=[]
price=[]
found=soup.find_all('div',attrs={'class':'col-4 col-xl-3'})

for book in found:
    wrapper=book.find('div',attrs={'class':'book-list-wrapper'})
    try:
        info=wrapper.find('div',attrs={'class':'book-text-area'})
        try:
            titles.append(info.find('p',attrs={'class':'book-title'}).text)
            author.append(info.find('p',attrs={'class':'book-author'}).text)
            available.append(info.find('p',attrs={'class':'book-status text-capitalize'}).text)
            price.append(info.find('p',attrs={'class':'book-price'}).span.text)
        except:
            pass
    except:
        pass
with open('rokomari.csv','w') as csv_file:
    header=['Book','Author','Available','Price']
    csv_writer=writer(csv_file)
    csv_writer.writerow(header)
                       
    for i in range(len(titles)):
        print(titles[i])
        print('Author: ',author[i])
        print('Available: ',available[i])
        print('Price: ', price[i])
        csv_writer.writerow([titles[i],available[i],price[i]])

