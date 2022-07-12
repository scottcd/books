// See https://aka.ms/new-console-template for more information
using System;
using System.Xml.Linq;
using static System.Console;

Console.WriteLine("Hello, World!");
XDocument doc = new();

/*
    Relating C# keywords to .NET types
 */
string s1 = "Hello";
String s2 = "World";
WriteLine($"{s1} {s2}");