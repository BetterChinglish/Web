#include <stdio.h>

//预处理指令从#开始，长度仅限于一行，存在换行符的，在预处理前会把多行物理行处理为一行
#define TWO 2
#define OW "thousands city from\
 home\n"
#define FOUR TWO*TWO
#define PX printf("X is %d\n",x)
#define P "X is %d\n"

/*
每行#define由三部分组成
第一部分：#define指令本身
第二部分：选定的缩写（又称：宏）
    有些宏代表值，称为类对象宏，如本例中的
    还有类函数宏，稍后讨论
    宏的名称中不允许有空格，命名规则遵守c语言规范
第三部分：成为替换列表或替换体
    预处理器找到宏的实例后，用替换提代替宏
    从宏变成最终替换文本的过程称为宏展开

宏定义还可以包含其他宏，如本例中的#define FOUR TWO*TWO


*/

int main()
{
    int x=TWO;
    PX;
    x=FOUR;
    printf(P,x);
    printf("%s",OW);
    printf("TWO:OW\n");




    return 0;
}