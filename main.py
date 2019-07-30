from ldt.pre import getYaml
from ldt.local import writePhp
from ldt.local import writeCsv


config = getYaml()


if __name__ == '__main__':
    if config['mode'] ==1:
        file = open('typecho-model-php.php', 'r+', encoding='utf-8')
        model = file.read()
        file.close()
        file = open('luogu.php', 'w', encoding='utf-8')
        for ojName in config['oj']:
            writePhp(ojName,file)
        file.write(model)
        file.close()
    elif config['mode'] == 2:
        file = open('data.csv', 'w')
        for ojName in config['oj']:
            writeCsv(ojName,file)
        file.close()
    else:
        print("This mode is unavailable!")
