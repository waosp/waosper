import os,sys,gc,re
def fix_name(n,f,c):
    if(c):d=n.encode('cp437').decode('gbk')
    else:d=n
    d=re.sub('_c2','',d)
    d=re.sub('_c','',d)
    d=re.sub('_z','',d)
    d=re.sub('ep_','',d)
    d=re.sub('ep *\.','\.',d)
    d=re.sub('_p','',d)
    d=re.sub('_s','',d)
    d=re.sub('_',' ',d)
    d=re.sub('\s+',' ',d)
    d=re.sub(' \n','\n',d)
    d=re.sub('\d{8}','',d)
    d=re.sub('\d{7}','',d)
    d=re.sub('\d{6} \d{3}','',d)
    d=re.sub('＝','=',d)
    #城市化
    pt=' *([（）\(\);；,，［］《》<>“”‘’\"\':：、·\[\]\{\}『』\.。]) *'
    try:
        for r in re.findall(pt,d):
            pt2=re.sub('\{','\\\{',' *{} *'.format(r))
            pt2=re.sub('\}','\\\}',pt2)
            pt2=re.sub('\[','\\\[',pt2)
            pt2=re.sub('\]','\\\]',pt2)
            pt2=re.sub('\(','\\\)',pt2)
            pt2=re.sub('\)','\\\)',pt2)
            pt2=re.sub('\.','\\\.',pt2)
            d=re.sub(pt2,r,d)
    except:pass
    #喝牛奶
    d=re.sub('\(','（',d)
    d=re.sub('\)','）',d)
    d=re.sub('\[','［',d)
    d=re.sub('\]','］',d)
    d=re.sub(';','；',d)
    d=re.sub(',','，',d)
    d=re.sub(':','：',d)
    d=re.sub('\{','『',d)
    d=re.sub('\}','』',d)
    #割小草
    pt=' *([-=|]+) *'
    try:d=re.sub(pt,re.search(pt,d).groups()[0][:1],d)
    except:pass
    #施肥料
    pt=' *([^—])(—)([^—]) *'
    try:s=re.search(pt,d).groups();d=re.sub(pt,'{}{}{}{}'.format(s[0],s[1],s[1],s[2]),d)
    except:pass
    #砍大树
    pt=' *(—{2,}) *'
    try:d=re.sub(pt,re.search(pt,d).groups()[0][-2:],d)
    except:pass
    #松松土
    pt='(—{2})'
    try:d=re.sub(pt,' {} '.format(re.search(pt,d).groups()[0]),d)
    except:pass
    pt='([-=|]+)'
    try:d=re.sub(pt,' {} '.format(re.search(pt,d).groups()[0][:1]),d)
    except:pass
    #斩枯枝
    if(f):
        pt=' \W+\.(\w{1,4})$'
        try:d=re.sub(pt,'\.{}'.format(re.search(pt,d).groups()[0]),d)
        except:pass
    else:d=re.sub(' \W+$','',d)
    d=re.sub('（{2,}','（',d)
    d=re.sub('）{2,}','）',d)
    d=re.sub('[［【]{2,}','［',d)
    d=re.sub('[］】]{2,}','］',d)
    d=re.sub('；{2,}','；',d)
    d=re.sub('，{2,}','，',d)
    d=re.sub('：{2,}','：',d)
    d=re.sub('『{2,}','『',d)
    d=re.sub('』{2,}','』',d)
    d=re.sub('《{2,}','《',d)
    d=re.sub('》{2,}','》',d)
    d=re.sub('<{3,}','<<',d)
    d=re.sub('>{3,}','>>',d)
    d=re.sub('“{2,}','“',d)
    d=re.sub('”{2,}','”',d)
    d=re.sub('‘{2,}','“',d)
    d=re.sub('’{2,}','”',d)
    d=re.sub('\'{2,}','\"',d)
    d=re.sub('\"{2,}','\"',d)
    d=re.sub('：{2,}','：',d)
    d=re.sub('、{2,}','、',d)
    d=re.sub('·{2,}','·',d)
    d=re.sub('\.{2,}','\.',d)
    d=re.sub('。{2,}','。',d)
    if(f):
        pt=' \.(\w{1,4})$'
        try:d=re.sub(pt,'\.{}'.format(re.search(pt,d).groups()[0]),d)
        except:pass
    else:
        if(d[-1:]==' '):d=d[:-1]
    #翻译官
    d=re.sub('[一壹]','1',d)
    d=re.sub('[二贰]','2',d)
    d=re.sub('[三叁]','3',d)
    d=re.sub('[四肆]','4',d)
    d=re.sub('[五伍]','5',d)
    d=re.sub('[六陆]','6',d)
    d=re.sub('[七柒]','7',d)
    d=re.sub('[八捌]','8',d)
    d=re.sub('[九玖]','9',d)
    d=re.sub('[零〇]','0',d)
    #为了便于搜索系统工作，所以采用全部阿拉伯数字代替大多数汉字数字格式
    #拉拉架，取消是因为像《中国人的1997 香港问题面面观》这样的没法办
    '''
    pt='([a-zA-Z_\u4e00-\u9fa5])(\d+)([a-zA-Z_\u4e00-\u9fa5])'#这是排除了数字的\w
    try:
        for r in re.findall(pt,d):
            r=r.groups()
            pt=re.sub('{}{}{}'.format(r[0],r[1],r[2]),'{} {} {}'.format(r[0],r[1],r[2]),d)
    except:continue
    pt='([a-zA-Z_\u4e00-\u9fa5])(\d+)'
    try:
        for r in re.findall(pt,d):
            r=r.groups()
            pt=re.sub('{}{}'.format(r[0],r[1]),'{} {}'.format(r[0],r[1]),d)
    except:continue
    pt='(\d+)([a-zA-Z_\u4e00-\u9fa5])'
    try:
        for r in re.findall(pt,d):
            r=r.groups()
    '''
    return d
def fix_run(n,f):
    for d in n:
        p=os.path.join(sys.path[0],d)
        try:d=fix_name(d,f,True)
        except:d=fix_name(d,f,False)
        try:
            os.rename(p,os.path.join(sys.path[0],d))
            if(f):t='文件'
            else:t='目录'
            print('“{}”{}转码再整理完成'.format(d,t))
        finally:pass
for a,b,c in os.walk(sys.path[0]):
    fix_run(b,False)
    fix_run(c,True)
