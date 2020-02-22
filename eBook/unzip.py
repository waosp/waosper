import os,sys
for a,b,c in os.walk(sys.path[0]):
    for d in c:
        if(d[-3:]=='zip' or d[-3:]=='uvz'):
            try:
                os.system('unar {} -p vomebook'.format(d).replace('(','*').replace(')','*'))
            except:
                pass
