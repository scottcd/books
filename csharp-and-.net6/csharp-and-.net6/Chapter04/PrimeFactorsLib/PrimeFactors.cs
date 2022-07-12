namespace PrimeFactorsLib;
public static class PrimeFactors
{
    public static string GetPrimeFactors(int number) 
    {
        string primeFactors = string.Empty;

        // Print the number of 2s that divide n
        while (number % 2 == 0)
        {
            primeFactors += (2 + " ");
            number /= 2;
        }

        // n must be odd at this point. So we can
        // skip one element (Note i = i +2)
        for (int i = 3; i <= Math.Sqrt(number); i += 2)
        {
            // While i divides n, print i and divide n
            while (number % i == 0)
            {
                primeFactors += (i + " ");
                number /= i;
            }
        }

        // This condition is to handle the case whien
        // n is a prime number greater than 2
        if (number > 2)
            primeFactors += (number);

        primeFactors = primeFactors.Trim(' ');

        return primeFactors;
    }
}