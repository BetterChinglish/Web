#include <stdio.h>
#include <stdlib.h>

#define BUFSIZE 4096
#define SLEN 81

void append(FILE* source, FILE* dest)
{
    size_t bytes;
    static char temp[BUFSIZE];
    while ((bytes=fread(temp,sizeof(char),bytes,dest))>0)   
    {
        fwrite(temp,sizeof(char),bytes,dest);
    }

}

char * s_gets(char* st, int n)
{
    char* ret_val;
    char* find;
    ret_val = fgets(st, n, stdin);
    if(ret_val)
    {
        find=strchr(st,'\n');
        if(find)
        {
            *find='\0';

        }
        else
        {
            
            while (getchar()!='\n')
            {
                continue;
            }
            
        }
        
    }
    return ret_val;
}


int main(void)
{   
    FILE *fa, *fas;
    int files=0;
    char file_app[SLEN];
    char file_src[SLEN];
    int ch;
    puts("enter name of destination file: ");
    s_gets(file_app, SLEN);
    if((fa=fopen(file_app,"a+"))==NULL)
    {
        fprintf(stderr,"can't open %s\n",file_app);
        exit(EXIT_FAILURE);

    }
    if (setvbuf(fa,NULL,_IOFBF,BUFSIZ)!=0)
    {
        
    }




    return 0;
}