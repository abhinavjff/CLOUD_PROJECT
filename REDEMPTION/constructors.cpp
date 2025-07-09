#include<iostream>
using namespace std;
//this code is basically showcases the uses of constructors 
//it is a method automatically called whenever the object is created and it is used for assigning values automatically 

class student {
    public:
    string name ;
    int age;
    double gpa;

    student(string name,int age,double gpa){
        this->name=name;
        this->age=age;
        this->gpa=gpa;

    }

};
int main()
{
    student student1("abhinav",21,7.52);
    student student2("virupa",22,8.02);

    cout<<"name is "<<student1.name<<endl;
    cout<<"age is "<<student1.age<<endl;
    cout<<"gpa is "<<student1.gpa<<endl;

    cout<<"name is "<<student2.name<<endl;
    cout<<"age is "<<student2.age<<endl;
    cout<<"gpa is "<<student2.gpa<<endl;

}