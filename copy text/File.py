f=open("mad.txt","r")
print("The given MAD file contains")
t=open("mad1.txt","w")
count=0
for i in f:
            t.write(i)
            string = list(i)
t=open("mad1.txt","r")
print(t.read())
for i in string:
            if i=="a": count+=1
            elif i=="e": count+=1
            elif i=="i": count+=1
            elif i=="o": count+=1
            elif i=="u": count+=1
print("The number of Vowels in the given file is " + str(count) + ".")
cString = ''
for i in string:
            if i.isupper():
                        cString +=i.lower()
            else: cString +=i.upper()
print("The altered string is" + cString + ".")