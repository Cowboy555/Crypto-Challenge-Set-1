import hashlib

hash1="67ae1a64661ac8b4494666f58c4822408dd0a3e4"

def perm(n,begin,end):      
    if begin>=end:  
        str1=''.join(n)
        sha = hashlib.sha1(str1)
        encrypts = sha.hexdigest()
        if encrypts==hash1:
          print "M is" ,str1
          exit()       
    else:  
        i=begin  
        for num in range(begin,end):  
            n[num],n[i]=n[i],n[num]  
            perm(n,begin+1,end)  
            n[num],n[i]=n[i],n[num]  

def mybin(num):
    bstr=bin(num).replace('0b','')
    l = len(bstr) % 8
    if l > 0:
        bstr = ('0'*(8-l)) + bstr
    return bstr
  

a1=['5','%']
a2=['8','(']
a3=['0','=']
a4=['*','+']
a5=['q','Q']
a6=['w','W']
a7=['i','I']
a8=['n','N']

for i in range(0,256):
    num=mybin(i)
    n=[]
    n.append(a1[int(num[0])])
    n.append(a2[int(num[1])])
    n.append(a3[int(num[2])])
    n.append(a4[int(num[3])])
    n.append(a5[int(num[4])])
    n.append(a6[int(num[5])])
    n.append(a7[int(num[6])])
    n.append(a8[int(num[7])])
    perm(n,0,len(n))  

