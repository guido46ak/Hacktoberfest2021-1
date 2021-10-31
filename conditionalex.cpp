#include<iostream>

using namespace std;

//checking if-else statements

int main(){
	int age;
	cout<<"Whats ur age ??"<<endl;
	cin>>age;
	
	if((age<18)&&(age>1)){
		cout<<"Minor!"<<endl;
	}
	else if(age==18){
		cout<<"Guardian Needed !"<<endl;
	}
	else if(age<1){
		cout<<"Not born! lol :)"<<endl;
	}
	else{
		cout<<"Not a Minor" <<endl;
	}
	
	return 0;
}
