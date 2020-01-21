from selenium import webdriver
import selenium
import time
import urllib.request
import re
import gc
#def dayadjust(int month,int year):
#    m=0
#    if((month-1)==[1,3,5,7,8,10,12]):
#        r=31
#    elif((month-1)==[4,6,9,11]):
#        r=30
#    elif((month-1)==2):
#        if((year%4)==0):
#            r=29
#        else:
#            r=28
#    else:
#        r=31
#        m=1
#    return [r,m]
def reload_channel_messages(str):
    browser = webdriver.Firefox()
    browser.get(str)
    ps1=''
    ps2='failure'
    j='var q=document.documentElement.scrollTop=2000000000'
    while(ps1!=ps2):
        browser.execute_script(j)
        ps1=browser.page_source
        time.sleep(3)
        ps2=browser.page_source
        gc.collect()
    browser.quit()
    del browser
    del ps1
    del j
    gc.collect()
    #只有在7163和16636行有这个，并且后者的视频网格性质是固定的，前者不太理解
    #7159 16596行，共产主义潮流，前者不明，后者是视频网格，可见这二者的位置没有多大变动
    #于是第三个channel videos必然是两个<div id="items" class="style-scope ytd-grid-renderer">，并且仍要取第三个，即[2]的列表索引项
    #此处在共产主义潮流里在第17384-17385行，且</div>有换行，在乔森昂鲁赫那里是在19042-19043行，影响这个行位的是已加载的视频数目，这个东西可能有一个固定的行数，既然如此</div>也就没必要取了
    #我们可以由此得到结论，每一个视频相差41行，这是根据下面这一条搜索项的周期性得到的，但毕竟最后一个不可能是视频，所以要[:-2]，以防下面的程序无法执行文本分割而崩溃
    ps2=ps2.split('<div id=\"items\" class=\"style-scope ytd-grid-renderer\">')[2].split('<ytd-button-renderer id=\"show-more-button\" align-by-text=\"\" class=\"style-scope ytd-grid-renderer style-text size-default\" button-renderer=\"\" use-keyboard-focused=\"\" hidden=\"\"></ytd-button-renderer>')[0].split('</ytd-grid-video-renderer>')[:-2]
    #redic=['title','time','views','picture','length','link']
    #new redic=['title','time','views','link']
    #regro=[redic,redic,redic] 多层列表的实现
    regro=[]
    z=0
    zl=len(ps2)
    for i in ps2:
        redic=['','',0,'','','']
        z+=1
        #redic[3]=urllib.request.urlopen(t).read()，原库由于bug暂废弃不用，直接保存字符串#这里特别注意一下不能用open()，否则：FileNotFoundError: [Errno 2] No such file or directory: '……'，这说明open()不能访问互联网，或者说至多只能访问ftp服务器？
        #同样……意义不大还浪费时间！redic[3]=i.split('<img id=\"img\" class=\"style-scope yt-img-shadow\" alt=\"\" src=\"')[1].split('\"')[0]
        t=i.split('<a id=\"video-title\" class=\"yt-simple-endpoint style-scope ytd-grid-video-renderer\" aria-label=\"')[1].split('\"')[0].split('by')
        #Juan Guaido Installs his own Parliament once Removed from NA by Jason Unruhe 11 hours ago 4 minutes, 17 seconds 715 views
        #分割并重新整理单词“by”
        n=0
        nl=len(t)
        for b in t:
            n+=1
            if(n>=nl):
                redic[0]=redic[0][:-2]
                break
            else:
                redic[0]='{0}{1}by'.format(redic[0],b)
            gc.collect()
        t=t[nl-1].split(' ')
        #一个逆向循环
        n=0
        nl=len(t)
        for b in t:
            n+=1
            if(n>=nl-1):
                redic[1]=re.search('\d.*',redic[1][:-2]).group(0)
                break
            else:
                if(n<=2):
                    pass
                else:
                    redic[1]='{0}{1} '.format(redic[1],b)
            gc.collect()
        del n
        del nl
        del b
        gc.collect()
        redic[2]=int(t[-2].replace(',',''))
        del t
        gc.collect()
        #意义不大，redic[4]=i.split('<span class=\"style-scope ytd-thumbnail-overlay-time-status-renderer\" aria-label=\"')[1].split('\"')[0]
        redic[3]=i.split('<a id=\"thumbnail\" class=\"yt-simple-endpoint inline-block style-scope ytd-thumbnail\" aria-hidden=\"true\" tabindex=\"-1\" rel=\"null\" href=\"')[1].split('\"')[0]
        #节省内存空间
        if(z>=zl):
            regro.append(redic)
        else:
            regro.append(redic[:])
        gc.collect()
        #print ('第',z,'个视频:[标题:',redic[0],',时间:',redic[1],',播放量:',redic[2],'，图片,时长:',redic[4],',链接:',redic[5],']')
    #print(regro)
    return regro
    del regro
    del redic
    del i
    del ps2
    del z
    del zl
    gc.collect()
    #    ti=list(time.localtime(time.time()))#取时间秒
        #年份计算
    #    if(a.find(' years')!=-1):
    #        y=a.split(' years')[-2]
    #        y=y.split(' ')[-1]
    #    elif(a.find(' year')!=-1):
    #        y=a.split(' year')[-2]
    #        y=y.split(' ')[-1]
    #    else:
    #        y=0
    #    ti[0]-=int(y)
        #同理，月份
    #    if(a.find(' months')!=-1):
    #        y=a.split(' months')[-2]
    #        y=y.split(' ')[-1]
    #    elif(a.find(' month')!=-1):
    #        y=a.split(' month')[-2]
    #        y=y.split(' ')[-1]
    #    else:
    #        y=0
    #    ti[1]-=int(y)
    #    if(a.find(' days')!=-1):
    #        y=a.split(' days')[-2]
    #        y=y.split(' ')[-1]
    #    elif(a.find(' day')!=-1):
    #        y=a.split(' day')[-2]
    #        y=y.split(' ')[-1]
    #    else:
    #        y=0
    #    ti[2]-=int(y)
    #    if(a.find(' hours')!=-1):
    #        y=a.split(' hours')[-2]
    #        y=y.split(' ')[-1]
    #    elif(a.find(' hour')!=-1):
    #        y=a.split(' hour')[-2]
    #        y=y.split(' ')[-1]
    #    else:
    #        y=0
    #    ti[3]-=int(y)
    #    if(a.find(' minutes')!=-1):
    #        y=a.split(' minutes')[-2]
    #        y=y.split(' ')[-1]
    #    elif(a.find(' minute')!=-1):
    #        y=a.split(' minute')[-2]
    #        y=y.split(' ')[-1]
    #    else:
    #        y=0
    #    ti[4]-=int(y)
    #    if(a.find(' seconds')!=-1):
    #        y=a.split(' seconds')[-2]
    #        y=y.split(' ')[-1]
    #    elif(a.find(' second')!=-1):
    #        y=a.split(' second')[-2]
    #        y=y.split(' ')[-1]
    #    else:
    #        y=0
    #    ti[5]-=int(y)
        #格式化时间
    #    ti=[ti[0],ti[1],ti[2],ti[3],ti[4],ti[5]]
    #    if(ti[1]<=0):
    #        ti[1]+=12
    #        ti[0]-=1
    #    if(ti[2]<=0):
    #        d=dayadjust(ti[1],ti[0])
    #        ti[2]+=d[1]
    #        ti[1]-=d[2]
    #    if(ti[1]<=0):
    #        ti[1]+=12
    #        ti[0]-=1
    #    if(ti[3]<0):
    #        ti[3]+=24
    #        ti[2]-=1
    #    if(ti[2]<=0):
    #        d=dayadjust(ti[1],ti[0])
    #        ti[2]+=d[1]
    #        ti[1]-=d[2]
    #    if(ti[1]<=0):
    #        ti[1]+=12
    #        ti[0]-=1
    #   return
    
