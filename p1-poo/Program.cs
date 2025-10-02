using System;

namespace Aula
{
    public class Funcionario
    {
        private string? nome;
        private string? cpf;
        private double salario;

        public string Nome
        {
            get => nome;
            set => nome = value;
        }

        public string Cpf
        {
            get => cpf;
            set => cpf = value;
        }

        public double Salario
        {
            get => salario;
            set => salario = value;
        }

        public Funcionario(string n, string c, double s)
        {
            Nome = n;
            Cpf = c;
            Salario = s;
        }

        public void ApresentarDados()
        {
            Console.WriteLine("Nome: " + Nome);
            Console.WriteLine("CPF: " + Cpf);
            Console.WriteLine("Salário: " + Salario.ToString("C"));
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            string nome1 = "Zé da manga";
            string cpf1 = "12345678901";    
            double salario1 = 3500.75;

            if (nome1 == "" || nome1 == null)
            {
                Console.WriteLine("Nome não pode ser vazio.");
            }
            else if (cpf1 == null || cpf1.Length != 11)
            {
                Console.WriteLine("CPF deve conter 11 dígitos numéricos.");
            }
            else if (salario1 < 0)
            {
                Console.WriteLine("Salário não pode ser negativo.");
            }
            else
            {
                Funcionario f1 = new Funcionario(nome1, cpf1, salario1);
                f1.ApresentarDados();
            }

            // Teste com nome inválido
            string nome2 = "";
            string cpf2 = "12345678901";
            double salario2 = 3500.75;

            if (nome2 == "" || nome2 == null)
            {
                Console.WriteLine("Nome não pode ser vazio.");
            }
            else if (cpf2 == null || cpf2.Length != 11)
            {
                Console.WriteLine("CPF deve conter 11 dígitos numéricos.");
            }
            else if (salario2 < 0)
            {
                Console.WriteLine("Salário não pode ser negativo.");
            }
            else
            {
                Funcionario f2 = new Funcionario(nome2, cpf2, salario2);
                f2.ApresentarDados();
            }

            // Teste com CPF inválido
            string nome3 = "Fulano de tal";
            string cpf3 = "123";
            double salario3 = 3500.75;

            if (nome3 == "" || nome3 == null)
            {
                Console.WriteLine("Nome não pode ser vazio.");
            }
            else if (cpf3 == null || cpf3.Length != 11)
            {
                Console.WriteLine("CPF deve conter 11 dígitos numéricos.");
            }
            else if (salario3 < 0)
            {
                Console.WriteLine("Salário não pode ser negativo.");
            }
            else
            {
                Funcionario f3 = new Funcionario(nome3, cpf3, salario3);
                f3.ApresentarDados();
            }

            // Teste com salário inválido
            string nome4 = "Bruno pires";
            string cpf4 = "12345678901";
            double salario4 = -1000;

            if (nome4 == "" || nome4 == null)
            {
                Console.WriteLine("Nome não pode ser vazio.");
            }
            else if (cpf4 == null || cpf4.Length != 11)
            {
                Console.WriteLine("CPF deve conter 11 dígitos numéricos.");
            }
            else if (salario4 < 0)
            {
                Console.WriteLine("Salário não pode ser negativo.");
            }
            else
            {
                Funcionario f4 = new Funcionario(nome4, cpf4, salario4);
                f4.ApresentarDados();
            }
        }
    }
}