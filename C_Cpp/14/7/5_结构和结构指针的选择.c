#include <stdio.h>

struct member
{
    int a;
    int b;
};

struct member sum(const struct member *mem1, const struct member *mem2);


int main()
{
    struct member member1,member2;
    struct member member3;

    member1.a=10;
    member1.b=9;

    member2.a=9;
    member2.b=10;

    member3=sum(&member1, &member2);
    printf("%d\n%d",member3.a,member3.b);

    return 0;
}

struct member sum(const struct member *mem1, const struct member *mem2){
    struct member temple;
    temple.a = mem1->a + mem2->a;
    temple.b = mem1->b + mem2->b;
    return temple;
}
