from TienXuLy import fromTextToList
import json
from model import classific
import re

kind = ['thoi-su', 'the-gioi', 'kinh-doanh',
        'giai-tri', 'the-thao', 'phap-luat', 'giao-duc', 'suc-khoe', 'doi-song', 'du-lich', 'khoa-hoc', 'so-hoa', 'oto-xe-may']

if __name__ == '__main__':
    length = len(kind)
    resultList = []
    for i in range(0, length):
        j = 0
        right = 0
        while True:
            try:
                f = open("./"+kind[i]+"-p_Test/demoT"+str(j) +
                         ".txt", "r", encoding="utf8")
                textOfNew = fromTextToList(f.read())
                print(j)
                with open("./runningFromTheHill.tok.txt", 'w') as fi:
                    fi.write(json.dumps(textOfNew))
                result = classific("./runningFromTheHill.tok.txt")
                if(len(re.findall(kind[i], result)) > 0):
                    right += 1
                j += 1
            except Exception as e:
                print(e)
                break
        resultList.append('{} has percent: {}'.format(kind[i], right/j*100))
    for l in resultList:
        print(l)
