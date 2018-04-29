from indic_transliteration import sanscript
try:
	input_file=open("sanskrit_input.txt","r")
	output_file=open("output_roman.txt","w")
except:
	print("please place a Document named sanskrit_input.txt in the directory.")
	exit()
for i in input_file:
	output=sanscript.transliterate(i,sanscript.DEVANAGARI, sanscript.HK)
	modified_output=''
	output=output.lower()
	for c in output:
		if c=='z':
			c='sh'
		modified_output+=c
	output_file.write(modified_output)