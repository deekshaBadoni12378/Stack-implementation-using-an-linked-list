#include<iostream>
#include <bits/stdc++.h>
using namespace std;
struct Node
{
	int data;
	Node* link;
};

Node* top;
void push(int data)
{
	Node* temp = new Node();
    if (!temp)
	{
		cout << "\n Overflow";
		exit(1);
	}

	temp->data = data;


	temp->link = top;

	top = temp;
}


int isEmpty()
{

	return top == NULL;
}

int peek()
{
	if (!isEmpty())
		return top->data;
	else
		exit(1);
}void pop()
{
	Node* temp;

	if (top == NULL)
	{
		cout << "\n Underflow" << endl;
		exit(1);
	}
	else
	{
		temp = top;
		top = top->link;
        free(temp);
	}
}
void display()
{
	Node* temp;
    if (top == NULL)
	{
		cout << "\n Underflow";
		exit(1);
	}
	else
	{
		temp = top;
		while (temp != NULL)
		{
           cout << temp->data << "-> ";

			temp = temp->link;
		}
	}
}


int main()
{
	push(10);
	push(12);
	push(14);
	push(16);

	display();
cout << "\n1st  element is "
		<< peek() << endl;


	pop();
	pop();

	display();


	cout << "\n1st element is "
		<< peek() << endl;

	return 0;
}
