from oracle import *
import sys


rc = 0

data1 = "DF70E343C4000A2AE35874CE75E64C31"

a = [0 for i in range(16)]
b = [0 for i in range(16)]
Oracle_Connect()
count = 0
while count < 16:
    for j in range(0,256):
        data=""                             
        b[15-count]=j
        for n in range(16-count,16):
            b[n] = a[n]^(count+1)
        for m in range(0,16):
            x=hex(b[m])
            x=x[2:]
            if len(x)<2:
                x = "0" + x
            data = data+x
        data = data + data1
        ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
        rc = Oracle_Send(ctext, 2)
        
        if rc == 1:         
            a[15-count]=b[15-count]^(count+1)
            count += 1         
            print data
            break
        
   
Oracle_Disconnect()
data=""
for i in range(0,16):    
    x=hex(a[i])
    x=x[2:]
    if len(x)<2:
        x = "0" + x
    data = data+x
print data



