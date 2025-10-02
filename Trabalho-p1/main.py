class Chave:
    def __init__(self, id_chave: str):
        # Atributo privado para o identificador da chave
        self.id_chave = id_chave

    def id_valido(self, id_para_validar: str) -> bool:
        return self.id_chave == id_para_validar

    def get_id(self) -> str:
        return self.id_chave

class Carro:
    # Mapeamento para os valores de aceleração por marcha
    ACELERACAO_POR_MARCHA = {1: 5, 2: 10, 3: 15}  # Adaptação da regra: 1ª +5, 2ª +10, 3ª +15
    
    def __init__(self, id_chave: str):
        # Atributos de estado do carro
        self.id_chave = id_chave         
        self.porta_aberta = False         
        self.ligado = False               
        self.velocidade = 0.0             
        self.marcha = 0                   
        self.pessoa_dentro = None
        self.log = []        

    def log_de_ação(self, acao: str, sucesso: bool, detalhes: str = ""):
        status = "SUCESSO" if sucesso else "FALHA"
     
        # Formato do log
        log_entrada = f"[{status}] - Ação: {acao}. {detalhes}"
        self.log.append(log_entrada)
        
    def exibir_historico(self):
        print("\n--- HISTÓRICO DE AÇÕES DO CARRO ---")
        if not self.log:
            print("Nenhuma ação registrada.")
            return
        for log in self.log:
            print(log)
        print("-----------------------------------")
    
    def validar_chave(self, chave: Chave) -> bool:
        return chave.id_valido(self.id_chave)

    def esta_parado(self) -> bool:
        return self.velocidade == 0.0

    # Métodos de comportamento de interação com Chave

    def abrir(self, chave: Chave) -> bool:
        if not self.validar_chave(chave):
            self.log_de_ação("Abrir Porta", False, "Chave incorreta.")
            print("Carro: FALHA - Chave incorreta. Não foi possível abrir a porta.")
            return False
        
        if self.porta_aberta:
            self.log_de_ação("Abrir Porta", True, "Porta já estava aberta.")
            print("Carro: Aviso - Porta já está aberta.")
            return True
        
        self.porta_aberta = True
        print("Carro: SUCESSO - Porta aberta.")
        return True

    def fechar(self, chave: Chave) -> bool:
        if not self.validar_chave(chave):
            self.log_de_ação("Fechar Porta", False, "Chave incorreta.")
            print("Carro: FALHA - Chave incorreta. Não foi possível fechar a porta.")
            return False
        
        if not self.porta_aberta:
            self.log_de_ação("Fechar Porta", True, "Porta já estava fechada.")
            print("Carro: Aviso - Porta já está fechada.")
            return True

        self.porta_aberta = False
        print("Carro: SUCESSO - Porta fechada.")
        return True

    def entrar_pessoa(self, pessoa) -> bool:
        if not self.porta_aberta:
            self.log_de_ação("Entrar no Carro", False, "Porta fechada.")
            print("Carro: FALHA - Porta fechada. A pessoa não pode entrar.")
            return False
        
        if self.pessoa_dentro is not None:
            self.log_de_ação("Entrar no Carro", False, "Carro já ocupado.")
            print("Carro: FALHA - Já tem uma pessoa no carro.")
            return False

        self.pessoa_dentro = pessoa
        print(f"Carro: SUCESSO - {pessoa.nome} entrou no carro.")
        return True

    def permitir_saida(self, pessoa) -> bool:
        # A pessoa deve ser a que está dentro
        if self.pessoa_dentro != pessoa:
            self.log_de_ação("Sair do Carro", False, "Pessoa não está no carro.")
            print(f"Carro: FALHA - {pessoa.nome} não está neste carro.")
            return False
        
        # Sair: carro desligado
        if self.ligado:
            self.log_de_ação("Sair do Carro", False, "Carro ligado.")
            print("Carro: FALHA - Carro ligado. Desligue antes de sair.")
            return False

        if not self.porta_aberta:
            self.log_de_ação("Sair do Carro", False, "Porta fechada.")
            print("Carro: FALHA - Porta fechada. A pessoa não pode sair.")
            return False

        self.pessoa_dentro = None
        print(f"Carro: SUCESSO - {pessoa.nome} saiu do carro.")
        return True

    def ligar(self, pessoa) -> bool:
        if self.ligado:
            self.log_de_ação("Ligar Carro", True, "Carro já estava ligado.")
            print("Carro: Aviso - Carro já está ligado.")
            return True
            
        if self.porta_aberta:
            self.log_de_ação("Ligar Carro", False, "Porta aberta.")
            print("Carro: FALHA - Porta aberta. Feche a porta para ligar.")
            return False
        
        if self.pessoa_dentro is None:
            self.log_de_ação("Ligar Carro", False, "Sem pessoa dentro.")
            print("Carro: FALHA - Sem pessoa dentro. Não é possível ligar.")
            return False
        
        # Validar chave a pessoa que está dentro deve ter a chave
        if not self.validar_chave(pessoa.chave):
            self.log_de_ação("Ligar Carro", False, "Chave incorreta.")
            print("Carro: FALHA - Pessoa dentro mas chave incorreta. Não pode ligar.")
            return False
            
        self.ligado = True
        print("Carro: SUCESSO - Motor ligado. Marcha atual: 0 (Ponto Morto).")
        return True

    def desligar(self, pessoa) -> bool:
        if not self.ligado:
            self.log_de_ação("Desligar Carro", True, "Carro já estava desligado.")
            print("Carro: Aviso - Carro já está desligado.")
            return True

        if not self.esta_parado():
            self.log_de_ação("Desligar Carro", False, "Carro em movimento.")
            print("Carro: FALHA - Carro em movimento. Pare o carro para desligar.")
            return False
            
        # Validar chave (a pessoa que está dentro deve ter a chave)
        if not self.validar_chave(pessoa.chave):
            self.log_de_ação("Desligar Carro", False, "Chave incorreta.")
            print("Carro: FALHA - Pessoa dentro mas chave incorreta. Não pode desligar.")
            return False
            
        self.ligado = False
        self.marcha = 0
        print("Carro: SUCESSO - Motor desligado.")
        return True
    
    def trocar_marcha(self, marcha: int) -> bool:
        if not self.ligado:
            self.log_de_ação("Trocar Marcha", False, "Carro desligado.")
            print("Carro: FALHA - Carro desligado. Não pode trocar marcha.")
            return False
        
        if self.velocidade > 0 and marcha == 0:
            self.log_de_ação("Trocar Marcha", False, "Carro em movimento.")
            print("Carro: FALHA - Precisa parar para ir para o Ponto Morto.")
            return False

        if marcha not in [0, 1, 2, 3]: # Exemplo de marcha
            self.log_de_ação("Trocar Marcha", False, f"Marcha {marcha} inválida.")
            print(f"Carro: FALHA - Marcha {marcha} inválida (use 0, 1, 2 ou 3).")
            return False
        
        self.marcha = marcha
        print(f"Carro: SUCESSO - Marcha trocada para {marcha}.")
        return True

    def acelerar(self, pessoa) -> bool:
        if not self.ligado:
            self.log_de_ação("Acelerar", False, "Carro desligado.")
            print("Carro: FALHA - Carro desligado. Não pode acelerar.")
            return False
        
        # Validar chave (a pessoa que está dentro deve ter a chave)
        if not self.validar_chave(pessoa.chave):
            self.log_de_ação("Acelerar", False, "Chave incorreta.")
            print("Carro: FALHA - Pessoa dentro mas chave incorreta. Não pode acelerar.")
            return False
        
        if self.marcha == 0:
            self.log_de_ação("Acelerar", False, "Carro em Ponto Morto.")
            print("Carro: FALHA - Carro em Ponto Morto. Troque a marcha para acelerar.")
            return False

        if self.marcha in self.ACELERACAO_POR_MARCHA:
            self.log_de_ação("Acelerar", True, f"Velocidade aumentada em {self.ACELERACAO_POR_MARCHA[self.marcha]} km/h.")
            
            # Acelera conforme a marcha
            incremento = self.ACELERACAO_POR_MARCHA[self.marcha]
            self.velocidade += incremento
            print(f"Carro: SUCESSO - Acelerando (+{incremento}). Nova velocidade: {self.velocidade:.1f} km/h (Marcha {self.marcha}).")
            return True
        else:
            self.log_de_ação("Acelerar", True, "Velocidade aumentada em 1 km/h.")
            
            # Para marchas acima de 3, pode manter um incremento constante ou bloquear
            self.velocidade += 1
            print(f"Carro: SUCESSO - Acelerando (+1). Nova velocidade: {self.velocidade:.1f} km/h (Marcha {self.marcha}).")
            return True

    def frear(self, pessoa) -> bool:
        if self.velocidade == 0:
            self.log_de_ação("Frear", True, "Carro já parado.")
            print("Carro: Aviso - Carro já está parado.")
            return True

        # reduz a velocidade -5
        reducao = 5.0
        self.velocidade = max(0.0, self.velocidade - reducao)
        
        if self.velocidade == 0.0:
            self.log_de_ação("Frear", True, "Carro parou totalmente.")
            self.marcha = 0 # volta para ponto morto ao parar
            print("Carro: SUCESSO - Carro parou totalmente. Velocidade: 0.0 km/h. Ponto Morto.")
        else:
            self.log_de_ação("Frear", True, f"Velocidade reduzida em {reducao} km/h.")
            print(f"Carro: SUCESSO - Freando (-{reducao}). Nova velocidade: {self.velocidade:.1f} km/h (Marcha {self.marcha}).")
        return True

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int, altura: float, chave: Chave):
        self.nome = nome                  
        self.sobrenome = sobrenome        
        self._idade = idade               
        self._altura = altura             
        self.velocidade = 0.0             
        self.chave = chave                
        self.dentro_carro = False         

    def abrir_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando abrir o carro...")
        return carro.abrir(self.chave)

    def fechar_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando fechar o carro...")
        return carro.fechar(self.chave)

    def entrar_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando entrar no carro...")
        if carro.entrar_pessoa(self):
            self.dentro_carro = True
            return True
        return False

    def sair_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando sair do carro...")
        if carro.permitir_saida(self):
            self.dentro_carro = False
            return True
        return False
    
    def ligar_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando ligar o carro...")
        return carro.ligar(self)

    def desligar_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando desligar o carro...")
        return carro.desligar(self)

    def acelerar_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando acelerar o carro...")
        return carro.acelerar(self)

    def frear_carro(self, carro: Carro) -> bool:
        print(f"\n{self.nome}: Tentando frear o carro...")
        return carro.frear(self)
    
    def trocar_marcha_carro(self, carro: Carro, marcha: int) -> bool:
        print(f"\n{self.nome}: Tentando trocar marcha para {marcha}...")
        return carro.trocar_marcha(marcha)

def main():
    print("\n--- SIMULAÇÃO DE INTERAÇÃO ENTRE PESSOA, CARRO E CHAVE ---")
    
    # 1. Criação dos Objetos
    chave_mestra = Chave("ABC-123")
    carro_do_ze = Carro("ABC-123")
    ze = Pessoa("Zé", "Silva", 30, 1.75, chave_mestra)
    
    print(f"\nOBJETOS CRIADOS: Carro (Chave ID: {carro_do_ze.id_chave}), Pessoa: {ze.nome} (Chave ID: {ze.chave.get_id()}).")
    print("-" * 30)

    # 2. Abrir, Entrar, Fechar
    ze.abrir_carro(carro_do_ze)
    ze.entrar_carro(carro_do_ze)
    ze.fechar_carro(carro_do_ze)

    # 3. Ligar
    ze.ligar_carro(carro_do_ze)

    # 4. Trocar marchas e acelerar
    ze.trocar_marcha_carro(carro_do_ze, 1)
    ze.acelerar_carro(carro_do_ze)        
    
    ze.trocar_marcha_carro(carro_do_ze, 2)
    ze.acelerar_carro(carro_do_ze)        
    
    ze.trocar_marcha_carro(carro_do_ze, 3)
    ze.acelerar_carro(carro_do_ze)        
    
    # 5. Frear
    ze.frear_carro(carro_do_ze)  
    ze.frear_carro(carro_do_ze)  
    ze.frear_carro(carro_do_ze)
    
    # 6. Tentar sair com o carro ligado (Falha)
    print("--- TESTE DE ERRO: Tentar sair com o carro ligado ---")
    ze.ligar_carro(carro_do_ze)
    ze.abrir_carro(carro_do_ze)
    ze.sair_carro(carro_do_ze)
    
    # 7. Desligar e Sair (Sucesso)
    print("--- FLUXO CORRETO: Desligar e Sair ---")
    ze.desligar_carro(carro_do_ze)
    ze.sair_carro(carro_do_ze)
    
    # 8. Teste de Validação de Chave (Opcional)
    print("\n--- TESTE DE VALIDAÇÃO DE CHAVE ---")
    chave_errada = Chave("XYZ-999")
    maria = Pessoa("Maria", "Souza", 25, 1.65, chave_errada)
    maria.abrir_carro(carro_do_ze)

    print("\n--- SIMULAÇÃO FINALIZADA ---")

    # Exibir histórico de ações do carro
    carro_do_ze.exibir_historico()
    
if __name__ == "__main__":
    main()