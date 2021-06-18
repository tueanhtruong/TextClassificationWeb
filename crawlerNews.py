from newsplease import NewsPlease
from newspaper import Article
import sys
from TienXuLy import fromTextToList
import json
from model import classific


def textFromUrl(url):
    article = NewsPlease.from_url(url)
    return article.title+'\n' + article.description + '\n'+article.maintext


if __name__ == "__main__":
    urls = []
    try:
        urls = sys.argv[1:]
    except:
        if len(urls) == 0:
            urls = [
                'https://vnexpress.net/chay-xe-may-gan-300-km-h-tren-dai-lo-thang-long-4246995.html']
    for url in urls:
        try:
            text = fromTextToList(textFromUrl(url))
        except:
            text = fromTextToList(
                'nguoi yeu anh cho em la sai')
        with open("./runningFromTheHill.tok.txt", 'w') as f:
            f.write(json.dumps(text))
        classific("./runningFromTheHill.tok.txt")
