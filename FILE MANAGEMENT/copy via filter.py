#program to copy a text file "source.txt" onto "target.txt"
#barring the lines starting with a "@" sign.

def filter(oldFile, newFile):
	fin = open(oldFile, "r")
	fout = open(newFile, "w")
	while True:
		text = fin.readline()
		if len(text)==0:
			break
		if text[0]=="@":
			continue
		fout.write(text)
	fin.close()
	fout.close()

filter("source.txt", "target.txt")