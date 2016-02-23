# encoding=utf-8
from datetime import datetime,timedelta
from BeautifulSoup import BeautifulSoup
def format_date(date):
    now=datetime.now()
    if now-date<timedelta(hours=24):
        return date.time().strftime('%H:%M:%S')
    elif now-date<timedelta(days=365):
        return date.date().strftime('%m-%d')
    else:
        return date.date().strftime('%Y-%m-%d')
def slug(content):
    res=u''
    soup=BeautifulSoup(content)
    res=soup.getText()
    if len(res)>200:
        res=res[:150]
        res+=u'...'
    return res
