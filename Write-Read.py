fw = open('sample.txt','w')
fw.write('Hello\n')
fw.write('how are you\n')
fw.close()

fr = open('sample.txt','r')
text= fr.read()
print(text)
fr.close()
