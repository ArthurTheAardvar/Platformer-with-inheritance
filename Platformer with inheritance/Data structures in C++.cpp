#include <stack>
#include <iostream>
using namespace std;

int main()
{
    stack <int> mystack; // set up an integer stack
    mystack.push(15); //push a bunch on numbers into it
    mystack.push(40);
    mystack.push(2);
    mystack.push(80);
    mystack.push(4);

    cout << "The stacks size is: " << mystack.size() << endl;
    cout << "its top is: " << mystack.top() << endl<< endl;

    cout << "Popping the stack elements: ";
    while (!mystack.empty())
    {
        cout << mystack.top() << " , ";
        mystack.pop();
    }
    cout << endl<< endl;

    cout << "its size is now: " << mystack.size() << endl;
}