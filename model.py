import json


def classific(path):
    # Read file and convert into list

    # f = open("doi-song/demo.tok.0.txt","r")
    # l = f.read()
    # l = l.replace("[","")
    # l = l.replace("]","")
    # l = l.split(",")
    # print(len(l))

    ###
    categories = ["doi-song", "du-lich", "giai-tri", "giao-duc", "khoa-hoc", "kinh-doanh",
                  "oto-xe-may", "phap-luat", "so-hoa", "suc-khoe", "the-gioi", "the-thao", "thoi-su"]
    # print(len(categories))
    tudien_tongquat = {}
    try:
        with open('./TuDienTongQuat.txt', 'r') as f:
            tudien_tongquat = json.loads(f.read())
    except:
        if len(tudien_tongquat) == 0:
            for i in range(0, len(categories)):
                # print(categories[i])
                tmp = categories[i]
                link = "d:/HK2N4/LapTrinhMangNC/crawl/"+tmp+"/aNounList.txt"
                g = open(link, "r")
                l1 = g.read()
                l1 = l1.replace("{", "")
                l1 = l1.replace("}", "")
                l1 = l1.split(",")
                tudien = {}
                for p in l1:
                    tmp = p.split(":")
                    tudien[tmp[0]] = int(tmp[1])
                dem = 0
                tong = 0
                dem = 0
                tbc = 0
                # print(tudien)
                for p in tudien:
                    tong = tong + tudien[p]
                tbc = tong // len(tudien)
                # print(len(tudien))
                selected = []
                selected_tudien = {}
                for p in tudien:
                    if(tudien[p] >= tbc):
                        selected.append(p)
                        selected_tudien[p] = tudien[p]
                # print(len(selected))
                tudien_tongquat[categories[i]] = selected
                # print(selected_tudien)

            with open("./TuDienTongQuat.txt", 'w') as f:
                f.write(json.dumps(tudien_tongquat))
        # print("--------------------------")
    # Kiem tra do tuong quan cua Noun giua hai categories

    # dem=0
    # for i in range(0,13):
    #     for j in range(0,13):
    #         dem=0
    #         if(i==j):
    #             continue
    #         for p in tudien_tongquat[categories[i]]:
    #             for q in tudien_tongquat[categories[j]]:
    #                 if(p==q):
    #                     dem+=1
    #         print('{0}---{1}---:{2}---tuong ung voi---{3}----{4}'.format(categories[i],categories[j],dem,len(tudien_tongquat[categories[i]]),len(tudien_tongquat[categories[j]])))

    # Ket luan: Se phan loai theo Danh tu - Vi dong tu va tinh tu, ti le phan tram trong tuong quan giua hai categories kha tuong duong nhau

    # Solve mot paper da tien xu ly bat ki

    filetest = open(path, "r")
    read_ = filetest.read()
    read_ = read_.replace("[", "")
    read_ = read_.replace("]", "")
    read_ = read_.split(",")
    # print(type(read_))
    dem_ = 0
    tong_ = 0
    tbc_ = 0
    matdo = {}
    for i in range(0, 13):
        dem_ = 0
        for p in read_:
            if(p in tudien_tongquat[categories[i]]):
                dem_ += 1
        matdo[categories[i]] = dem_
        tong_ += dem_
    tbc_ = tong_ // 13
    maax_ = 0
    vt_ = 0
    # print('TBC la: {0}'.format(tbc_))
    for i in range(0, 13):
        if(matdo[categories[i]] > tbc_):
            # print('Mat do cua {0} trong paper la: {1}'.format(categories[i],matdo[categories[i]]))
            if(matdo[categories[i]] > maax_):
                maax_ = matdo[categories[i]]
                vt_ = i
    maax_ = 0
    vt1_ = -1
    for i in range(0, 13):
        if(i == vt_):
            continue
        if(matdo[categories[i]] > tbc_):
            # print('Mat do cua {0} trong paper la: {1}'.format(categories[i],matdo[categories[i]]))
            if(matdo[categories[i]] > maax_):
                maax_ = matdo[categories[i]]
                vt1_ = i

    # print('Mat do cua {0} trong paper la: {1}'.format(categories[vt_],matdo[categories[vt_]]))
    # if (vt1_!= -1):
    #     print('Mat do cua {0} trong paper la: {1}'.format(categories[vt1_],matdo[categories[vt1_]]))

    tong_sum = 2*matdo[categories[vt_]]-matdo[categories[vt1_]]
    tile1 = float(matdo[categories[vt_]]/tong_sum)
    tile2 = float(1-tile1)
    res = ''
    if(vt1_ != -1):
        res = '{0}_{1} {2}_{3}'.format(categories[vt_], tile1*100,
                                       categories[vt1_], tile2*100)
        print(res)
    else:
        res = '{0}_{1}'.format(
            categories[vt_], tile1*100)
        print(res)
    return res
