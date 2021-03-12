from bs4 import BeautifulSoup
import urllib.request
import os


Purl = 'https://vnexpress.net/'
kind = ['thoi-su-p', 'the-gioi-p', 'kinh-doanh-p',
        'giai-tri-p', 'the-thao-p', 'phap-luat-p', 'giao-duc-p', 'suc-khoe-p', 'doi-song-p', 'du-lich-p', 'khoa-hoc-p', 'so-hoa-p', 'oto-xe-may-p']
for k in kind:
    url = Purl+k
    os.mkdir("./"+k+'_Test')
    i = 0
    for j in range(31, 34):
        subUrl = url+str(j)
        page = urllib.request.urlopen(subUrl)
        soup = BeautifulSoup(page, 'html.parser')
        new_feeds = soup.findAll(class_='item-news item-news-common')
        data = []

        for nfeed in new_feeds:
            try:
                data.clear()
                tfeed = nfeed.find(class_="title-news")
                a = tfeed.find('a')
                title = a.get('title')
                link = a.get('href')
                pfeed = nfeed.find(class_="description")
                content = pfeed.find("a")
                subData = content.get('title')
                if title == None or title == "" or subData == None:
                    continue

                print('Title: {} - Link: {}\nsubData: {}'.format(title, link, subData))
                data.append(
                    'Title: {} - Link: {}\nsubData: {} \n'.format(title, link, subData))
                nd = urllib.request.urlopen(link)
                soupnd = BeautifulSoup(nd, 'html.parser')
                att = soupnd.find('article')
                if att != None:
                    at = att.findAll(class_='block-item')
                    if(len(at) > 0):
                        for _ in at:
                            h = _.find(class_='header-block')
                            h = h.find(class_='title-block-live').text+'\n'
                            data.append(h)
                            n = _.find(class_='content-block')
                            n = n.findAll(class_="Normal")
                            data += [t.text+'\n' for t in n]
                    else:
                        at = soupnd.find(class_='sidebar-1')
                        at = at.findAll(class_='Normal')
                        for _ in at:
                            if _.text != "":
                                data.append(_.text.rstrip()+"\n")
                f = open("./"+k+"_Test/demoT"+str(i) +
                         ".txt", "w+", encoding="utf-8")
                f.writelines(data)
                f.close()
                i += 1
            except:
                continue
        j += 1
