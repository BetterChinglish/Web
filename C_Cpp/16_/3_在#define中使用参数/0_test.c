#include <stdio.h>

// #define MEAN(X,Y) {((X)+(Y))/2}
        //宏（宏参数    替换体

#define Square(x) x*x
//注意在计算中，预处理器将宏替换为其替换体，故而可能产生一些不符合预期的错误
//例如：Square(4)=16,但是100/Square(4)=100/4*4=100,以及Square(x+2)=x+2*x+2=3*x+2

//解决方法：增加括号，强制转换优先级：
#define SQUARE(x) ((x)*(x))


int main()
{
    // 这看上去像函数调用，但是它的行为和函数调用完全不同
    int y=Square(13);
    int z=100/Square(4);

    printf("%d\n",z);
    printf("%d\n",y);

    int y1=SQUARE(13);
    int z1=100/SQUARE(4);

    printf("%d\n",z1);
    printf("%d\n",y1);
    return 0;
}