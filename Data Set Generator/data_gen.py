import random
from indic_transliteration import sanscript
data_file=open('1.txt',"r")
l=[]
counter=0
# exit()
itrans_file=open('itans',"r")
itrans_mapping_to_roman={}
for i in itrans_file:
	#print(i)
	itrans_mapping_to_roman[i.split('\t')[0]]= (((i.split('\t'))[1])[:-1]).lower().split(',')
#print(itrans_mapping_to_roman)
aur=0
def generator(s):
	# print(s)
	# global aur
	# print(aur)
	# aur+=1
	if len(s)==0:
		return [""]
	ans=[]
	try:
		for i in itrans_mapping_to_roman[s[0]]:
			for j in generator(s[1:]):
				ans.append(i+j)
	except:
		#print(s[0])
		return generator(s[1:])
	return ans
output_data=open("output_data.txt","w")
counter=0
# exit()
for i in data_file:
	l=(i.split('\t')[1])[:-1]
	s=[]
	for j in list(l):
		output=sanscript.transliterate(j,sanscript.DEVANAGARI, sanscript.ITRANS)
		s.append(output)
	#print("".join(s))
	#print("yeh jo mohaabaat hai ")
	l=generator(s)
	if len(l)<10:
		for k in l:
			output_data.write(k+"\t"+i.split('\t')[1])
			counter+=1
			if counter==700000:
				exit()
	else:
		ans=set()
		while len(ans)<20:
			current = random.choice(l)
			while current in ans:
				current = random.choice(l)
			ans.add(current)
			print (ans)
		for k in ans:
			output_data.write(k+"\t"+i.split('\t')[1])
			counter+=1
			if counter==700000:
				exit()