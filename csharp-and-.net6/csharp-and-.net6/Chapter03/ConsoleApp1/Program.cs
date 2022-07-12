using static System.Console;

// increment a after assigning it
int a = 3;
int b = a++;
WriteLine($"a is {a}, b is {b}");
//

// increment c before assigning it
int c = 3;
int d = ++c;
WriteLine($"c is {c}, d is {d}");
//

// arithmetic operators below:
int e = 11;
int f = 3;
double g = 11.0;
WriteLine($"e is {e}, f is {f}");
WriteLine($"e + f = {e + f}");
WriteLine($"e - f = {e - f}");
WriteLine($"e * f = {e * f}");
WriteLine($"e / f = {e / f}");
WriteLine($"e % f = {e % f}");

WriteLine($"g is {g:N1}, f is {f}");
WriteLine($"g / f = {g / f}");
//