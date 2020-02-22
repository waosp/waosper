import PIL
def a(a):
    pr='paragraphs_result'
    if pr in a:
        wr,lo,pt,te='words_result','location',['left','top','width','height'],[]
        for b in a[pr]:
            t,s,n2='',[0,0,0,0],0
            for c in b['{}_idx'.format(wr)]:
                if(a[wr][c]['probability']['min']>0.4):
                    t,n2='{}{}'.format(t,a[wr][c]['words']),n2+1
                    if(n2<=1):s=[a[wr][c][lo][pt[0]],a[wr][c][lo][pt[0]]+a[wr][c][lo][pt[2]]]
                    else:
                        if(a[wr][c][lo][pt[0]]<s[0]):s[0]=a[wr][c][lo][pt[0]]
                        if(a[wr][c][lo][pt[0]]+a[wr][c][lo][pt[2]]>s[1]):s[1]=a[wr][c][lo][pt[0]]+a[wr][c][lo][pt[2]]
            if(t!=''):
                if(s[0]<=1632 and s[1]<=1632):te.append([False,t[:]])
                elif(s[0]>1632 and s[1]>1632):te.append([True,t[:]])
                elif((1632-s[0])>=(s[1]-1632)):te.append([False,t[:]])
                elif((1632-s[0])<(s[1]-1632)):te.append([True,t[:]])
                else:raise BaseException
        left,right=[],[]
        for b in te:
            if(b[0]):right.append(b[1][:])
            else:left.append(b[1][:])
        return [left,right]
    return None
def b(a,b):
    wr,pt,te='words_result',['left','top','width','height'],[]

