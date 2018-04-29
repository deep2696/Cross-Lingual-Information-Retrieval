from nltk.translate.bleu_score import sentence_bleu
from math import floor
import edit_distance
import matplotlib.pyplot as plt

actual_output=open("actual_output.txt","r")
system_output=open("system_output.txt","r")
a=[]
s=[]
for i in actual_output:
	x=[]
	i=i[:-1]
	for j in i:
		x.append(j)
	a.append(x)
for i in system_output:
	x=[]
	i=i[:-1]
	for j in i:
		x.append(j)
	s.append(x)
print(a[0])
print(s[0])

output=[]
edit_distance_output=[]
for j in range(5):
	net_score=0
	total_words=0
	edit_distance_score=0
	for i in range(int(floor(j*len(a))/5.0),int(floor((j+1)*len(a))/5.0)):
		reference = [a[i]]
		candidate = s[i]
		score = sentence_bleu(reference, candidate)
		net_score+=score
		total_words+=1
		sm = edit_distance.SequenceMatcher(a=a[i], b=s[i])
		edit_distance_score+=sm.ratio()
	edit_distance_output.append(edit_distance_score/total_words)
	output.append(net_score/total_words)

print(output)

plt.plot([1,2,3,4,5], output, 'ro')
plt.axis([0, 6, 0.7, 0.8])
plt.xlabel('Test Set')
plt.ylabel('Bleu Score')
plt.show()

print(edit_distance_output)
plt.plot([1,2,3,4,5], edit_distance_output, 'ro')
plt.axis([0, 6, 0.8, 0.9])
plt.xlabel('Test Set')
plt.ylabel('Edit Distance')
plt.show()