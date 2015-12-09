#include <stdio.h>
#include <time.h>
#include <stdarg.h>
#include <vector>
#include <unistd.h>
#include <string.h>
#include <algorithm>
using namespace std;



void Log(const char* fmt, ...)
{
   struct tm* ptm;
   char strTime[1024] = {0};
   char logStr[1024] = {0};
   va_list ap;

   time_t cur = time(NULL);
   ptm = localtime(&cur);

   strftime(strTime, 1024, "%Y-%m-%d %H:%M:%S", ptm);

   //printf("%s\n", strTime);

   va_start(ap, fmt);
 
   vsprintf(logStr, fmt, ap);

   printf("[%s]: %s\n", strTime, logStr);
   va_end(ap);
}


typedef enum TBool{

    TRUE = 0,
    FALSE = 1
}TBool;


typedef struct NUM{
    char num[21];
    char type[5];

    NUM(){
    memset(num, 0, sizeof(num));
    memset(type, 0, sizeof(type)); 
    }
}DATA;

TBool readFile(const char* filename, vector<DATA>& ve)
{
    FILE* fd = fopen(filename, "r");
    if (NULL == fd)
    {
       Log("ERROR: open %s failed!\n", filename);

       return FALSE;
    }
    
    Log("read file ......");
    char tmpLine[102] = {0};
    int count = 0;
    while(!feof(fd))
    {
        memset(tmpLine, 0, sizeof(tmpLine));
        char *OK = fgets(tmpLine, sizeof(tmpLine), fd);
        if(NULL == OK)
        {
           Log("read end...");
           break;
        }
        DATA data;
        strncpy(data.num, tmpLine, strlen(data.num));
        ve.push_back(data);
        count++;
    }

    fclose(fd);


    Log("count=%d\n", count);
    Log("lastLine=%s\n", tmpLine);

    return TRUE;
}


bool Comp(const DATA& a, const DATA& b)
{
   return strcmp(a.num, b.num);
}

int main()
{


   Log("%s\n", "start ");
   char filename[] = "seqs.txt";
   vector<DATA> ve;


   readFile(filename, ve);
   Log("ve.size()=%d\n", ve.size());
   Log("first=%s, end=%s", ve[0].num, ve.back().num);
   sort(ve.begin(), ve.end(), Comp);
   Log("first=%s, end=%s", ve[0].num, ve.back().num);
   Log("%s\n", "end" );
   sleep(20);
   return 0;

}
