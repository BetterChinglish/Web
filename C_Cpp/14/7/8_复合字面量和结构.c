#include <stdio.h>

#define MAXTITL 41
#define MAXAUTL 31



//复合字面量和结构

//可以使用符合字面量创建一个结构作为函数的参数或赋给另一个结构


struct book {
    char tittle[MAXTITL];
    char author[MAXAUTL];
    float value;


};


int main()
{

    struct book readfirst;
    int score;
    printf("enter test score:");
    scanf("%d",&score);
    if (score>=84)
    {
        readfirst=(struct book) {   "Crime and Punishment",
                                    "Fydor Dostoyevsky",
                                    11.25};

    }
    else
    {
        readfirst=(struct book) {
            "Mr.Bouncy's Nice Hat",
            "Fred Winsome",
            5.99
        };
    }
    printf("Your assigned reading:\n");
    printf("%s by %s: $%.2f\n",readfirst.tittle,readfirst.author,readfirst.value);
    
    //还可以作为参数传递
    //也可以传递复合字面量的地址
    return 0;
    
}












