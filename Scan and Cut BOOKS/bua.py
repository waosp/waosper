def a(a,a2,cr,ep,mi):#cr:center rate;ep:extend compare;mi:probability minium value
    ha,ep,wr=a2/2,ep+1,'words_result'
    if wr in a:
        lo,pt,m,ptb='location',['left','width'],[-1,999999999],[False,False]
        for b in a[wr]:
            if(b['probability']['min']>=mi):
                s=[b[lo][pt[0]],b[lo][pt[0]]+b[lo][pt[1]]]
                if(s[0]<=ha and s[1]<=ha and ptb[0]==False):ptb[0]=True
                elif(s[0]>ha and s[1]>ha and ptb[1]==False):ptb[1]=True
                if(ptb[0] and ptb[1]):break
        if(ptb[0] and ptb[1]):
            ptc=False
            for b in a[wr]:
                if(b['probability']['min']>=mi):
                    s=[b[lo][pt[0]],b[lo][pt[0]]+b[lo][pt[1]]]
                    if(s[0]<=ha and s[1]<=ha):
                        if(s[1]>m[0]):m[0]=s[1]
                    elif(s[0]>ha and s[1]>ha):
                        if(s[0]<m[1]):m[1]=s[0]
                    elif not(abs(s[0]-ha)>=ha*cr and abs(s[1]-ha)>=ha*cr):#即超限连接字符
                        if not ptc:ptc=True
                        if((ha-s[0])>=(s[1]-ha)*ep):
                            if(s[1]>m[0]):m[0]=s[1]
                        elif((ha-s[0])*ep<(s[1]-ha)):
                            if(s[0]<m[1]):m[1]=s[0]
        elif ptb[0]:
            m=-1
            for b in a[wr]:
                if(b['probability']['min']>=mi):
                    s=b[lo][pt[0]]+b[lo][pt[1]]
                    if(s>m):m=s
        elif ptb[1]:
            m=999999999
            for b in a[wr]:
                if(b['probability']['min']>=mi):
                    s=b[lo][pt[0]]
                    if(s<m):m=s
        if(isinstance(m,int)):
            if(abs(m-ha)>=ha*cr):m=ha
            return m
        elif(len(m)==2):
            if(m==[-1,999999999]):m=[0,ha]
            m=(m[0]+m[1])//2
            if(abs(m-ha)>=ha*cr and not ptc):m=ha
            return m
    return None
