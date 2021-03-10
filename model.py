### Read file and convert into list

# f = open("doi-song/demo.tok.0.txt","r")
# l = f.read()
# l = l.replace("[","")
# l = l.replace("]","")
# l = l.split(",")
# print(len(l))

### 
categories = ["doi-song","du-lich","giai-tri","giao-duc","khoa-hoc","kinh-doanh","oto-xe-may",""]
g = open("doi-song/aAdjList.txt","r")
l1 = g.read()
l1 = l1.replace("{","")
l1 = l1.replace("}","")
l1 = l1.split(",")
tudien ={}
for p in l1: 
    tmp = p.split(":")
    tudien[tmp[0]]=int(tmp[1])
dem=0
tong = 0
dem=0
tbc=0
# print(tudien)
for p in tudien:
    tong=tong + tudien[p]
tbc = tong // len(tudien)
print(len(tudien))
selected = []
selected_tudien = {}
for p in tudien:
    if(tudien[p]>=tbc):
        selected.append(p)
        selected_tudien[p]=tudien[p]
print(len(selected))
# print(selected_tudien)

print("Hello")
