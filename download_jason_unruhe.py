#!/usr/local/bin/python3
from pytube import Playlist
from pytube import YouTube
import tkinter
from tkinter import *
import rcm
#import math
#import urllib.request
import gc
import re
import time
import os
#from PIL import Image, ImageTk
#from io import BytesIO
#from tkinter import font as tkFont
vg=[]
#c=''
e=''
og=False
ogt=''
dg=False
dgt=''
ytbc=False
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
'''
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
    print('睡眠两秒')
    time.sleep(2)
    global sleep
    global vg
    sleep+=1
    if(sleep>=5):
        tg=open('视频介绍.txt','r').read().split('1GULzFrGD5标题trRqPB4@Ty')[:-1]
        a=len(tg)+1
        print('“{0}”视频不可用\n'.format(vg[a-1][0]))
        if(os.path.exists('missing.txt')):
            f=open('missing.txt','a')
            f.write('\n{0}'.format(a))
            f.close()
        else:
            f=open('missing.txt','w+')
            f.write(str(a))
            f.close()
        tg.close()
        tg=open('视频介绍.txt','a')
        if(a-1<=0):
            lb='请勿使标题的二十二位密码多余出现在视频介绍里\n{0}\n1GULzFrGD5标题trRqPB4@Ty\n此视频不可用，跳过\n==========描述==========\n'.format(vg[a-1][0])
        elif(a-1<l-1 and a-1>0):
            lb='{0}\n1GULzFrGD5标题trRqPB4@Ty\n此视频不可用，跳过\n==========描述==========\n'.format(vg[a-1][0])
        else:
            lb='{0}\n1GULzFrGD5标题trRqPB4@Ty\n此视频不可用，跳过\n==========描述=========='.format(vg[a-1][0])
        tg.write(lb)
        tg.close()
    gc.collect()
    download()#如果去掉try except结构，这就是最起作用的部分！！！！！
    #要为没有dg=False加一个使其dg=False的按钮
    #except:
    #   downline()
def download():
    global vg
    global dg
    l=len(vg)
    n=0
    if(dg):
        try:
            tg=open('视频介绍.txt','r').read().split('1GULzFrGD5标题trRqPB4@Ty')[:-1]
            n=0
            for la in vg:
                n+=1
                if(n>=len(tg)):
                    yt = YouTube('https://www.youtube.com{0}'.format(la[5]))
                    lb = la[5].split("=")
                    stream = yt.streams.first()
                    print('“{0}”正在下载中……ID：{1}'.format(la[0],lb[1]))
                    stream.download(filename=la[0])#filename=yt.title.replace('&#39;','\'').replace('&39','\''))la[0]防止出现编码错误
                    print('“{0}”下载完成。\n'.format(la[0]))
                    global sleep
                    sleep=0
                    file=open('视频介绍.txt','a')
                    if(n<=0):
                        lb='请勿使标题的二十二位密码多余出现在视频介绍里\n{0}\n1GULzFrGD5标题trRqPB4@Ty\n{1}\n==========描述==========\n{2}*时间*{3}|播放量|{4}+链接尾+\n'.format(la[0],yt.description,la[1],la[2],la[5])
                    elif(n<l-1 and n>0):
                        lb='{0}\n1GULzFrGD5标题trRqPB4@Ty\n{1}\n==========描述==========\n{2}*时间*{3}|播放量|{4}+链接尾+\n'.format(la[0],yt.description.replace('&#39;','\'').replace('&39','\''),la[1],la[2],la[5])
                    else:
                        lb='{0}\n1GULzFrGD5标题trRqPB4@Ty\n{1}\n==========描述==========\n{2}*时间*{3}|播放量|{4}+链接尾+'.format(la[0],yt.description.replace('&#39;','\'').replace('&39','\''),la[1],la[2],la[5])
                    file.write(lb)
                    file.close()
                gc.collect()
        except:
            downline()
    else:
        for la in vg:
            n+=1
            yt = YouTube('https://www.youtube.com{0}'.format(la[5]))
            lb = la[5].split("=")
            stream = yt.streams.first()
            print('“{0}”正在下载中……ID：{1}'.format(la[0],lb[1]))
            stream.download(filename=la[0])
            print('“{0}”下载完成。\n'.format(la[0]))
            file=open('视频介绍.txt','a')
            if(n<=1):
                lb='请勿使标题的二十二位密码多余出现在视频介绍里\n{0}\n1GULzFrGD5标题trRqPB4@Ty\n{1}\n==========描述==========\n{2}*时间*{3}|播放量|{4}+链接尾+\n'.format(la[0],yt.description.replace('&#39;','\'').replace('&39','\''),la[1],la[2],la[5])
            elif(n<l and n>1):
                lb='{0}\n1GULzFrGD5标题trRqPB4@Ty\n{1}\n==========描述==========\n{2}*时间*{3}|播放量|{4}+链接尾+\n'.format(la[0],yt.description.replace('&#39;','\'').replace('&39','\''),la[1],la[2],la[5])
            else:
                lb='{0}\n1GULzFrGD5标题trRqPB4@Ty\n{1}\n==========描述==========\n{2}*时间*{3}|播放量|{4}+链接尾+'.format(la[0],yt.description.replace('&#39;','\'').replace('&39','\''),la[1],la[2],la[5])
            file.write(lb)
            file.close()
            gc.collect()
    gc.collect()
def analyzse():
    #global c
    global e
    global vg
    global og
    if(og):
        og=False
        global ogt
        #执行适应导入的文本
        i=re.compile(r'\'\[\'.+?\'\]\'').findall(ogt.get())
        n=0
        il=len(i)
        fil=['','','','','','']
        for i2 in i:
            n+=1
            fil[0]=i2.split('\',\'')
            fil[1]=fil[0][1]
            fil[2]=int(fil[0][2])
            fil[3]=fil[0][3]
            fil[4]=fil[0][4]
            fil[5]=fil[0][5][:-3]
            fil[0]=fil[0][0][3:][:-1]#以后改回来
#            if(n<=1):
#                fil[0]=re.search('\'\[\'.+?\',\'',i2).group(0)[3:][:-4]
#                vg.append(fil[:])
#            elif(n>1 and n<il):
#                fil[1]=re.compile(r'\',\'.+?\',\'').findall(i2)
#                fil[3]=fil[1][1][3:][:-3]#
#                fil[1]=fil[1][0][3:][:-3]#
#                fil[1]=re.split(r'\',\'.+?\',\'',i2)
#                print(fil[1])
#                fil[2]=int(fil[1][1][3:][:-3])
#                fil[4]=fil[1][0][3:][:-3]
#                vg.append(fil[:])
#            else:
#                fil[5]=re.search('\',\'.+?\'\]\'',i2).group(0)[3:][:-3]
#                vg.append(fil)
            if(n>=il):
                vg.append(fil)
            else:
                vg.append(fil[:])
            gc.collect()
    else:
        vg=rcm.reload_channel_messages(e.get())
        file=open('videoGroup.txt','w')
        fil2=fil=''
        n=0
        il=len(vg)
        for i in vg:
            n+=1
            n2=0
            il2=len(vg[n-1])
            for i2 in vg[n-1]:
                n2+=1
                if(n2<=1):
                    fil2='[\'{0}\',\''.format(str(i2))
                elif(n2>1 and n2<il2):
                    fil2='{0}{1}\',\''.format(fil2,str(i2))
                else:
                    fil2='{0}{1}\']'.format(fil2,str(i2))
                gc.collect()
            if(n<=1):
                fil='[\'{0}\',\''.format(fil2)
            elif(n>1 and n<il):
                fil='{0}{1}\',\''.format(fil,fil2)
            else:
                fil='{0}{1}\']'.format(fil,fil2)
            gc.collect()
        file.write(fil)
        file.close()
        del il2
        del fil2
        del n2
        del file
        gc.collect()
    del i
    del i2
    del il
    del fil
    gc.collect()
    n=0
    #这一部分代码运行时太耗时了！
    #画布更新: global vg
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
def analyzse_download():
    analyzse()
    download()
    gc.collect()
def imput():
    global og
    og=True
    analyzse()
def d_imput():
    global dg
    dg=True
    download()
def main():
    app = tkinter.Tk()
    app.title('YouTube视频批量下载器 - waosp')
    app.geometry("800x128")
    app.update()
    #global c
    #c = Canvas(app,background='white')#一会需要规定滚动区
    #c.pack(fill='both',expand='yes',side='bottom')
    Button(app,text='分析',font=('黑体',11),command=analyzse).pack(side='left',fill='y')
    Button(app,text='下载',font=('黑体',11),command=download).pack(side='left',fill='y')
    Button(app,text='分析&下载',font=('黑体',11),command=download).pack(side='left',fill='y')
    Button(app,text='导入下载进度',font=('黑体',11),command=d_imput).pack(side='bottom',fill='y')
    Label(app,text="（注：100以上的视频资料下载需要一些时间）请输入批量视频所在链接：",font=('黑体',11)).pack(side="top")
    global e
    e = Entry(app,font=('黑体',11))
    e.pack(side="top",fill="x")
    Button(app,text='导入',font=('黑体',11),command=imput).pack(side='left',fill='y')
    Label(app,text="请输入视频组：",font=('黑体',11)).pack(side='left',fill='y')
    global ogt
    ogt = Entry(app,font=('黑体',11))
    ogt.pack(side="top",fill="both")
    mainloop()
if __name__ == '__main__':
    main()
'''
allLinks = []
pl = Playlist("https://www.youtube.com/playlist?list=PLbNXRaAKyCiNiUHoi6PYW0HqsY0ofi7jJ")
for la in pl.parse_links():
    yt = YouTube('https://www.youtube.com' + la)
    lb = la.split("=")
    stream = yt.streams.first()
    print('“' + yt.title + '”正在下载中……ID：'+lb[1])
    stream.download()
    print('“'+yt.title + '”下载完成。\n')
'''
main()
