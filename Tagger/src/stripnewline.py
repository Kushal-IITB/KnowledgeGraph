import os,syspath= os.getcwd()filenames = os.listdir(path)i=1for filename in filenames:	f = open(filename,"r")	str1 =  f.read()	f.close()	f = open(filename,"w")	str2 = str1.replace('\n','')	f.write(str2)	f.close()	i=i+1	print i