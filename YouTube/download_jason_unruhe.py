#!/usr/local/bin/python3
from pytube import YouTube
from tkinter import *
import tkinter,rcm,gc,re,time,os,sys,psutil,numpy
#import math#import urllib.request#from PIL import Image, ImageTk#from io import BytesIO#from tkinter import font as tkFont
vg=[]
e=''
og=''
'''
#ytbc=False
#def blockp(ap):
#    #336x282
#    awa=int(c.winfo_geometry().split('x')[0])
#    aw=awa//336
#    aww=(awa%336)/(aw+1)#间隙值
#    del awa
#    gc.collect()
#    return(aww+(ap-1)%aw*(336+aww),8+((ap-1)//aw)*282)#动态的横向距离与纵向距离
#    del aw
#    del aww
#    del ap
#    gc.collect()
def if_connected():
    global ytbc
    if(urllib.request.urlopen('https://www.youtube.com').status==200):
        ytbc=True
    elif(ytbc=True):
        ytbc=False
    ontimer(if_connected,1000)
'''
sleep=0
def downline():
    #try:
    # Exception as e:
    #if(e.find('unavailable')==0 or e.find('urlopen error [Errno -2] Name or service not known')==0):
    print('睡眠两秒');time.sleep(2);global sleep;sleep+=1
    if(sleep>=5):
        global vg;sleep=0;m='missing.txt'
        tg=open('视频介绍.txt','r');a=tg.read().split('1GULzFrGD5标题trRqPB4@Ty')[:-1];tg.close();del tg
        a=len(a)+1;print('“{}”视频不可用\n'.format(vg[a-1][0]));global np;np=0
        if(os.path.exists(m)):f=open(m,'a');f.write('\n{}'.format(a));f.close();del f
        else:f=open(m,'w+');f.write(str(a));f.close();del f
        del m;l=len(vg);m='{}\n1GULzFrGD5标题trRqPB4@Ty\n此视频不可用，跳过\n==========描述=========='.format(vg[a-1][0])
        if(a-1<=0):lb='请勿使标题的二十二位密码多余出现在视频介绍里\n{}\n1GULzFrGD5标题trRqPB4@Ty\n此视频不可用，跳过\n==========描述==========\n'.format(vg[a-1][0])
        elif(a-1<l-1 and a-1>0):lb='{}\n'.format(m)
        else:lb=m
        tg=open('视频介绍.txt','a');tg.write(lb);tg.close()
        del lb;del l;del a;del m;global size,st;print(size,st)
    download()#如果去掉try except结构，这就是最起作用的部分#except:downline()
np,entire,progress,size,st=0,0,0,[],[]
def progress_callback(stream, chunk, file_handle, bytes_remaining):
    global np;np+=1;global entire;global progress,size,st
    if(np==1):entire=bytes_remaining;size.append(bytes_remaining/1048576);st.append(time.time())#如果下载出错，需要删除错误的st/size?
    elif(np==2):time.sleep(0.01);progress=entire-bytes_remaining;print('下载进度：{}% 进度：{}/{}(MB) 速度：{}MB/s'.format(round(100-bytes_remaining/entire*100,2),round(progress/1048576,2),round(entire/1048576,2),round(progress/10485.76,2)),end='\r')
    else:time.sleep(0.01);progress=entire-bytes_remaining-progress;print('下载进度：{}% 进度：{}/{}(MB) 速度：{}MB/s'.format(round(100-bytes_remaining/entire*100),round((entire-bytes_remaining)/1048576,2),round(entire/1048576,2),round(progress/10485.76,2)),end='\r');progress=entire-bytes_remaining
def download():
    global vg;l=len(vg);n=0
    try:
        tg='视频介绍.txt'
        if(os.path.exists(os.path.join(sys.path[0],tg))==True):tg=open(tg,'r');lg=len(tg.read().split('1GULzFrGD5标题trRqPB4@Ty')[:-1]);tg.close()
        else:lg=0;tg=open(tg,'w+');tg.close()
        del tg;n=0
        for la in vg:
            n+=1#在此处出错后，由于重新调用download函数，以至于lg一定会被更新
            if(n>=lg):
                yt=YouTube('https://www.youtube.com{0}'.format(la[5]));yt.register_on_progress_callback(progress_callback);global sleep
                if(sleep<=0):print('“{0}”正在下载中……ID：{1}'.format(la[0],la[5].split("=")[1]))
                s=yt.streams.first()#eventlet.monkey_patch()
                s.download(filename=la[0])
                #if(os.path.exists('{}.mp4'.format(la[0]))==False):raise Exception('File missing!')#文件下载失败
                del s;print('“{0}”下载完成。'.format(la[0]));global st,size;p=len(st)-1;st[p]=size[p]/(time.time()-st[p])#filename=yt.title.replace('&#39;','\'').replace('&39','\''))la[0]防止出现编码错误
                lg+=1;average_size=numpy.mean(size)*(l-lg);average_speed=numpy.mean(st)
                print('剩余整体平均大小：{}MB 剩余整体平均速度：{}MB/s 剩余整体平均预计时间：{}h'.format(round(average_size,2),round(average_speed,2),round(average_size/(average_speed*3600),2)))
                sleep=0;global np;np=0
                lb='{}\n1GULzFrGD5标题trRqPB4@Ty\n{}\n==========描述==========\n{}*时间*{}|播放量|{}+链接尾+'.format(la[0],yt.description.replace('&#39;','\'').replace('&39','\''),la[1],la[2],la[5])
                if(n<=0):lb='请勿使标题的二十二位密码多余出现在视频介绍里\n{}\n'.format(lb)
                elif(n<l-1 and n>0):lb='{}\n'.format(lb)
                file=open('视频介绍.txt','a');file.write(lb);file.close()
                mb=psutil.Process(os.getpid()).memory_info().rss/1048576;ta=''
                if(mb<200):ta='\n'
                print('内存占用：{}MB{}'.format(round(mb,2),ta))
                if(ta==''):print('内存占用过多，重启程序……\n');file=open('pass_setting.txt','w+');file.write('videoGroup.txt');file.close();os.execl(sys.executable,sys.executable,*sys.argv)
                del yt;del lb;del la;del file
    except:downline()
    #except Exception as e:
        #if(str(e)!='File missing!'):downline()
        #else:raise Exception('File missing!')
def analyzse():
    global e;global vg;vg=rcm.reload_channel_messages(e.get());fil2=fil='';n=0;il=len(vg)
    for i in vg:
        n+=1;n2=0;il2=len(vg[n-1])
        for i2 in vg[n-1]:
            n2+=1
            if(n2<=1):fil2='[\'{}\',\''.format(str(i2))
            elif(n2>1 and n2<il2):fil2='{}{}\',\''.format(fil2,str(i2))
            else:fil2='{}{}\']'.format(fil2,str(i2))
            del i2
        if(n<=1):fil='[\'{}\',\''.format(fil2)
        elif(n>1 and n<il):fil='{}{}\',\''.format(fil,fil2)
        else:fil='{}{}\']'.format(fil,fil2)
        file=open('videoGroup.txt','w+');file.write(fil);file.close()
        del i;del il2;del fil2;del n2;del file
    del il;del fil;del n
    gc.collect()
    #这一部分代码运行时太耗时了！#画布更新: global vg
    '''
    for aa in vg:
        #336x188
        n+=1
        aap=blockp(n)
        vg[n-1][3]=ImageTk.PhotoImage(Image.open(BytesIO(urllib.request.urlopen(aa[3]).read())).crop((0,45,480,315)).resize((336,188)))#在picture这里，我们应该选择后压缩法，把完整的图像留给下载者
        c.create_image(aap[0],aap[1],anchor='nw',image=vg[n-1][3])
        tl=ai=0
        tt=[]
        only=False
        black = tkFont.Font(family='黑体', size=11)
        n2=0
        nl2=len(aa[0])
        for tj in aa[0]:
            n2+=1
            tl+=black.measure(tj)
            if(tl>336):
                tt.append(aa[0][:ai])
                only=True
                break
            elif(n2>=nl2):
                tt.append(aa[0][:])
            ai+=1
            gc.collect()
        tl=ai2=0
        if(only):
            n2=0
            nl2=len(aa[0][ai:])
            for tj in aa[0][ai:]:
                tl+=black.measure(tj)
                n2+=1
                if(tl>336):
                    tt.append('{0}…'.format(aa[0][ai:ai+ai2]))
                    break
                elif(n2>=nl2):#切记，切记，别忘了前边的也要写这个，切记！
                    tt.append(aa[0][ai:])
                ai2+=1
                gc.collect()
            c.create_text(aap[0]+168,aap[1]+209,text=tt[1],font=('黑体',11))
        del tl
        del ai
        del ai2
        del tj
        del black
        del n2
        del nl2
        gc.collect()
        c.create_text(aap[0]+168,aap[1]+196,text=tt[0],font=('黑体',11))
        del tt
        gc.collect()
        c.create_text(aap[0]+168,aap[1]+225,text='{0}个观众 - {1}'.format(aa[2],aa[1]),font=('黑体',11))
        vg[n-1].append(0)#为每一个视频数据提供下载进度变量
        c.create_text(aap[0]+168,aap[1]+241,text='下载进度：{0}%'.format(vg[n-1][6]),font=('黑体',11))
        gc.collect()
    del aa
    del n
    del aap
    gc.collect()
    '''
def analyzse_download():analyzse();download()
def input():
    global vg;global og;vg=[];i=re.compile(r'\'\[\'.+?\'\]\'').findall(og.get())
    n=0;il=len(i);fil=['','','','','','']
    for i2 in i:
        n+=1;fil[0]=i2.split('\',\'');fil[1]=fil[0][1];fil[2]=int(fil[0][2]);fil[3]=fil[0][3];fil[4]=fil[0][4];fil[5]=fil[0][5][:-3];fil[0]=fil[0][0][3:][:-1]#以后改回来
        if(n>=il):vg.append(fil)
        else:vg.append(fil[:])
        del i2
    del i;del il;del n;gc.collect();print('一共导入视频数：{}'.format(len(vg)))
def main():
    app = tkinter.Tk();app.title('YouTube视频批量下载器 - waosp');app.geometry("800x64");app.update()
    '''
    global c
    c = Canvas(app,background='white')#一会需要规定滚动区
    c.pack(fill='both',expand='yes',side='bottom')
    '''
    Button(app,text='分析',font=('黑体',11),command=analyzse).pack(side='left',fill='y')
    Button(app,text='下载',font=('黑体',11),command=download).pack(side='left',fill='y')
    Button(app,text='分析&下载',font=('黑体',11),command=analyzse_download).pack(side='left',fill='y')
    Label(app,text="（注：100以上的视频资料下载需要一些时间）请输入批量视频所在链接：",font=('黑体',11)).pack(side="top")
    global e;e=tkinter.Variable();Entry(app,textvariable=e,font=('黑体',11)).pack(side="top",fill="x");Button(app,text='导入',font=('黑体',11),command=input).pack(side='left',fill='y');Label(app,text="请输入视频组：",font=('黑体',11)).pack(side='left',fill='y')
    global og;og=tkinter.Variable();Entry(app,textvariable=og,font=('黑体',11)).pack(side="top",fill="both")
    if(os.path.exists(os.path.join(sys.path[0],'pass_setting.txt'))==True):file=open('pass_setting.txt','r');r=file.read();file.close();file=open(r,'r');r=file.read();file.close();del file
    if(r!=''):og.set(r);del r;input();download()
    mainloop()
if __name__ == '__main__':main()
