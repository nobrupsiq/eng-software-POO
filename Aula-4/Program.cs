using System

namespace Aula-4 
{
    public class Program
    {
        static void Main(string[] args) 
        {
            Console.WriteLine("Ol�! Este � um projeto console em c#.");
            Console.WriteLine("Digite seu nome: ");
            string nome = Console.ReadLine();
            Console.WriteLine($"Prazer em te conhecer, {nome}!");
        }
    }
}