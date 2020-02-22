import os,sys
def com(p,t,pre,aft)
    f=[]
    for a,b,c in os.walk(p):
        for d in c:
            un==False
            for e in t:
                if(d[-2:]==e or d[-3:]==e):un=True
            if(un):
                try:os.system('{}{}{}'.format(pre,d.replace('(','\(').replace(')','\)').replace(' ','\ '),aft));f.append(d[:])
                except:pass
    return f
