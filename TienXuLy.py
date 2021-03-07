from pyvi import ViTokenizer, ViUtils, ViPosTagger
import re
import os
import json


def no_accent_vietnamese(s):
    # s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(u'[à]', 'af', s)
    s = re.sub(u'[á]', 'as', s)
    s = re.sub(u'[ạ]', 'aj', s)
    s = re.sub(u'[ả]', 'ar', s)
    s = re.sub(u'[ã]', 'ax', s)
    s = re.sub(u'[â]', 'aa', s)
    s = re.sub(u'[ầ]', 'aaf', s)
    s = re.sub(u'[ấ]', 'aas', s)
    s = re.sub(u'[ậ]', 'aaj', s)
    s = re.sub(u'[ẩ]', 'aar', s)
    s = re.sub(u'[ẫ]', 'aax', s)
    s = re.sub(u'[ă]', 'aw', s)
    s = re.sub(u'[ằ]', 'awf', s)
    s = re.sub(u'[ắ]', 'aws', s)
    s = re.sub(u'[ặ]', 'awj', s)
    s = re.sub(u'[ẳ]', 'awr', s)
    s = re.sub(u'[ẵ]', 'awx', s)

    # s = re.sub(u'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(u'[À]', 'AF', s)
    s = re.sub(u'[Á]', 'AS', s)
    s = re.sub(u'[Ạ]', 'AJ', s)
    s = re.sub(u'[Ả]', 'AR', s)
    s = re.sub(u'[Ã]', 'AX', s)
    s = re.sub(u'[Â]', 'AA', s)
    s = re.sub(u'[Ầ]', 'AAF', s)
    s = re.sub(u'[Ấ]', 'AAS', s)
    s = re.sub(u'[Ậ]', 'AAJ', s)
    s = re.sub(u'[Ẩ]', 'AAR', s)
    s = re.sub(u'[Ẫ]', 'AAX', s)
    s = re.sub(u'[Ă]', 'AW', s)
    s = re.sub(u'[Ằ]', 'AWF', s)
    s = re.sub(u'[Ắ]', 'AWS', s)
    s = re.sub(u'[Ặ]', 'AWJ', s)
    s = re.sub(u'[Ẳ]', 'AWR', s)
    s = re.sub(u'[Ẵ]', 'AWX', s)

    # s = re.sub(u'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(u'[è]', 'ef', s)
    s = re.sub(u'[é]', 'es', s)
    s = re.sub(u'[ẹ]', 'ej', s)
    s = re.sub(u'[ẻ]', 'er', s)
    s = re.sub(u'[ẽ]', 'ex', s)
    s = re.sub(u'[ê]', 'ee', s)
    s = re.sub(u'[ề]', 'eef', s)
    s = re.sub(u'[ế]', 'ees', s)
    s = re.sub(u'[ệ]', 'eej', s)
    s = re.sub(u'[ể]', 'eer', s)
    s = re.sub(u'[ễ]', 'eex', s)

    # s = re.sub(u'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(u'[È]', 'EF', s)
    s = re.sub(u'[É]', 'ES', s)
    s = re.sub(u'[Ẹ]', 'EJ', s)
    s = re.sub(u'[Ẻ]', 'ER', s)
    s = re.sub(u'[Ẽ]', 'EX', s)
    s = re.sub(u'[Ê]', 'EE', s)
    s = re.sub(u'[Ề]', 'EEF', s)
    s = re.sub(u'[Ế]', 'EES', s)
    s = re.sub(u'[Ệ]', 'EEJ', s)
    s = re.sub(u'[Ể]', 'EER', s)
    s = re.sub(u'[Ễ]', 'EEX', s)

    # s = re.sub(u'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(u'[ò]', 'of', s)
    s = re.sub(u'[ó]', 'os', s)
    s = re.sub(u'[ọ]', 'oj', s)
    s = re.sub(u'[ỏ]', 'or', s)
    s = re.sub(u'[õ]', 'ox', s)
    s = re.sub(u'[ô]', 'oo', s)
    s = re.sub(u'[ồ]', 'oof', s)
    s = re.sub(u'[ố]', 'oos', s)
    s = re.sub(u'[ộ]', 'ooj', s)
    s = re.sub(u'[ổ]', 'oor', s)
    s = re.sub(u'[ỗ]', 'oox', s)
    s = re.sub(u'[ơ]', 'ow', s)
    s = re.sub(u'[ờ]', 'owf', s)
    s = re.sub(u'[ớ]', 'ows', s)
    s = re.sub(u'[ợ]', 'owj', s)
    s = re.sub(u'[ở]', 'owr', s)
    s = re.sub(u'[ỡ]', 'owx', s)

    # s = re.sub(u'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(u'[Ò]', 'OF', s)
    s = re.sub(u'[Ó]', 'OS', s)
    s = re.sub(u'[Ọ]', 'OJ', s)
    s = re.sub(u'[Ỏ]', 'OR', s)
    s = re.sub(u'[Õ]', 'OX', s)
    s = re.sub(u'[Ô]', 'OO', s)
    s = re.sub(u'[Ồ]', 'OOF', s)
    s = re.sub(u'[Ố]', 'OOS', s)
    s = re.sub(u'[Ộ]', 'OOJ', s)
    s = re.sub(u'[Ổ]', 'OOR', s)
    s = re.sub(u'[Ỗ]', 'OOX', s)
    s = re.sub(u'[Ơ]', 'OW', s)
    s = re.sub(u'[Ờ]', 'OWF', s)
    s = re.sub(u'[Ớ]', 'OWS', s)
    s = re.sub(u'[Ợ]', 'OWJ', s)
    s = re.sub(u'[Ở]', 'OWR', s)
    s = re.sub(u'[Ỡ]', 'OWX', s)

    # s = re.sub(u'[ìíịỉĩ]', 'i', s)
    s = re.sub(u'[ì]', 'if', s)
    s = re.sub(u'[í]', 'is', s)
    s = re.sub(u'[ị]', 'ij', s)
    s = re.sub(u'[ỉ]', 'ir', s)
    s = re.sub(u'[ĩ]', 'ix', s)

    # s = re.sub(u'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(u'[Ì]', 'IF', s)
    s = re.sub(u'[Í]', 'IS', s)
    s = re.sub(u'[Ị]', 'IJ', s)
    s = re.sub(u'[Ỉ]', 'IR', s)
    s = re.sub(u'[Ĩ]', 'IX', s)

    # s = re.sub(u'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(u'[ù]', 'uf', s)
    s = re.sub(u'[ú]', 'us', s)
    s = re.sub(u'[ụ]', 'uj', s)
    s = re.sub(u'[ủ]', 'ur', s)
    s = re.sub(u'[ũ]', 'ux', s)
    s = re.sub(u'[ư]', 'uw', s)
    s = re.sub(u'[ừ]', 'uwf', s)
    s = re.sub(u'[ứ]', 'uws', s)
    s = re.sub(u'[ự]', 'uwj', s)
    s = re.sub(u'[ử]', 'uwr', s)
    s = re.sub(u'[ữ]', 'uwx', s)

    # s = re.sub(u'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(u'[Ù]', 'UF', s)
    s = re.sub(u'[Ú]', 'US', s)
    s = re.sub(u'[Ụ]', 'UJ', s)
    s = re.sub(u'[Ủ]', 'UR', s)
    s = re.sub(u'[Ũ]', 'UX', s)
    s = re.sub(u'[Ư]', 'UW', s)
    s = re.sub(u'[Ừ]', 'UWF', s)
    s = re.sub(u'[Ứ]', 'UWS', s)
    s = re.sub(u'[Ự]', 'UWJ', s)
    s = re.sub(u'[Ử]', 'UWR', s)
    s = re.sub(u'[Ữ]', 'UWX', s)

    # s = re.sub(u'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(u'[ỳ]', 'yf', s)
    s = re.sub(u'[ý]', 'ys', s)
    s = re.sub(u'[ỵ]', 'yj', s)
    s = re.sub(u'[ỷ]', 'yr', s)
    s = re.sub(u'[ỹ]', 'yx', s)

    # s = re.sub(u'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(u'[Ỳ]', 'YF', s)
    s = re.sub(u'[Ý]', 'YS', s)
    s = re.sub(u'[Ỵ]', 'YJ', s)
    s = re.sub(u'[Ỷ]', 'YR', s)
    s = re.sub(u'[Ỹ]', 'YX', s)

    s = re.sub(u'[Đ]', 'DD', s)

    s = re.sub(u'[đ]', 'dd', s)

    return s


if __name__ == '__main__':
    kind = ['thoi-su-p', 'the-gioi-p', 'kinh-doanh-p',
            'giai-tri-p', 'the-thao-p', 'phap-luat-p', 'giao-duc-p', 'suc-khoe-p', 'doi-song-p', 'du-lich-p', 'khoa-hoc-p', 'so-hoa-p', 'oto-xe-may-p', ]
    kindTok = ['thoi-su', 'the-gioi', 'kinh-doanh',
               'giai-tri', 'the-thao', 'phap-luat', 'giao-duc', 'suc-khoe', 'doi-song', 'du-lich', 'khoa-hoc', 'so-hoa', 'oto-xe-may', ]

    length = len(kindTok)

    Noun = dict()
    Verb = dict()
    Adj = dict()
    for i in range(0, length):
        Noun.clear()
        Verb.clear()
        Adj.clear()
        print(kindTok[i])
        # os.mkdir("./"+kindTok[i])
        j = 0
        while True:
            try:
                f = open("./"+kind[i]+"/demo"+str(j) +
                         ".txt", "r", encoding="utf8")
                print(f.readline())
                test = f.read()
                test = re.sub(u'[\'\"-:]', '', test)
                test = re.sub(u'subData', '', test)
                b1 = ViTokenizer.tokenize(test)
                (b1, POS) = ViPosTagger.postagging(b1)
                arrText = [no_accent_vietnamese(re.sub(u'_', ' ', s)).lower()
                           for s in b1]

                max = len(POS)
                for n in range(0, max):
                    if re.match('N', POS[n]):
                        te = arrText[n]
                        if Noun.get(te):
                            Noun[te] = Noun.get(te)+1
                        else:
                            Noun[te] = 1
                    if re.match('V', POS[n]):
                        te = arrText[n]
                        if Verb.get(te):
                            Verb[te] = Verb.get(te)+1
                        else:
                            Verb[te] = 1
                    if re.match('A', POS[n]):
                        te = arrText[n]
                        if Adj.get(te):
                            Adj[te] = Adj.get(te)+1
                        else:
                            Adj[te] = 1

                with open("./"+kindTok[i]+"/demo.tok."+str(j) +
                          ".txt", 'w') as f:
                    f.write(json.dumps(arrText))
                j += 1
            except:
                break
        with open("./"+kindTok[i]+"/aNounList.txt", 'w') as f:
            f.write(json.dumps(Noun))
        with open("./"+kindTok[i]+"/aVerbList.txt", 'w') as f:
            f.write(json.dumps(Verb))
        with open("./"+kindTok[i]+"/aAdjList.txt", 'w') as f:
            f.write(json.dumps(Adj))

    # for test_run in range(0, 10):
    #     f = open("thoi-su-p/demo"+str(test_run)+".txt", "r", encoding="utf8")
    #     f.readline()
    #     test = f.read()
    #     test = re.sub(u'[\'\"-:]', '', test)
    #     test = re.sub(u'subData', '', test)
    #     # print(test)
    #     b1 = ViTokenizer.tokenize(test)
    #     (b1, POS) = ViPosTagger.postagging(b1)
    #     arrText = [no_accent_vietnamese(re.sub(u'_', ' ', s)).lower()
    #                for s in b1]
    #     max = len(POS)
    #     for n in range(0, max):
    #         if re.match('N', POS[n]):
    #             te = arrText[n]
    #             if Noun.get(te):
    #                 Noun[te] = Noun.get(te)+1
    #             else:
    #                 Noun[te] = 1
    #         if re.match('V', POS[n]):
    #             te = arrText[n]
    #             if Verb.get(te):
    #                 Verb[te] = Verb.get(te)+1
    #             else:
    #                 Verb[te] = 1
    #         if re.match('A', POS[n]):
    #             te = arrText[n]
    #             if Adj.get(te):
    #                 Adj[te] = Adj.get(te)+1
    #             else:
    #                 Adj[te] = 1

    # with open('test.txt', 'w') as f:
    #     f.write(json.dumps(arrText))

    # with open('testNoun.txt', 'w') as f:
    #     f.write(json.dumps(Noun))

    # Ham doc dict
    # a = dict()
    # with open('testNoun.txt', 'r') as f:
    #     a = json.loads(f.read())

    # Ham read array from txt
    # a = list()
    # with open('test.txt', 'r') as f:
    #     a = json.loads(f.read())
    # print(a)
