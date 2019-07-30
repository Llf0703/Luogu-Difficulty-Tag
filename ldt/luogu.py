import re
import time
from ldt.pre import getHtml


def getData(Type):
    listUrl = ''.join(['https://www.luogu.org/problem/list?type=', Type])
    problemListHtml = getHtml(listUrl)
    problemNum = re.search(r'count\%22\%3A(.+?)\%2C\%22result', problemListHtml).group(1)
    pageNum = (int(problemNum) + 49) // 50

    print(''.join(['Type: ', Type, ' ; Total: ', str(pageNum), ' pages.']))

    problemIDList = problemDifficultyList = []
    for page in range(1, pageNum+1):
        print(''.join(['Now: page ', str(page)]))
        url = "".join([listUrl, '&page=', str(page)])
        html = getHtml(url)
        curProblemIDList = re.compile(r'<li>(.+?)&nbsp;<a').findall(html)
        problemIDList = problemIDList + curProblemIDList
        curProblemDifficultyList = re.compile(r'difficulty%22%3A([0-7]{1,1})%2C%22totalSubmit').findall(html)
        problemDifficultyList = problemDifficultyList + curProblemDifficultyList
        time.sleep(1)

    return problemIDList, problemDifficultyList
