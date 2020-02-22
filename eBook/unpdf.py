import os,sys
from PyPDF2 import PdfFileReader
for a,b,c in os.walk(sys.path[0]):
    for d in c:
        if(d[:5]=='毛泽东集 第'):
            p=os.path.join(sys.path[0],d)
            d=PdfFileReader(open(p,'rb')).getDocumentInfo().title
            print(d)
            os.rename(p,os.path.join(sys.path[0],d))
