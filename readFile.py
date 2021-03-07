import json
a = dict()
with open('doi-song/aNounList.txt', 'r') as f:
    a = json.loads(f.read())
d = sorted(a.items(), key=lambda x: x[1], reverse=True)
print(len(d))
print(d)
