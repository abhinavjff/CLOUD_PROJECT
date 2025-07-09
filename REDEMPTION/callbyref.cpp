#include <bits/stdc++.h>
using namespace std;

int main() {

	int T;
	cin>>T;
	for(int j=0;j<=T;j++)
	{
	vector<int> vec;
	int N;
	cin>>N;
	for (int i=0;i<=N;i++)
	{
	    vec[i]=i+1;
	}
	
	for(int i=0;i<=N;i++)
	{
	    cout<<vec[i]<<" ";
	}
	
	}

}
