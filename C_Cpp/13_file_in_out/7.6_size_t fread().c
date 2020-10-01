/* 
size_t fread()函数原型：
size_t fread(void * restrict ptr,
size_t size,
size_t nmemb,
FILE * restrict fp
);
*/



/*
example:
double earnings[10];
fread(earnings,sizeof(double),10,fp);

*/


/*
fread()返回读出成功项的数量
正常返回值应该为nmemb
如果出错或者提前读到文件结尾，返回的值比nmemb小

*/