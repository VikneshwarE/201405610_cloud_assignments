#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
using namespace std;

int main()
{
	char S[10005];
	int i;
	while(scanf(" %[^\n]s",S)!=EOF)
	{
		if(!strcmp(S,".cfi_startproc"))
		{
			cout<<S<<endl<<"subq	$8, %rsp"<<endl;
		}
		else if(strstr(S,".cfi_def_cfa_offset"))
			printf(".cfi_def_cfa_offset 16\n");
		else if(strstr(S,"movl	$9,"))
		{
			cout<<"movl	$9,%";
			printf("edx\n");
		}
		else if(strstr(S,"movl	$.LC0,"))
		{
			cout<<"movl	$.LC0,%";
			printf("esi\n");
		}
		else if(strstr(S,"movl	$1,"))
		{
			cout<<"movl	$1,%";
			printf("edi\n");
		}
		else if(!strcmp(S,"call	__printf_chk"))
		{
			cout<<"xorl	%";
			cout<<"eax, %";
			printf("eax\n");
			printf("call	__printf_chk\n");
			cout<<"xorl	%";
			cout<<"eax, %";
			printf("eax\n");
			cout<<"addq	$8, %rsp"<<endl;
			printf(".cfi_def_cfa_offset 8\n");
		}
		else if(!strcmp(S,"ret")||!strcmp(S,".cfi_endproc"))
		{
			printf("%s\n",S);
		}
	}
	return 0;
}


