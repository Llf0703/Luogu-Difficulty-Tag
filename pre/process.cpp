#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("luogu.txt","r",stdin);
    freopen("luogu.php","a",stdout);
    string s;
    printf("<?php\n");
    while (getline(cin,s))
    {
        printf("$id['");
        for (int i=0;i<=4;i++) printf("%c",s[i]);
        printf("']=\"");
        printf("%c",s[6]);
        printf("\";\n");
    }
    printf("?>")
    return 0;
}