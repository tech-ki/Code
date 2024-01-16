// See https://aka.ms/new-console-template for more information
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
namespace Home;

class Q1n1 {
    static void One(){
//Question 1.1 - Print a statement with 3 parts:
//Use string interpolation
var name = "Ki";

Console.WriteLine($"\n# Question 1.1\nHello, World! \nMy name is {name}. \nWelcome to Computer Science. \nProgramming is useful!");
    }
}

class Q1n2 {
public static void Two(){
//Question 1.2 - Write a statement that repeats 5 times.
string reps = new string('+',5).Replace("+","\nDo it again!");
Console.WriteLine(reps);

string apple = string.Join("\n", Enumerable.Repeat("Do it AGAIN!",5));
Console.WriteLine(apple);
     }
}

class Q1n3 {
    static void Three(){
//Question 1.3 - Display a  pattern that prints C# using the symbols only (level 02)
// All in letter C is C , All in letter # is #
    }
}

class Q1n4 {
    static void Four(){
//Question 1.4 - Print a table that sums from LtoR

    }
}

class Home
{ 
    static void Main(string[] args)
    { 
        //Q1n2 myObj = new Q1n2()
        Console.WriteLine("Hello, World!");
        Console.WriteLine("The current time is " + DateTime.Now);
    }
}
 
