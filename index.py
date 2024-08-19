import json 
import re 

class Contato:
    def __init__(self, nome, telefone, email): 
        """
        Inicializa um objeto Contato com nome, telefone e email.

        :param nome: Nome do contato.
        :param telefone: Telefone do contato.
        :param email: Email do contato.
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email

    @staticmethod
    def validar_email(email: str) -> bool:
        """
        Valida se o email está no formato correto.

        :param email: Email a ser validado.
        :return: True se o email for válido, False caso contrário.
        """
        padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None

    @staticmethod
    def validar_telefone(telefone: str) -> bool:
        """
        Valida se o telefone está no formato correto.

        :param telefone: Telefone a ser validado.
        :return: True se o telefone for válido, False caso contrário.
        """
        padrao = r'^\+?\d[\d\s-]{7,15}$'
        return re.match(padrao, telefone) is not None

    def editar(self, telefone: str, email: str):
        """
        Edita o telefone e o email do contato.

        :param telefone: Novo telefone do contato.
        :param email: Novo email do contato.
        """
        self.telefone = telefone
        self.email = email

def carregar_contatos(arquivo: str) -> dict:
    """
    Carrega contatos de um arquivo JSON.

    :param arquivo: Caminho para o arquivo JSON.
    :return: Dicionário contendo os contatos carregados do arquivo.
    """
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def salvar_contatos(arquivo: str, contatos: dict):
    """
    Salva contatos em um arquivo JSON.

    :param arquivo: Caminho para o arquivo JSON.
    :param contatos: Dicionário contendo os contatos a serem salvos.
    """
    with open(arquivo, 'w') as file:
        json.dump(contatos, file, indent=4)

def adicionar_contato(contatos: dict):
    """
    Adiciona um novo contato ao dicionário de contatos.

    Solicita ao usuário o nome, telefone e email do novo contato e valida
    as informações antes de adicioná-las ao dicionário.

    :param contatos: Dicionário de contatos onde o novo contato será adicionado.
    """
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    if not Contato.validar_telefone(telefone):
        print("Telefone inválido! Tente novamente.")
        return

    if not Contato.validar_email(email):
        print("Email inválido! Tente novamente.")
        return

    contatos[nome] = {'telefone': telefone, 'email': email}
    print("Contato adicionado com sucesso!")

def editar_contato(contatos: dict):
    """
    Edita um contato existente no dicionário de contatos.

    Solicita ao usuário o nome do contato a ser editado, o novo nome (se desejado),
    o novo telefone e o novo email. Se o contato for encontrado, as informações
    serão atualizadas.

    :param contatos: Dicionário de contatos onde o contato será editado.
    """
    nome = input("Nome do contato a editar: ")
    if nome in contatos:
        novo_nome = input("Novo Nome (deixe em branco para manter o atual): ")
        telefone = input("Novo Telefone: ")
        email = input("Novo Email: ")

        if not Contato.validar_telefone(telefone):
            print("Telefone inválido! Tente novamente.")
            return

        if not Contato.validar_email(email):
            print("Email inválido! Tente novamente.")
            return

        if novo_nome:
            contatos[novo_nome] = contatos.pop(nome)
            nome = novo_nome

        contatos[nome]['telefone'] = telefone
        contatos[nome]['email'] = email
        print("Contato editado com sucesso!")
    else:
        print("Contato não encontrado!")

def excluir_contato(contatos: dict):
    """
    Exclui um contato existente do dicionário de contatos.

    Solicita ao usuário o nome do contato a ser excluído. Se o contato for encontrado,
    ele será removido do dicionário.

    :param contatos: Dicionário de contatos onde o contato será excluído.
    """
    nome = input("Nome do contato a excluir: ")
    if nome in contatos:
        del contatos[nome]
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado!")

def listar_contatos(contatos: dict):
    """
    Lista todos os contatos presentes no dicionário.

    :param contatos: Dicionário de contatos a ser listado.
    """
    if contatos:
        for nome, dados in contatos.items():
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}")
    else:
        print("Nenhum contato disponível.")

def menu():
    """
    Exibe o menu principal do gerenciador de contatos.
    """
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Excluir Contato")
    print("4. Listar Contatos")
    print("5. Sair")

def main():
    """
    Função principal que executa o gerenciador de contatos.
    """
    arquivo = 'contatos.json'
    contatos = carregar_contatos(arquivo)
    
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_contato(contatos)
        elif escolha == '2':
            editar_contato(contatos)
        elif escolha == '3':
            excluir_contato(contatos)
        elif escolha == '4':
            listar_contatos(contatos)
        elif escolha == '5':
            salvar_contatos(arquivo, contatos)
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
