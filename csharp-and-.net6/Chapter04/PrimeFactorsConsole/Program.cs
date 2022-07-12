using PrimeFactorsLib;


int [] numbers = { 2, 4, 7, 30, 40, 50 };

foreach (var number in numbers)
{
    GetPrimeFactors(number);
}



void GetPrimeFactors(int number){
    string answer = PrimeFactors.GetPrimeFactors(number);
    Console.WriteLine($"prime factor of {number} is: {answer}.");
}