#include<iostream>
#include<vector>
using namespace std;
int main()
{
   vector<int> pr, rem;                    // vector that holds the coprimes and the remainders
   int i,num=1,n,flag=1;
   int p,r;
   cin>>n;                                 // number of inputs
   for(i=0;i<n;i++)
   {
     cin>>p>>r;
     pr.push_back(p);
     rem.push_back(r);
    }
    while(1)
    { flag=1;
      for(i=0;i<n;i++)
        if(num%pr[i] != rem[i])            // if the number does not satisfy we flag it
          { 
           flag=0;
          }
       if(flag==1)                        // if the flag does not change it means all conditions are satisfied
        break;
      num++;
     }
     cout<< num;
 return 0;
}

