import requests
def site():
    r=requests.get('https://goo.gl/PsibBu')
    with open('image.png','wb') as f:
        for  data in r.iter_content(chunk_size=100000):

            f.write(data)
            print("chulbul")
    print("success")
def site2():
    query = {'q': 'Forest', 'order': 'popular', 'min_width': '800', 'min_height': '600'}
    req = requests.get('https://pixabay.com/en/photos/', params=query)
    with open("site2.png",'wb') as f:
        f.write(req.content)
    return req.url
print(site2())
def site3():
    
    req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
    req.raise_for_status()
    with open('Nanotechnology.html', 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            fd.write(chunk)
def site4():
    url = 'http://some-domain.com/set/cookies/headers'
 
    headers = {'user-agent': 'your-own-user-agent/0.0.1'}
    cookies = {'visit-month': 'February'}
    
    req = requests.get(url, headers=headers, cookies=cookies)