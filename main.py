import os,sys,re,un7z,shutil
for a,b,c in os.walk(sys.path[0]):
    for d in b:
        if(os.path.exists(d)==True):
            try:
                if(int(re.search('\d+',d).group(0))>=17):
                    print('开始解压“{}”内文件'.format(d))
                    f=un7z.seven(d,'vomebook')
                    print(f,'解压完成——开始整理文件')
                    f2=[]
                    for a2,b2,c2 in os.walk(d):
                        for d2 in c2:
                            if(d2[-2:]=='7z' or d2[-3:]=='zip' or d2[-3:]=='uvz' or d2[-3:]=='rar'):
                                if(f2.count(a2)<1):print('再解压{}开始'.format(a2));f2.append(a2);f3=un7z.seven(a2,'vomebook');print(f3,'再解压完成')
                            elif(d2=='本书目由vomebook小组制作.jpg'):
                                try:os.remove(os.path.join(a2,d2));print('删除“本书目由vomebook小组制作.jpg”')
                                except:pass
                    f2=''
                    for f2 in f:
                        n=0;f2=f2.split('.');nl=len(f2)
                        for d2 in f2:
                            n+=1
                            if(n<=1):t=d2
                            elif(n>1 and n<nl):t='{}.{}'.format(t,d2)
                        p2=os.path.join(d,t)
                        for a2,b2,c2 in os.walk(p2):
                            for d2 in range(len(b2)):
                                if(d2==0):p3=os.path.join(p2,b2[d2]);shutil.move(p3,p2);print('移动子目录至父目录……');os.remove(p3);print('删除子目录')
                    print('“{}”处理完毕'.format(d))
            except:pass
