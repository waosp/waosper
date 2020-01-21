from youtube_transcript_api import YouTubeTranscriptApi
import gc
import re
import os
import time
import requests
def stotime(s):
    s=float(s)
    t=[s//3600,(s//60)%60,int(s%60),int((s*1000)%1000)]
    n=0
    for i in t[:-1]:
        if(0<i<10):t[n]='0{0}'.format(t[n])
        elif(i<=0):t[n]='00'
        n+=1
        gc.collect()
    if(10<=t[3]<100):t[3]='0{0}'.format(t[3])
    elif(0<t[3]<10):t[3]='00{0}'.format(t[3])
    elif(t[3]<=0):t[3]='000'
    return '{0}:{1}:{2},{3}'.format(t[0],t[1],t[2],t[3])
    del t
    del n
    del i
    gc.collect()
i=re.compile(r'\'\[\'.+?\'\]\'').findall(open('videoGroup.txt','r').read())
n=0
il=len(i)
fil=['','','','','','']
vg=[]
for i2 in i:
    n+=1
    fil[0]=i2.split('\',\'')
    fil[1]=fil[0][1]
    fil[2]=int(fil[0][2])
    fil[3]=fil[0][3]
    fil[4]=fil[0][4]
    fil[5]=fil[0][5][:-3]
    fil[0]=fil[0][0][3:][:-1]#以后改回来
    gc.collect()
    if(n>=il):
        vg.append(fil)
    else:
        vg.append(fil[:])
def tryout():
    try:
        if(requests.get('https://www.youtube.com',timeout=5).status_code!=200):
            print('断网——等待十秒')
            time.sleep(10)
            main()
        else:
            n=int(open('subtitlen.txt','r').read())+1
            print('“{0}”字幕不可用\n'.format(vg[n-1][0]))
            if(os.path.exists('missing.txt')):
                f=open('missing.txt','a')
                f.write('\n{0}'.format(n))
                f.close()
            else:
                f=open('missing.txt','w+')
                f.write(str(n))
                f.close()
            f=open('subtitlen.txt','w')
            f.write(str(n))
            f.close()
            del f
            del n
            gc.collect()
        if(os.path.exists('subtitlen.txt')==False):
            il=0
            f=open('subtitlen.txt','w+')
            f.write('0')
            f.close()
            del f
            gc.collect()
        else:
            il=int(open('subtitlen.txt','r').read())
        mn=0
        for i in vg:
            mn+=1
            if(mn>il):
                i2=i[5].split('=')[1]
                print('“{0}”字幕正在下载中……ID：{1}'.format(i[0],i2))
                captions = YouTubeTranscriptApi.get_transcript(video_id=i2)
                al=len(captions)
                n2=0
                for a in captions:
                    n2+=1
                    t=[a['start'],a['duration']]
                    t[1]+=t[0]
                    t=[stotime(t[0]),stotime(t[1])]
                    if(n2<=1):
                        sub='1\n{0} --> {1}\n{2}'.format(t[0],t[1],a['text'])
                    else:
                        sub='{0}\n\n{1}\n{2} --> {3}\n{4}'.format(sub,n2,t[0],t[1],a['text'])
                fil = open('{0}（英文）.srt'.format(i[0]),'w')
                fil.write(sub)
                fil.close()
                captions = YouTubeTranscriptApi.list_transcripts(video_id=i2).find_transcript(['en']).translate('zh-Hans').fetch()
                n2=0
                for a in captions:
                    n2+=1
                    t=[a['start'],a['duration']]
                    t[1]+=t[0]
                    t=[stotime(t[0]),stotime(t[1])]
                    if(n2<=1):
                        sub='1\n{0} --> {1}\n{2}'.format(t[0],t[1],a['text'])
                    else:
                        sub='{0}\n\n{1}\n{2} --> {3}\n{4}'.format(sub,n2,t[0],t[1],a['text'])     
                fil = open('{0}（简体中文）.srt'.format(i[0]),'w')
                fil.write(sub)
                fil.close()
                fil = open('subtitlen.txt','w')
                fil.write(str(mn))
                fil.close()
                print('“{0}”字幕下载完成\n'.format(i[0]))
            gc.collect()
        print('normal')
    except:
        tryout()
def main():
    try:
        if(os.path.exists('subtitlen.txt')==False):
            il=0
            f=open('subtitlen.txt','w+')
            f.write('0')
            f.close()
            del f
            gc.collect()
        else:
            il=int(open('subtitlen.txt','r').read())
        mn=0
        for i in vg:
            mn+=1
            if(mn>il):
                i2=i[5].split('=')[1]
                print('“{0}”字幕正在下载中……ID：{1}'.format(i[0],i2))
                captions = YouTubeTranscriptApi.get_transcript(video_id=i2)
                al=len(captions)
                n2=0
                for a in captions:
                    n2+=1
                    t=[a['start'],a['duration']]
                    t[1]+=t[0]
                    t=[stotime(t[0]),stotime(t[1])]
                    if(n2<=1):
                        sub='1\n{0} --> {1}\n{2}'.format(t[0],t[1],a['text'])
                    else:
                        sub='{0}\n\n{1}\n{2} --> {3}\n{4}'.format(sub,n2,t[0],t[1],a['text'])
                fil = open('{0}（英文）.srt'.format(i[0]),'w')
                fil.write(sub)
                fil.close()
                captions = YouTubeTranscriptApi.list_transcripts(video_id=i2).find_transcript(['en']).translate('zh-Hans').fetch()
                n2=0
                for a in captions:
                    n2+=1
                    t=[a['start'],a['duration']]
                    t[1]+=t[0]
                    t=[stotime(t[0]),stotime(t[1])]
                    if(n2<=1):
                        sub='1\n{0} --> {1}\n{2}'.format(t[0],t[1],a['text'])
                    else:
                        sub='{0}\n\n{1}\n{2} --> {3}\n{4}'.format(sub,n2,t[0],t[1],a['text'])     
                fil = open('{0}（简体中文）.srt'.format(i[0]),'w')
                fil.write(sub)
                fil.close()
                fil = open('subtitlen.txt','w')
                fil.write(str(mn))
                fil.close()
                print('“{0}”字幕下载完成\n'.format(i[0]))
            gc.collect()
        print('normal')
    except:
        tryout()
if __name__ == '__main__':
    main()
