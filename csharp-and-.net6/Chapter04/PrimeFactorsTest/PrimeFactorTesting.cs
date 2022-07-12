using Xunit;
using PrimeFactorsLib;
namespace PrimeFactorsTest;

public class PrimeFactorTesting
{
    [Fact]
    public void PrimeFactorofFour()
    {
        // arrange
        int number = 4;
        string expected = "2 2";
        // act
        string answer = PrimeFactors.GetPrimeFactors(number);
        // assert
        Assert.Equal(expected, answer);
    }

    [Fact]
    public void PrimeFactorofSeven()
    {
        // arrange
        int number = 7;
        string expected = "7";
        // act
        string answer = PrimeFactors.GetPrimeFactors(number);
        // assert
        Assert.Equal(expected, answer);
    }

    [Fact]
    public void PrimeFactorofThirty()
    {
        // arrange
        int number = 30;
        string expected = "2 3 5";
        // act
        string answer = PrimeFactors.GetPrimeFactors(number);
        // assert
        Assert.Equal(expected, answer);
    }

    [Fact]
    public void PrimeFactorofForty()
    {
        // arrange
        int number = 40;
        string expected = "2 2 2 5";
        // act
        string answer = PrimeFactors.GetPrimeFactors(number);
        // assert
        Assert.Equal(expected, answer);
    }

    [Fact]
    public void PrimeFactorofFifty()
    {
        // arrange
        int number = 50;
        string expected = "2 5 5";
        // act
        string answer = PrimeFactors.GetPrimeFactors(number);
        // assert
        Assert.Equal(expected, answer);
    }
}
