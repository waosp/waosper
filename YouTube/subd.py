from youtube_transcript_api import YouTubeTranscriptApi
import gc,re,os,sys,time,requests,psutil
jumpset=False
def stotime(s):
    s=float(s);t=[s//3600,(s//60)%60,int(s%60),int((s*1000)%1000)];del s;n=0
    for i in t[:-1]:
        if(0<i<10):t[n]='0{0}'.format(t[n])
        elif(i<=0):t[n]='00'
        n+=1;del i
    if(10<=t[3]<100):t[3]='0{0}'.format(t[3])
    elif(0<t[3]<10):t[3]='00{0}'.format(t[3])
    elif(t[3]<=0):t[3]='000'
    return '{0}:{1}:{2},{3}'.format(t[0],t[1],t[2],t[3])
    del t,n,i
f=open('videoGroup.txt','r');i=re.compile(r'\'\[\'.+?\'\]\'').findall(f.read());f.close();del f;n=0;il=len(i);f=['','','','','',''];vg=[];sleep=0
for i2 in i:
    n+=1;f[0]=i2.split('\',\'');f[1]=f[0][1];f[2]=int(f[0][2]);f[3]=f[0][3];f[4]=f[0][4];f[5]=f[0][5][:-3];f[0]=f[0][0][3:][:-1]#以后改回来
    if(n>=il):vg.append(f)
    else:vg.append(f[:])
    del i2
del i,il,n,f
def tryout():
    m='subtitlen.txt'
    print('睡眠两秒');time.sleep(2)
    c=False;global sleep
    try:requests.get('https://www.youtube.com',timeout=5)
    except:c=True
    if(c):print('断网——等待十秒');time.sleep(10);sleep=0
    else:
        sleep+=1
        if(sleep>=5):
            m1='missing.txt';m2='subtitlen.txt';f=open(m2,'r');n=int(f.read())+1;f.close();print('“{}”字幕不可用\n'.format(vg[n-1][0]));del c;sleep=0
            if(os.path.exists(m1)):f=open(m1,'a');f.write('\n{0}'.format(n));f.close()
            else:f=open(m1,'w+');f.write(str(n));f.close()
            f=open(m2,'w');f.write(str(n));f.close();del m1,f,n
        if(sleep==1):gc.collect()
    global jumpset;jumpset=True;main()
def subd(id,zhHans,title):
    if(zhHans==1):captions=YouTubeTranscriptApi.list_transcripts(id).find_transcript(['en']).translate('zh-Hans').fetch();m='简体中文'
    elif(zhHans==0):captions=YouTubeTranscriptApi.get_transcript(id);m='英文'
    elif(zhHans==2):captions=YouTubeTranscriptApi.list_transcripts(id).find_transcript(['en']).translate('zh-Hant').fetch();m='繁体中文'
    n=0
    for a in captions:
        n+=1;t=[a['start'],a['duration']];t[1]+=t[0];t=[stotime(t[0]),stotime(t[1])]
        sub='1\n{} --> {}\n{}'.format(t[0],t[1],a['text']) if(n<=1) else '{}\n\n{}\n{} --> {}\n{}'.format(sub,n,t[0],t[1],a['text'])
        del a,t
    f=open('{}（{}）.srt'.format(title,m),'w');f.write(sub);f.close();del n,f,sub,captions,id,zhHans,m,title
def main(asl,adm,apa,ail2):
    sl=asl#Languages setting(Selected Languages)
    dm=adm;m3='missing.txt'#Download Mode
    la=['英语','简体中文','繁体中文'];pa=apa;global jumpset;il2=ail2
    print(sl,dm,pa,jumpset,il2)
    while(pa!=2 and jumpset==False):
        while(pa==0):
            if(sl==None):sl=[]
            n=0;nl=len(sl);rt='暂无'
            for p in sl:
                rt=la[p] if(n<=0) else '{},{}'.format(rt,la[p])
                n+=1
            print('''=             欢迎使用            =
=            语言选择             =
=      +-1.添加/删除英语          =
=      +-2.添加/删除简体中文      =
=      +-3.添加/删除繁体中文      =
=            4.下一步             =
已选择:{}'''.format(rt))
            it=input()
            try:
                it=int(it)
                if(4>it>0):sl.append(it-1)
                elif(it==4 and nl!=0):pa=1;rt='暂无'
                else:sl.remove(abs(it)-1)
            except:continue
        while(pa==1):
            print('''=     请选择下载模式    =
=    1.补充   2.正常    =
=    3.确定   4.返回    =
已选择:{}'''.format(rt))
            it=input()
            try:
                it=int(it)
                if(it==1):rt='补充'
                elif(it==2):rt='正常'
                elif(it==3 and rt!='' and os.path.exists(m3)):
                    pa=2
                    dm=0 if(rt=='补充') else 1
                elif(it==4):pa=0
            except:continue
    m='subtitlen.txt'
    if(dm==1):
        try:
            if(os.path.exists(m)==False):il=0;f=open(m,'w+');f.write('0');f.close();del f;gc.collect()
            else:il=int(open(m,'r').read())
            mn=0
            for i in vg:
                mn+=1
                if(mn>il):
                    m2=i[5].split('=')[1];global sleep
                    if(sleep==0):print('“{}”字幕正在下载中……ID：{}'.format(i[0],m2))
                    for a in sl:subd(m2,a,i[0])
                    f=open(m,'w');f.write(str(mn));f.close();print('“{}”字幕下载完成\n'.format(i[0]));sleep=0;del m2;del f
                    if(psutil.Process(os.getpid()).memory_info().rss/1048576>=50):os.execl(sys.executable,sys.executable,*sys.argv)
                del i
        except:tryout()
    else:
        try:
            il=[]
            eg=open(m3,'r').readlines()
            rem=[]
            for a in range(len(eg)):
                mn=0
                if(a>=il2):
                    for i in vg:
                        mn+=1
                        if(mn==int(eg[a])):
                            m2=i[5].split('=')[1]
                            print('“{}”字幕正在下载中……ID：{}'.format(i[0],m2))
                            for a in sl:subd(m2,a,i[0])
                            rem.append(eg[a]);print('“{}”字幕下载完成\n'.format(i[0]));il2+=1
                            if(psutil.Process(os.getpid()).memory_info().rss/1048576>=50):os.execl(sys.executable,sys.executable,*sys.argv)
            for a in rem:eg.remove(a)
            for a in range(len(eg)):
                t=eg[a] if(a<=0) else '{}\n{}'.format(t,eg[a])
            f=open(m3,'w+');f.write(t);f.close();del f
            if(len(eg)-1<il2):print('下载完成');quit()
        except:
            if(len(eg)-1<il2):print('下载完成');quit()
            tryouta(i[0],sl,dm,pa,il2)
def tryouta(i,asl,adm,apa,ail2):print('“{}”字幕不可用'.format(i));ail2+=1;global jumpset;jumpset=True;main(asl,adm,apa,ail2)
if __name__ == '__main__':main([],1,0,0)
