from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def weget(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if true_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def true_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def error(e):
    print(e)

url_html1=weget("http://www.rrbcdg.gov.in/")    
html1=BeautifulSoup(url_html1,'html.parser')
for i, td in enumerate(html1.select('td')):
	print(i, td.text)

url_html2=weget("http://joinindianarmy.nic.in/alpha/officers-notifications.htm")
html2=BeautifulSoup(url_html2,'html.parser')
requireddiv=html2.find('div',id='ContentPlaceHolder1_OfficerNotificationList1_pnlList')
for i ,li in enumerate(requireddiv.select('li')):
	print(i,li.text)

url_html3=weget("https://mohfw.gov.in/media/news-and-highlights1")    
html3=BeautifulSoup(url_html3,'html.parser')
for i, tr in enumerate(html3.select('tr')):
	print(i, tr.text)

url_html4=weget("http://mhrd.gov.in/updates")
html4=BeautifulSoup(url_html4,'html.parser')
requireddiv2=html4.find('div',class_='tabcontext')
for i ,li in enumerate(requireddiv2.select('li')):
	print(i,li.text)