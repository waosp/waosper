#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <Python.h>
char* Substrend(char*str,int n)
{
	char *substr=(char*)malloc(n);
	int length=strlen(str);
	if (n>=length){
		strcpy(substr,str);
		return substr;
    }
	int k=0;
	for (int i=length-n;i<length;i++){
		substr[k]=str[i];
		k++;
	}
	substr[k]='\0';
	return substr;
}
/*
otr_fsend_python(const char *path,int fraglength)
{
    Py_Initialize();
    if(!Py_IsInitialized()){printf("初始化失败！");return 0;}
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('/home/waosp/Pictures')");
    PyObject *pmodule = PyImport_ImportModule("cutfile");
    if(pmodule==NULL){printf("Python文件不存在");Py_Finalize();return 0;}
    PyObject *pfunc = PyObject_GetAttrString(pmodule, "get_fragments");
    PyObject *args = Py_BuildValue(path,fraglength);
    PyObject *pRet = PyObject_CallFunction(pfunc,args);
    Py_Finalize();
    return 0;
}
*/
int main(void)
{
    FILE *fp;fp=fopen("/home/waosp/Downloads/gcc/otr.c","r");
    char *str;int len;char *head;char *mid;char size[16]={0};int cut=0;
    fseek(fp,0,SEEK_END);len=ftell(fp);fseek(fp,0,SEEK_SET);
    str=(char*)malloc(len*sizeof(char));
    if(str!=NULL){
        head="接收到了文件 大小:";
        fread(str,len*sizeof(char),1,fp);
        double lf=strlen(str);int strl=(int)lf;
        if(lf>100){cut=1;strl=100;}
        if(lf<=1){mid="bit\n";}
        else if(lf>1&&lf<1024){mid="bits\n";}
        else if(lf>=1024&&lf<1048576){lf=lf/1024;mid="kb\n";}
        else if(lf>=1048576&&lf<1073741824){lf=lf/1048576;mid="mb\n";}
        else{lf=lf/1073741824;mid="gb\n";}
        sprintf(size,"%f",lf);
        int len2=strlen(head)+strl+strlen(size)+strlen(mid);
        if(cut){strl=strl+4;}
        char *print=(char*)malloc(len2);strcpy(print,head);strcat(print,size);strcat(print,mid);
        if(cut){
            char str_beg[50];strncpy(str_beg,str,50);
            char *str_end=Substrend(str,50);
            strcat(print,str_beg);strcat(print,"\n……\n");strcat(print,str_end);
        }
        else{strcat(print,str);}
        printf("%s",print);
        free(str);
        //执行python脚本
        fp=popen("python cutfile.py Screenshot.jpg 1024", "r");
        fseek(fp,0,SEEK_END);len=ftell(fp);fseek(fp,0,SEEK_SET);
        str=(char*)malloc(len*sizeof(char));
        fread(str,len*sizeof(char),1,fp);
        char *msg[]=strtok(str,"\n");
        //pthread_t pyline;pthread_create(&pyline,NULL,&otr_fsend_python,&"/home/waosp/Pictures/Screenshot.jpg",&1024);
    }else{printf("请不要传递空文件，这样会为服务器制造更多的无形压力。");}
}
