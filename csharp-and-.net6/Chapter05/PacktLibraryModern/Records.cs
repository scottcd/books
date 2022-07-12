using System;
using System.Collections.Generic;
using System.Text;


namespace Packt.Shared; // C# 10 file-scoped namespace
public class ImmutablePerson
{
    public string? FirstName { get; init; }
    public string? LastName { get; init; }
}
public record ImmutableVehicle
{
    public int Wheels { get; init; }
    public string? Color { get; init; }
    public string? Brand { get; init; }
}

// simpler way to define a record
// auto-generates the properties, constructor, and deconstructor
public record ImmutableAnimal(string Name, string Species);

