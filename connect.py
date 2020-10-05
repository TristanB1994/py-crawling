from bs4 import BeautifulSoup
import requests, requests.exceptions

def geturl(url):
    headers = { 'Access-Control-Allow-Origin':'*','Access-Control-Allow-Methods':'GET','Access-Control-Allow-Headers':'Content-Type','Access-Control-Max-Age':'3600','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    try:
        conn = requests.get(url, headers=headers)
    except requests.HTTPError as e:
        print("HTTPError: {}".format(e.response))
    except requests.URLRequired as e:
        print("URLError: {}".format(e.response))
    else:
        return conn

def beautyurl(conn):
    if conn.content:
        return BeautifulSoup(conn.content, 'html.parser')