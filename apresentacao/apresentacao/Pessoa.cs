using System;

public class Pessoa
{
    // Atributos (propriedades públicas)
    public string Nome { get; set; }
    public string Sobrenome { get; set; }
    public int Idade { get; set; }

    // Construtor
    public Pessoa(string nome, string sobrenome, int idade)
    {
        Nome = nome;
        Sobrenome = sobrenome;
        Idade = idade;
    }
    public void Apresentar()
    {
        Console.WriteLine($"Olá, meu nome é {Nome} {Sobrenome} e tenho {Idade} anos.");
    }
}