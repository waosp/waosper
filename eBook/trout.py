import os
p='EBOOKS'
o=os.popen('cd {};tree'.format(p)).read().split('\n')[:-2]
t=''
n=0
for a in o:
    n+=1
    if(n<=1):
        t='{}'.format(a)
    else:
        t='{}\n{}'.format(t,a)
f=open('文件列表.txt'.format(p),'w+')
f.write(t)
f.close()
