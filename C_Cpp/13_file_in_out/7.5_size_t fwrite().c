/*
fwrite()函数原型：
size_t fwrite
(const void * restrict ptr, 
size_t size, 
size_t nmemb, 
FILE * restrict fp)
*/

// size_t   是根据标准C类型定义的类型，是sizeof运算符返回的类型，通常是unsigned int
// ptr      是待写入数据块的地址
// size     表示带写入数据块的大小（以字节为单位）
// nmemb    表示带写入数据块的数量
// fp       指定带写入的文件

/*
例如：
char buffer[256];
fwrite(buffer,256,1,fp)

*/

