/*
 * A1.cpp
 *
 *  Created on: May 13, 2021
 *      Author: ciarraw
 */

#include "A1.h"

A1::A1() {
	// TODO Auto-generated constructor stub

}

A1::~A1() {
	// TODO Auto-generated destructor stub
}

/* For the Week Two Lab assignment, you will submit two C++ programs, one for Task 1 and one for Task 2,

To summarize task 1 - Create a GenericStack class, which MUST store elements internally in a BasicContainer.
It should use only the public interface to BasicContainer,

## Interface includes following public functions, ##

- GenericStack(): no-argument constructor. Initializes the Stack to some pre-specified capacity.

- ~GenericStack (): destructor.

- GenericStack (const GenericStack <T>&): copy constructor.

- GenericStack<T>& operator= (const GenericStack <T>&): assignment operator.

- bool empty() const: returns true if the GenericStack contains no elements, and false otherwise.

- void push(const T& x): adds x to this GenericStack.

- void pop(): removes and discards the most recently added element of the GenericStack.

- T& top(): mutator that returns a reference to the most recently added element of the GenericStack.

- const T& top() const: accessor that returns the most recently added element of the GenericStack.

- int size(): returns the number of elements stored in this GenericStack.

- void print(std::ostream& os, char ofc = '\0') const: print this instance of GenericStack to ostream os.

The following non-member functions should also be supported:

- std::ostream& operator<< (std::ostream& os,const GenericStack<T>& a): invokes the print() method to print the GenericStack<T> a in the specified ostream.

- bool operator== (const GenericStack<T>&,const GenericStack <T>&): returns true if the two compared "GenericStack"s have the same elements, in the same order.

- bool operator< (const GenericStack<T>& a, const GenericStack <T>& b): returns true if every element in GenericStack a is smaller than corresponding elements of GenericStatck b, i.e., if repeatedly invoking top() and pop() on both a and b will generate a sequence of elements a_i from a and b_i from b, and for every i, a_i < b_i, until a is empty.

//For Task 2 - Your program should expect as input from (possibly re-directed) stdin a series of space- separated strings. If you read a1 (no space) this is the name of the variable a1 and not "a" followed by "1". Similarly, if you read "bb 12", this is a variable "bb" followed by the number "12" and not "b" ,"b", "12" or "bb", "1" ,"2". Your program should convert all Infix expressions to Postfix expressions, including expressions that contain variable names. The resulting Postfix expression should be printed to stdout. Your program should evaluate the computed Postfix expressions that contain only numeric operands, using the above algorithm, and print the results to stdout.

(5 + 3) * 12 - 7 is an infix arithmetic expression that evaluates to 89

5 + 3 * 12 – 7 is an infix arithmetic expression that evaluates to 34

Postfix arithmetic expressions (also known as reverse Polish notation) equivalent to the above examples are:

5 3 + 12 * 7 –

5 3 12 * + 7 –

// Following is code sample for GenericStack() class definition for your reference,  */

/// @brief 
/// @tparam GenericStackType 
/// @return 
template <class GenericStackType> class GenericStack {
GenericStackType *stck;
int tos;
int size;

public:
GenericStack() {
tos = 0;
size = 0;
}
GenericStack(int length)
{

}
stck = new GenericStackType[size];
}

~GenericStack(){
delete []stck;
}
void push(GenericStackType ob)
{

}

GenericStackType pop()
{

}
int Size()
{
return size;
}

GenericStackType operator= (const GenericStackType &right)
{

}
bool empty()
{
if(tos==0)
return true;
else
return false;
}

GenericStackType top() const
{

}

void print()
{

}
