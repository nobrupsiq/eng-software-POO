class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def resumo(self):   
        return f"{self.titulo}, escrito por {self.autor} em {self.ano}."

    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}"

class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_pegos = []

    def pegar_livro(self, livro):
        self.livros_pegos.append(livro)

    def listar_livros(self):
        return [str(livro) for livro in self.livros_pegos]

    def __str__(self):
        return f"Usuário: {self.nome}"

class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.livros = []
        self.emprestimos = {}

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar(self, usuario, livro):
        if livro in self.livros:
            usuario.pegar_livro(livro)
            if usuario not in self.emprestimos:
                self.emprestimos[usuario] = []
            self.emprestimos[usuario].append(livro)
            self.livros.remove(livro)
        else:
            print(f"O livro '{livro.titulo}' não está disponível na biblioteca.")

    def listar_emprestimos(self):
        emprestimos_list = {}
        for usuario, livros in self.emprestimos.items():
            emprestimos_list[usuario.nome] = [str(livro) for livro in livros]
        return emprestimos_list

    def buscar_livros_emprestados_por_usuario(self, usuario):
        return [str(livro) for livro in self.emprestimos.get(usuario, [])]

    def buscar_usuarios_por_livro(self, livro):
        usuarios = []
        for usuario, livros in self.emprestimos.items():
            if livro in livros:
                usuarios.append(usuario.nome)
        return usuarios

    def __str__(self):
        return f"Biblioteca: {self.nome}, Endereço: {self.endereco}"

def main():
    livro1 = Livro("Teste do teste", "Alguem", 1949)
    livro2 = Livro("O Senhor dos Anéis", "Fulano", 2025)

    usuario1 = Usuario("Alice", "001")
    usuario2 = Usuario("Bob", "002")

    biblioteca = Biblioteca("Biblioteca da faculdade", "Rua ali perto, 123")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    biblioteca.emprestar(usuario1, livro1)
    biblioteca.emprestar(usuario2, livro2)

    print(biblioteca.listar_emprestimos())
    print(biblioteca.buscar_livros_emprestados_por_usuario(usuario1))
    print(biblioteca.buscar_usuarios_por_livro(livro1))
    print(livro1.resumo())
    print(usuario1.listar_livros())
    print(biblioteca)
    print(usuario1)
    print(usuario2)
    
if __name__ == "__main__":
    main()