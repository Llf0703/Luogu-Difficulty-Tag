import urllib.request
import re
import time


def get_html(url):
    headers = ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    page = opener.open(url)
    html = page.read()
    html = html.decode('utf-8')
    return html

luogu_url='https://www.luogu.org/problemnew/'

p_url='lists?page='

file=open('luogu.php','w')
file.write('<?php\n')
file.close()

for page in range(1,87):
    url=luogu_url+p_url+str(page)
    html=get_html(url)
    rst=re.compile(r'<span class=\"am-badge am-radius lg-bg-(.+?)\">')
    rst_list=rst.findall(html)
    pro=re.compile(r'P([0-9]{4,}) <a target=\"_blank\" href=\"/problemnew/show/')
    pro_list=pro.findall(html)
    pro_len=len(pro_list)
    file=open('luogu.php','a')
    for i in range(0,pro_len):
        j=rst_list[i]
        pro_id=pro_list[i]
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
        file.write('$id[\'P'+str(pro_id)+'\']=\"'+str(level)+'\";\n')
    file.close()
    print('Luogu ok: page'+str(page))
    time.sleep(1)

uva_url='lists?type=16&page='

for page in range(1,100):
    url=luogu_url+uva_url+str(page)
    html=get_html(url)
    rst=re.compile(r'<span class=\"lg-right am-text-right\">\n<span class=\"am-badge am-radius lg-bg-(.+?)\">')
    rst_list=rst.findall(html)
    pro=re.compile(r'UVA([0-9]{3,}) <a target=\"_blank\" href=\"/problemnew/show/')
    pro_list=pro.findall(html)
    pro_len=len(pro_list)
    file=open('luogu.php','a')
    for i in range(0,pro_len):
        j=rst_list[i]
        pro_id=pro_list[i]
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
        file.write('$id[\'UVA'+str(pro_id)+'\']=\"'+str(level)+'\";\n')
    file.close()
    print('UVA ok: page'+str(page))
    time.sleep(1)