using System;

namespace apresentacao
{
    public class Program
    {
        static void Main(string[] args)
        {
            Pessoa p1 = new Pessoa("Diego", "Inácio", 35);
            Pessoa p2 = new Pessoa("Maria", "Silva", 28);

            p1.Apresentar();
            p2.Apresentar();
        }
    }
}