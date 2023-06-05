# Função para exibir o menu principal
def exibir_menu():
    print('')
    print('Bem-vindo à No Food Waste')
    print('')
    print('Selecione uma opção:')
    print('1. Cadastrar doador de alimentos')
    print('2. Cadastrar organização')
    print('3. Realizar doação de alimentos')
    print('4. Consultar doadores de alimentos')
    print('5. Consultar organizações cadastradas')
    print('6. Consultar alimentos doados')
    print('7. Sair')

# Função para cadastrar um doador de alimentos
def cadastrar_doador():
    print('')
    print('Você acessou a página de Cadastro de Doadores!')
    print('Por favor, preencha os campos abaixo:')
    nome = input('Digite o nome do doador: ')
    endereco = input('Digite o endereço do doador: ')
    telefone = input('Digite o telefone do doador: ')
    cpf = input('Digite o CPF do doador: ')
    email = input('Digite o e-mail do doador: ')
    doador = {
        'nome': nome,
        'endereco': endereco,
        'telefone': telefone,
        'cpf': cpf,
        'email': email,
    }
# Confirmação de cadastro
    print('')
    print('Por favor, confirme os dados do doador:')
    print(f"Nome: {doador['nome']}")
    print(f"Endereço: {doador['endereco']}")
    print(f"Telefone: {doador['telefone']}")
    print(f"CPF: {doador['cpf']}")
    print(f"E-mail: {doador['email']}")
    print('')
    confirmacao = input('Os dados estão corretos? (s/n): ')
    if confirmacao.lower() == 's':
        doadores.append(doador)
        print('Doador cadastrado com sucesso!')
    else:
        print('Cadastro cancelado.')


# Função para cadastrar uma organização
def cadastrar_organizacao():
    print('')
    print('Você acessou a página de Cadastro de Organizações!')
    print('Por favor, preencha os campos abaixo:')
    nome = input('Digite o nome da organização: ')
    endereco = input('Digite o endereço da organização: ')
    telefone = input('Digite o telefone da organização: ')
    cnpj = input('Digite a CNPJ da organização: ')
    email = input('Digite o email da organização: ')
    alimentos = input('Digite os alimentos principais que deseja receber: ')
    organizacao = {
        'nome': nome,
        'endereco': endereco,
        'telefone': telefone,
        'cnpj': cnpj,
        'email': email,
        'alimentos': alimentos
    }
# Confirmação de cadastro
    print('')
    print('Por favor, confirme os dados da organização:')
    print(f"Nome: {organizacao['nome']}")
    print(f"Endereço: {organizacao['endereco']}")
    print(f"Telefone: {organizacao['telefone']}")
    print(f"CNPJ: {organizacao['cnpj']}")
    print(f"E-mail: {organizacao['email']}")
    print(f"Alimentos: {organizacao['alimentos']}")
    print('')
    confirmacao = input('Os dados estão corretos? (s/n): ')
    if confirmacao.lower() == 's':
        organizacoes.append(organizacao)
        print('Organização cadastrada com sucesso!')
    else:
        print('Cadastro cancelado.')


# Função para realizar uma doação de alimentos
def realizar_doacao():
    print('')
    print('Você acessou a página de Doações!')
    print('Por favor, preencha os campos abaixo:')
    cpf_doador = input('Digite o CPF do doador: ')
    nome_organizacao = input('Digite o nome da organização para qual o alimento será doado: ')
    alimentos = input('Digite quais alimentos foram doados: ')
    quantidade = int(input('Digite a quantidade de alimentos doados: '))
    doacao = {
        'doador': cpf_doador,
        'organizacao': nome_organizacao,
        'alimentos': alimentos,
        'quantidade': quantidade
    }
# Confirmação de cadastro
    print('')
    print('Por favor, confirme os dados da doação:')
    print(f"CPF do doador: {doacao['doador']}")
    print(f"Organização: {doacao['organizacao']}")
    print(f"Alimentos: {doacao['alimentos']}")
    print(f"Quantidade: {doacao['quantidade']}")
    print('')
    confirmacao = input('Os dados estão corretos? (s/n): ')
    if confirmacao.lower() == 's':
        doacoes.append(doacao)
        print('Doação realizada com sucesso!')
    else:
        print('Doação cancelada.')

# Função para exibir as organizações cadastradas
def consultar_organizacoes():
    print('')
    print('Você acessou a página "Organizações Cadastradas"!')
    print('Abaixo, todas as organizações cadastradas até o momento:')
    for organizacao in organizacoes:
        print(f"Nome: {organizacao['nome']}")
        print(f"Endereço: {organizacao['endereco']}")
        print(f"Telefone: {organizacao['telefone']}")
        print(f"CNPJ: {organizacao['cnpj']}")
        print(f"E-mail: {organizacao['email']}")
        print(f"Alimentos: {organizacao['alimentos']}")

# Função para exibir os doadores de alimentos cadastrados
def consultar_doadores():
    print('')
    print('Você acessou a página "Doadores Cadastrados"!')
    print('Abaixo, todos os doadores cadastrados até o momento:')
    for doador in doadores:
        print(f"Nome: {doador['nome']}")
        print(f"Endereço: {doador['endereco']}")
        print(f"Telefone: {doador['telefone']}")
        print(f"CPF: {doador['cpf']}")
        print(f"E-mail: {doador['email']}")

# Função para exibir os alimentos doados cadastrados
def consultar_doacoes():
    print('')
    print('Você acessou a página "Alimentos Doados"!')
    print('Abaixo, todos os alimentos doados até o momento:')
    for doacao in doacoes:
        print(f"Alimentos: {doacao['alimentos']}")
        print(f"Quantidade: {doacao['quantidade']}")

# Listas para armazenar os doadores, organizações e doações de alimentos
doadores = []
organizacoes = []
doacoes = []

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input('Digite sua opção: ')
    
    if opcao == '1':
        cadastrar_doador()
    elif opcao == '2':
        cadastrar_organizacao()
    elif opcao == '3':
        realizar_doacao()
    elif opcao == '4':
        consultar_doadores()
    elif opcao == '5':
        consultar_organizacoes()
    elif opcao == '6':
        consultar_doacoes()
    elif opcao == '7':
        print('')
        print('Obrigado por utilizar a plataforma. Até logo!')
        break
    else:
        print('Opção inválida.')
    
    print('')
    input('Pressione "Enter" para voltar ao menu.')