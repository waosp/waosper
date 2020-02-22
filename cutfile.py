import os,sys#,time
def baseN(num, b):
  return ((num == 0) and "0") or \
      (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])
if len(sys.argv)==3:
    e,fl=sys.argv[1],int(sys.argv[2]);f=open(e,'rb');e=repr(f.read());f.close();del f
    l,r=len(e)//fl+1,''
    for a in range(l):
        if(a==l-1):
            pre=baseN(len(e[fl*a:]),36)#运用36进制，适当减少数字长度log(36,1024)=1.934264036;log(32,1024)=2
            if(len(pre)<2):pre='{} '.format(pre)
            r='{}\n{}{}{}'.format(r,pre,e[fl*a:],baseN(a,36))
        elif(a==0):r='{}{}'.format(e[fl*a:fl*(a+1)],baseN(a,36))
        else:r='{}\n{}{}'.format(r,e[fl*a:fl*(a+1)],baseN(a,36))
    print('{}\n{}'.format(baseN(l,36),r))
"""
def on_send(m):f=open('send.bin','w+');f.write(m);f.close();del f
def on_receive():f=open('receive.bin','r');r=f.read();f.close();del f;return r
def file_send(p):
    f=open(p,'rb');a,b=get_fragments(repr(f.read()),1024),True;f.close();del f
    on_send('对方发起了文件发送请求，段长：1028-{}、段数：{}、文件名：{}、输入Y/y接收文件，否则拒绝接收文件。'.format(str(1028+int(pow(a[0],0.1))),str(a[0]),p.split('/')[-1:][0]))
    while(b):
        time.sleep(0.01);m=on_receive()
        if(m=='Y' or m=='y'):b=False
        else:return None
    for c in a[1]:
        on_send('?FMV{}'.format(c));b=True
        while(b):
            time.sleep(0.01);m=on_receive()
            if(m[:4]=='?FMV'):
                if(m[4:]==c[1028:]):b=False
    return 0
def file_receive(f,p):
    if not os.path.exists(p):a=open(p,'wb+');a.write(eval(''.join(f[4:1028])));a.close();del a
"""
