import os
import sys
import zipfile
import gc
for a in os.listdir(sys.path[0]):
    if(a.find('part6')!=-1 or a.find('part7')!=-1 or a.find('part8')!=-1 or a.find('part9')!=-1 or a.find('part10')!=-1 or a.find('part11')!=-1 or a.find('part12')!=-1 or a.find('part13')!=-1 or a.find('part14')!=-1 or a.find('part15')!=-1):
        print('“{0}”正在解压中……格式：{1}'.format(a[:-4],a[-3:].upper()))
        try:
            zipfile.ZipFile(a).extractall(pwd='vomebook'.encode())
        except RuntimeError as e:
            print(e)
        print('“{0}”解压完成'.format(a[:-3]))
    gc.collect()
