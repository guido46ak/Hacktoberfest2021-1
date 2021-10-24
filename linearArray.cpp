#include <iostream>

using namespace std;

int main()
{
   int arr[10], n=10, keyy;
   cout<<"Enter the array elements :"<<endl;
   for(int i=0; i<n; i++)
   {    
       cin>>arr[i];
   }
   cout<<"Enter a key: "<<endl;
   cin>>keyy;
   for(int i=0; i<n; i++)
   {   if(keyy == arr[i])
        {   cout<<"Element Found"<<i<<endl;
            exit(0);
        }
   }
    cout<<"Element isn't found";
   
   return 0;
}