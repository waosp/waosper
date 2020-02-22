#['主标题',[[副标题,多选与否,[[选项文本,回显文本],<更多的迭代>]],<更多的迭代>],'完成语']
#[[在第一页的选项],第二页的选项……]
import gc
def gui(gui):
    pl,sl,r=0,[],[]
    while(True):
        pr,n,t='{}\n{}\n{}\n'.format(repr(r),gui[0],gui[1][pl][0]),0,'无'
        for a in gui[1][pl][2]:n+=1;pr='{}±{}.{}\n'.format(pr,n,a[0])
        if(pl==0):pr='{}{}.下一步\n{}.退出\n'.format(pr,n+1,n+2)
        elif(len(gui[1])-1>pl>0):pr='{}{}.下一步\n{}.返回\n'.format(pr,n+1,n+2)
        else:pr='{}{}.完成\n{}.返回\n'.format(pr,n+1,n+2)
        for a in range(len(sl)):
            t=gui[1][pl][2][sl[a]][1] if(a==0) else '{},{}'.format(t,gui[1][pl][2][sl[a]][1])
        print("\033c", end="")
        print('{}已选择：{}'.format(pr,t));i=input()
        if(isinstance(i,float)):print('警告：输入小数将会被向下取整\n')
        try:i=int(i)
        except:print('错误：请输入数字\n');continue
        if(len(sl)>=i>=1):
            if(gui[1][pl][1]):
                if(len(sl)==0):sl.append(int(i))
                else:print('错误：已选择选项\n')
            else:
                if(sl.count(i)==0):sl.append(int(i))
                else:print('警告：所添加项已存在\n')
        elif(-len(sl)<=i<=-1):
            i=-i
            if(gui[1][pl][1]):
                if(sl.count(i)==1):sl.remove(i)
                else:print('错误：未选择选项\n')
            else:
                if(sl.count(i)==1):sl.remove(i)
                else:print('警告：所添加项不存在\n')
        elif(i==len(sl)+1):
            if(pl!=len(gui[1]-1)):pl+=1;r.append(sl[:]);sl=[]
            else:print(gui[2]);del gui,pl,sl,r,pr,n,t,a,i;gc.collect();return r
        elif(i==len(sl)+2):
            if(pl!=0):pl-=1;r=r[:-1];sl=[]
            else:del gui,pl,sl,r,pr,n,t,a,i,r;gc.collect();return None
        else:print('错误：请按菜单输入\n')
