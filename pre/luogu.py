import urllib.request
import re
import time


def get_html(url):
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    page = opener.open(url)
    html = page.read()
    html = html.decode('utf-8')
    return html

luogu_url='https://www.luogu.org/problemnew/'

p_url='lists?page='

pro_id=999

for page in range(1,86):
    url=luogu_url+p_url+str(page)
    html=get_html(url)
    rst=re.compile(r'<span class=\"lg-right am-text-right\">\n<span class=\"am-badge am-radius lg-bg-(.+?)\">')
    rst_list=rst.findall(html)
    file=open('luogu.txt','a')
    for j in rst_list:
        level=0
        if j=='gray':
            level=0
        if j=='red':
            level=1
        if j=='orange':
            level=2
        if j=='yellow':
            level=3
        if j=='green':
            level=4
        if j=='bluelight':
            level=5
        if j=='purple':
            level=6
        if j=='bluedark':
            level=7
        pro_id=pro_id+1
        file.write('P'+str(pro_id)+' '+str(level)+'\n')
    file.close()
    print("now:"+' page'+str(page))
    time.sleep(1)

uva_url='lists?type=16&page='

pro_id=99

for page in range(1,100):
    url=luogu_url+uva_url+str(page)
    html=get_html(url)
    rst=re.compile(r'<span class=\"lg-right am-text-right\">\n<span class=\"am-badge am-radius lg-bg-(.+?)\">')
    rst_list=rst.findall(html)
    file=open('luogu-UVA.txt','a')
    for j in rst_list:
        level=0
        if j=='gray':
            level=0
        if j=='red':
            level=1
        if j=='orange':
            level=2
        if j=='yellow':
            level=3
        if j=='green':
            level=4
        if j=='bluelight':
            level=5
        if j=='purple':
            level=6
        if j=='bluedark':
            level=7
        pro_id=pro_id+1
        if pro_id==1761:
            pro_id=10000
        if pro_id==290:
            pro_id=291
        if pro_id==12300:
            pro_id=12304
        file.write('UVA'+str(pro_id)+' '+str(level)+'\n')
    file.close()
    print("now:"+' page'+str(page))
    time.sleep(1)