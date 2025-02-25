"""
SISTEMA BANCÁRIO COM MÚLTIPLAS FUNÇÕES

Este script simula um sistema bancário básico com operações de saque, depósito, extrato,
cadastro de usuários e cadastro de contas bancárias.

ESTRUTURA DE DADOS:
- Armazenamos usuários como dicionários
- Contas bancárias também são dicionários associados aos usuários
- Utilizamos listas para armazenar múltiplos usuários e contas
"""

# Estas são variáveis globais que armazenam os dados do sistema bancário
# Uma variável é um espaço na memória que guarda informações
usuarios = []          # Lista vazia para armazenar todos os usuários cadastrados 
contas = []            # Lista vazia para armazenar todas as contas bancárias
AGENCIA = "0001"       # Número da agência bancária (constante)

# Funções do sistema - Uma função é um bloco de código que realiza uma tarefa específica


def menu():
    """
    Exibe o menu principal do sistema bancário.
    
    Exemplo da vida real: Como um cardápio de restaurante que mostra todas as opções disponíveis.
    """
    menu_text = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair
    => """
    return input(menu_text)


def depositar(saldo, valor, extrato, /):
    """
    Realiza um depósito na conta.
    
    Argumentos:
    saldo (float): Saldo atual da conta
    valor (float): Valor a ser depositado
    extrato (str): Histórico de transações
    
    Retornos:
    tuple: Novo saldo e extrato atualizado
    
    Exemplo da vida real: Como colocar dinheiro em um cofre. Você só pode adicionar valores positivos,
    não pode "depositar" -R$50,00 (isso seria um saque).
    
    Obs: O símbolo '/' nos parâmetros indica que estes são parâmetros posicionais obrigatórios.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque da conta.
    
    Argumentos:
    saldo (float): Saldo atual da conta
    valor (float): Valor a ser sacado
    extrato (str): Histórico de transações
    limite (float): Limite máximo de saque
    numero_saques (int): Número de saques realizados
    limite_saques (int): Limite de saques permitidos
    
    Retornos:
    tuple: Saldo, extrato e número de saques atualizados
    
    Exemplo da vida real: Como retirar dinheiro de um caixa eletrônico, que possui:
    - Limite por operação (ex: máximo de R$500,00 por saque)
    - Limite diário de saques (ex: máximo de 3 saques por dia)
    - Verificação se há saldo suficiente
    
    Obs: O símbolo '*' nos parâmetros indica que todos são parâmetros nomeados obrigatórios.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        
    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        
    elif excedeu_saques:
        print(f"Operação falhou! Número máximo de {limite_saques} saques excedido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    
    Argumentos:
    saldo (float): Saldo atual da conta (parâmetro posicional)
    extrato (str): Histórico de transações (parâmetro nomeado)
    
    Exemplo da vida real: Como verificar o histórico de transações no aplicativo do banco,
    mostrando todos os depósitos, saques e o saldo atual.
    
    Obs: O símbolo '/' indica que o 'saldo' é um parâmetro posicional, e o '*' indica
    que o 'extrato' é um parâmetro nomeado.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """
    Cadastra um novo usuário no sistema.
    
    Argumentos:
    usuarios (list): Lista de usuários existentes
    
    Retornos:
    list: Lista atualizada de usuários
    
    Exemplo da vida real: Como preencher um formulário para abrir uma conta em um banco,
    fornecendo CPF, nome completo e endereço.
    """
    cpf = input("Informe o CPF (somente números): ")
    
    # Verifica se o usuário já existe
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuário com esse CPF já existe!")
        return usuarios
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    # Cria um dicionário com as informações do usuário
    # Um dicionário é uma estrutura que armazena dados em pares de chave e valor
    novo_usuario = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    
    usuarios.append(novo_usuario)  # Adiciona o novo usuário à lista
    print("Usuário criado com sucesso!")
    
    return usuarios


def filtrar_usuario(cpf, usuarios):
    """
    Filtra um usuário pelo CPF.
    
    Argumentos:
    cpf (str): CPF do usuário
    usuarios (list): Lista de usuários
    
    Retornos:
    dict ou None: Usuário encontrado ou None
    
    Exemplo da vida real: Como um atendente do banco procura seus dados no sistema
    usando seu CPF como identificação única.
    """
    # A função next com um gerador (expressão geradora) busca o primeiro elemento que atende à condição
    # Se não encontrar, retorna o valor padrão (None neste caso)
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma nova conta bancária vinculada a um usuário.
    
    Argumentos:
    agencia (str): Número da agência
    numero_conta (int): Número da conta
    usuarios (list): Lista de usuários
    
    Retornos:
    dict: Nova conta criada
    
    Exemplo da vida real: Como quando o banco, após verificar seus documentos,
    cria uma conta com número único vinculada ao seu CPF.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        # Cria um dicionário com as informações da conta
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    
    print("\nUsuário não encontrado! Operação cancelada.")
    return None


def listar_contas(contas):
    """
    Lista todas as contas cadastradas.
    
    Argumentos:
    contas (list): Lista de contas
    
    Exemplo da vida real: Como um gerente de banco visualiza todas as contas
    sob sua administração.
    """
    # Se não houver contas, exibe uma mensagem
    if not contas:
        print("\nNão há contas cadastradas!")
        return
    
    # Itera sobre cada conta na lista e exibe suas informações
    # O loop for percorre cada elemento de uma coleção, um por vez
    print("\n================ CONTAS CADASTRADAS ================")
    for conta in contas:
        # Acessa os dados do usuário vinculado à conta
        usuario = conta["usuario"]
        
        # Formata e exibe as informações
        # O caractere \t é uma tabulação, usado para alinhar o texto
        print(f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
        """)
    print("====================================================")


def main():
    """
    Função principal que executa o programa.
    
    Exemplo da vida real: Como o sistema operacional de um caixa eletrônico
    que gerencia todas as operações possíveis.
    """
    # Inicialização de variáveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    numero_conta = 1  # Contador para gerar números de conta sequenciais
    
    # Loop principal do programa
    # Um loop while executa repetidamente enquanto uma condição for verdadeira
    while True:
        opcao = menu()  # Exibe o menu e captura a opção do usuário
        
        # Estruturas condicionais (if/elif/else) para tratar cada opção
        # Elas permitem que o programa tome decisões baseadas em condições
        
        if opcao == "d":
            # Operação de depósito
            print("\n================ DEPÓSITO ================")
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            # Operação de saque
            print("\n================ SAQUE ================")
            valor = float(input("Informe o valor do saque: R$ "))
            
            # O operador ** desempacota o dicionário de argumentos nomeados
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            # Exibição do extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            # Cadastro de novo usuário
            print("\n================ NOVO USUÁRIO ================")
            usuarios = criar_usuario(usuarios)

        elif opcao == "nc":
            # Criação de nova conta
            print("\n================ NOVA CONTA ================")
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            # Listagem de contas
            listar_contas(contas)

        elif opcao == "q":
            # Sair do programa
            print("\nObrigado por usar nosso sistema bancário!")
            break

        else:
            # Opção inválida
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


# Ponto de entrada do programa
# Este bloco verifica se o script está sendo executado diretamente (não importado)
if __name__ == "__main__":
    """
    Essa estrutura é um padrão em Python que verifica se este arquivo está sendo executado diretamente.
    Se for, chama a função principal.
    
    Exemplo da vida real: Como ligar a chave geral antes de usar qualquer equipamento.
    """
    # Exibe uma mensagem de boas-vindas
    print("=" * 50)
    print("Bem-vindo ao Sistema Bancário".center(50))
    print("=" * 50)
    
    # Inicia o programa chamando a função principal
    main()