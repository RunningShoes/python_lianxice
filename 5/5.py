
filepath='5.txt'
letter=[] 
str=''
with open(filepath) as file:
    f=file.readline()
    for line in f:
        str+=line
print(str)
letter=str.split(' ')
for word in letter:
    print(word)
print(len(letter))

