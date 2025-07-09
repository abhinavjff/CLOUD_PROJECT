#include<iostream>
using namespace std;
//define the class which is a template 

class dev{

    public:
    string name;
    string job;
    int salary;

    void work()
    {
        cout<<"bro is cookin"<<endl;
    }

    void enjoy()
    {
        cout<<"bro deserved the rest"<<endl;
    }
    

};


int main(){
    //imma reinforce the information that i am an amazing developer using this example of classes and objects.
    //this is a demo of classes and objects

    dev dev1;
    dev1.name="abhinav";
    dev1.job="backend genius";
    dev1.salary=100000;
    cout<<"name of the developer is "<<dev1.name<<endl;
    cout<<"role of the developer is "<<dev1.job<<endl;
    cout<<"salary of the developer is "<<dev1.salary<<endl;
    dev1.work();
    dev1.enjoy();

}