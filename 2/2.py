#!usr/local/bin/python3
# -*- coding:utf-8 -*-


import random
import string

def rndChar():
    temp=random.randint(1,100)
    if temp%2==0:
        return (chr(random.randint(65,90)))
    else:
        return (chr(random.randint(97,122)))


def rndNum():
    return(str(random.randint(0,10)))

def generatorStr():
    str1=""
    for i in range(25):
        temp=random.randint(0,20)
        if temp%2==0:
            ch1=rndNum()
        else:
            ch1=rndChar()
        str1+=ch1
    return str1

for i in range(10):
    print(generatorStr())

