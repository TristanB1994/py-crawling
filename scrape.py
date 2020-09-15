from bs4 import BeautifulSoup
import requests
import requests.exceptions 
# from usp.tree import sitemap_tree_for_homepage
import pathlib

docUrl = 'https://www.docpace.com/'

def getContent(pageUrl):

        content = None
        links = []
        path = pathlib.Path(pageUrl)
        # styles = None
        # js = []
        # endpoints = None

        headers = {
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Allow-Methods':'GET',
            'Access-Control-Allow-Headers':'Content-Type',
            'Access-Control-Max-Age':'3600',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        
        try:
            # conn = urllib.request.urlopen(pageUrl)
            conn = requests.get(pageUrl, headers=headers)
        except requests.HTTPError as e:
            print("HTTPError: {}".format(e.response))
        except requests.URLRequired as e:
            print("URLError: {}".format(e.response))
        else:
            content = BeautifulSoup(conn.content, 'html.parser')
        
        for x in content.find_all('link'):
            links.append(x)

        print('---- CONTENT.FIND_ALL LINKS FINISHED ----')
        print(f'Path is: {path}')

        for x in content.find_all('a'):
            links.append(x)

        print('---- CONTENT.FIND_ALL a FINISHED ----')

        
        payload = { 'content':content, 'links':links}

        return payload            
        

            

# def getpages(url):
    

def getPic(url, file):
    ext = splitext(url)
    file += ('.'+ext)
    print(file)

    with open(file, 'wb') as handle:
        response = requests.get(url, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

def splitext(path):
    url = pathlib.Path(path)
    ext = url.name.split('.')[-1]
    return ext
        