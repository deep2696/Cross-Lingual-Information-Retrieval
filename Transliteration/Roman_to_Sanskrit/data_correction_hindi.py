f=open('train.rel.2.en','r')
eng_list=[]
for i in f:
    i=i[:-1]
    i=i.split(' ')
    i="".join(i)
    eng_list.append(i)
print (eng_list)

f=open('train.rel.2.hn',encoding='utf8')
fi=open('data.txt','w')
hin_list=[]
for i in f:
    i=i[:-1]
    i=i.split(' ')
    i="".join(i)
    fi.write(eng_list[0]+"\t"+i+"\n")
    eng_list.pop(0)
