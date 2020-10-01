#include <stdio.h>

#define LEN 20

struct name
{
    char first[LEN];
    char last[LEN];     
};

struct pname
{
    char* first;
    char* last;
};

int main()
{

    struct name name1;
    struct pname pname1;

    scanf("%s",name1.first);
    
    //scanf("%s",pname1.first);//错误
    char pnames[LEN];
    scanf("%s",pnames);
    pname1.first=pnames;

    printf("%s\n",name1.first);
    printf("%s",pname1.first);

    return 0;
}