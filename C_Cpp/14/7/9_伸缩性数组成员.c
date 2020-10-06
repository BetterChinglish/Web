#include <stdio.h>

// 伸缩型数组成员
// 1 必须是结构的最后一个成员
// 2 结构中必须至少有一个成员
// 3 ·伸缩数组的声明类似于普通数组，只是它的方括号中是空的。

// struct flex
// {
//     int count;

//     double average;
//     double scores [];//伸缩型数组成员

// };// 声明一个struct flex类型的结构变量时，无法使用scores做任何事，因为没有给这个数组预留存储空间

// 目的：
// 实际上，C99的意图并不是让你声明struct flex类型的变量，
// 而是希望你声明一个指向struct flex类型的指针，
// 然后用malloc()来分配足够的空间，
// 以存储struct flex类型结构的常规内容和伸缩型数组成员所需的额外空间。

// 例如：
// struct flex * pf;
// pf = malloc(sizeof(struct flex) + 5 * sizeof(double));


int main(void)
{
    int a;
    


    return 0;
}