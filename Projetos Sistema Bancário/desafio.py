
import textwrap


def menu():
    """
    Função que exibe o menu de opções para o usuário e retorna a opção escolhida.
    
    A função textwrap.dedent() remove o recuo (espaços no início das linhas) de uma string,
    tornando o texto mais legível no código e mantendo a formatação adequada na saída.
    
    Exemplo na vida real: Como um menu de caixa eletrônico que mostra todas as operações 
    disponíveis para o cliente do banco.
    
    Retorna:
        str: A opção escolhida pelo usuário.
    """
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    # O input() exibe uma mensagem e espera que o usuário digite algo
    # textwrap.dedent() remove a indentação excessiva para melhorar a apresentação
    return input(textwrap.dedent(menu_text))


def depositar(saldo, valor, extrato, /):
    """
    Função que realiza um depósito na conta.
    
    A barra (/) nos parâmetros indica que todos os argumentos anteriores a ela
    devem ser posicionais (não podem ser passados como argumentos nomeados).
    
    Parâmetros posicionais obrigatórios:
        saldo (float): O saldo atual da conta.
        valor (float): O valor a ser depositado.
        extrato (str): O extrato atual da conta.
    
    Exemplo na vida real: Como depositar dinheiro em um caixa eletrônico,
    onde o valor é adicionado ao saldo da conta e registrado no extrato.
    
    Retorna:
        tuple: Uma tupla contendo o novo saldo e o extrato atualizado.
    """
    # Verificamos se o valor é válido (maior que zero)
    if valor > 0:
        # Adiciona o valor ao saldo
        saldo += valor
        # Atualiza o extrato com a informação do depósito
        # A formatação :.2f garante que o valor tenha sempre 2 casas decimais
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        # Informa ao usuário que o valor é inválido
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o saldo e extrato atualizados
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função que realiza um saque na conta.
    
    O asterisco (*) nos parâmetros indica que todos os argumentos após ele
    devem ser nomeados (keyword arguments).
    
    Parâmetros nomeados obrigatórios:
        saldo (float): O saldo atual da conta.
        valor (float): O valor a ser sacado.
        extrato (str): O extrato atual da conta.
        limite (float): O limite de valor por saque.
        numero_saques (int): O número de saques já realizados.
        limite_saques (int): O limite de saques permitidos.
    
    Exemplo na vida real: Como sacar dinheiro em um caixa eletrônico,
    onde existem limitações como saldo disponível, limite por operação e
    número máximo de saques diários.
    
    Retorna:
        tuple: Uma tupla contendo o novo saldo e o extrato atualizado.
    """
    # Verifica se o valor do saque excede o saldo disponível
    excedeu_saldo = valor > saldo
    # Verifica se o valor do saque excede o limite por operação
    excedeu_limite = valor > limite
    # Verifica se o número de saques já atingiu o limite
    excedeu_saques = numero_saques >= limite_saques

    # Verifica as condições para realizar o saque
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        # Se todas as condições forem satisfeitas, realiza o saque
        saldo -= valor
        # Atualiza o extrato com a informação do saque
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        # Incrementa o contador de saques
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        # Informa ao usuário que o valor é inválido
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o saldo e extrato atualizados
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    """
    Função que exibe o extrato da conta.
    
    Combina parâmetros posicionais e nomeados:
    - A barra (/) indica que 'saldo' deve ser um parâmetro posicional.
    - O asterisco (*) indica que 'extrato' deve ser um parâmetro nomeado.
    
    Parâmetros:
        saldo (float): O saldo atual da conta.
        extrato (str): O histórico de transações da conta.
    
    Exemplo na vida real: Como verificar o extrato bancário em um aplicativo
    de banco, onde você vê todas as transações recentes e o saldo atual.
    """
    print("\n================ EXTRATO ================")
    # Exibe "Não foram realizadas movimentações" se o extrato estiver vazio,
    # caso contrário, exibe o conteúdo do extrato
    print("Não foram realizadas movimentações." if not extrato else extrato)
    # Exibe o saldo atual formatado com duas casas decimais
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """
    Função que cria um novo usuário no sistema.
    
    Parâmetros:
        usuarios (list): A lista de usuários existentes.
    
    Exemplo na vida real: Como criar uma conta em um banco,
    onde você precisa fornecer seus dados pessoais para cadastro.
    """
    # Coleta as informações do usuário
    cpf = input("Informe o CPF (somente número): ")
    
    # Verifica se já existe um usuário com o CPF informado
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    # Coleta os demais dados do usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Cria um dicionário com os dados do usuário e adiciona à lista de usuários
    # Um dicionário é uma estrutura de dados que armazena pares de chave-valor
    usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    """
    Função que busca um usuário pelo CPF.
    
    Parâmetros:
        cpf (str): O CPF do usuário a ser buscado.
        usuarios (list): A lista de usuários existentes.
    
    Exemplo na vida real: Como um sistema de busca em um banco de dados
    de clientes, onde o CPF é usado como identificador único.
    
    Retorna:
        dict: O usuário encontrado ou None se não encontrar.
    """
    # List comprehension: cria uma nova lista com os usuários que possuem o CPF informado
    # É uma forma concisa de escrever um loop for com uma condição
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    # Retorna o primeiro usuário encontrado ou None se a lista estiver vazia
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    """
    Função que cria uma nova conta bancária para um usuário existente.
    
    Parâmetros:
        agencia (str): O número da agência.
        numero_conta (int): O número da conta.
        usuarios (list): A lista de usuários existentes.
    
    Exemplo na vida real: Como abrir uma conta em um banco após já ter
    feito o cadastro como cliente.
    
    Retorna:
        dict: Um dicionário com os dados da conta criada ou None se não for criada.
    """
    # Solicita o CPF do usuário para associar à conta
    cpf = input("Informe o CPF do usuário: ")
    # Busca o usuário pelo CPF
    usuario = filtrar_usuario(cpf, usuarios)

    # Se o usuário for encontrado, cria a conta
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        # Retorna um dicionário com os dados da conta
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    # Se o usuário não for encontrado, informa e não cria a conta
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None


def listar_contas(contas):
    """
    Função que lista todas as contas cadastradas.
    
    Parâmetros:
        contas (list): A lista de contas existentes.
    
    Exemplo na vida real: Como um gerente de banco visualiza
    todas as contas dos clientes no sistema.
    """
    # Para cada conta na lista de contas
    for conta in contas:
        # Formata as informações da conta
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        # Imprime uma linha separadora
        print("=" * 100)
        # Imprime as informações da conta, removendo a indentação excessiva
        print(textwrap.dedent(linha))


def main():
    """
    Função principal que controla o fluxo do programa.
    
    Esta função é o ponto de entrada do programa e gerencia todas as operações
    do sistema bancário, mantendo o estado do programa e chamando as funções
    apropriadas com base na escolha do usuário.
    
    Exemplo na vida real: Como o sistema central de um banco que coordena
    todas as operações e mantém todos os dados atualizados.
    """
    # Constantes (valores que não mudam durante a execução do programa)
    LIMITE_SAQUES = 3  # Limite máximo de saques permitidos
    AGENCIA = "0001"   # Número da agência

    # Variáveis para armazenar o estado do programa
    saldo = 0          # Saldo inicial da conta
    limite = 500       # Limite de valor por saque
    extrato = ""       # String para armazenar o histórico de transações
    numero_saques = 0  # Contador de saques realizados
    usuarios = []      # Lista para armazenar os usuários cadastrados
    contas = []        # Lista para armazenar as contas criadas

    # Loop principal do programa
    # O loop continuará até que o usuário escolha sair (opção 'q')
    while True:
        # Exibe o menu e obtém a escolha do usuário
        opcao = menu()

        # Processa a opção escolhida
        if opcao == "d":
            # Operação de depósito
            valor = float(input("Informe o valor do depósito: "))
            # Chama a função depositar e atualiza o saldo e extrato
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            # Operação de saque
            valor = float(input("Informe o valor do saque: "))
            # Chama a função sacar com todos os parâmetros necessários
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            # Operação de exibir extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            # Operação de criar usuário
            criar_usuario(usuarios)

        elif opcao == "nc":
            # Operação de criar conta
            # Gera um número de conta sequencial
            numero_conta = len(contas) + 1
            # Chama a função criar_conta
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            # Se a conta foi criada com sucesso, adiciona à lista de contas
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            # Operação de listar contas
            listar_contas(contas)

        elif opcao == "q":
            # Operação de sair do programa
            break

        else:
            # Opção inválida
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Este comando inicia a execução do programa chamando a função principal
# Quando o Python executa um script, ele define a variável __name__ como "__main__"
# Isso permite que o script seja importado por outros scripts sem executar a função main()
if __name__ == "__main__":
    main()


"""
EXEMPLOS ADICIONAIS DE USO NA VIDA REAL:

1. Sistema Bancário:
   - Este script simula um sistema bancário simples, similar aos sistemas usados
     em bancos reais para gerenciar contas e transações.

2. Controle Financeiro Pessoal:
   - Você pode adaptar este código para criar um aplicativo de controle financeiro
     pessoal, onde pode registrar receitas (depósitos) e despesas (saques).

3. Sistema de Estoque:
   - Os conceitos de adicionar (depositar) e remover (sacar) podem ser adaptados
     para um sistema de controle de estoque de uma loja.

4. Sistema de Pontos de Fidelidade:
   - As funções de depósito e saque podem ser adaptadas para adicionar ou
     resgatar pontos em um programa de fidelidade.

5. Biblioteca Digital:
   - A estrutura de usuários e "contas" pode ser adaptada para um sistema
     de biblioteca, onde os usuários podem emprestar (sacar) e devolver (depositar) livros.
"""