from ldt.luogu import getData


def writeCsv(Type, file):
    problemIDList, problemDifficultyList = getData(Type)
    file.write('id, dif\n')
    num = len(problemIDList)
    for i in range(0, num):
        file.write("".join([problemIDList[i], ', ', problemDifficultyList[i], '\n']))

def writePhp(Type, file):
    problemIDList, problemDifficultyList = getData(Type)
    file.write('<?php\n')
    num = len(problemIDList)
    for i in range(0, num):
        file.write("".join(['$id[\'',problemIDList[i], '\']=\"', problemDifficultyList[i], '\";\n']))
    file.write('?>\n')