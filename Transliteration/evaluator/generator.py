file=open("test_set.txt","r")
output=open("actual.txt","w")
test_input=open("test_input.txt","w")
for i  in file:
	s=i.split("\t")
	output.write(s[1])
	test_input.write(s[0]+"\n")