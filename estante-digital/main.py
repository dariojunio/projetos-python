from livro import Livro
from biblioteca import Biblioteca

minha_estante = Biblioteca()

l1 = Livro('O Principe', 'Maquiavel', 130)
l2 = Livro('A Arte da Guerra', 'Sun Tzu', 160)

minha_estante.adicionar_livro(l1)
minha_estante.adicionar_livro(l2)

while True:
    print("\n=== MENU BIBLIOTECA ===")
    print("1. Listar Livros")
    print("2. Emprestar Livro")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        minha_estante.listar_livros()
    elif opcao == '2':
        busca = input("Nome do livro: ")
        minha_estante.emprestar_livro(busca)
    elif opcao == '3':
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida!")
