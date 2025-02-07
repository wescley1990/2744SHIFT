from service.autor_service import AutorService

menu_principal = """[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""


menu_categorias = """
[Categorias] Escolha uma das seguintes opções:
1 - Listar toda as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
0 - Voltar ao menu anterior
"""

menu_editoras = """
[Editoras] Escolha uma das seguintes opções:
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior
"""

menu_livros = """
[Livros] Escolha uma das seguintes opções:
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
0 - Voltar ao menu anterior
"""

autor_service = AutorService()

tabela_categorias = []
tabela_editoras = []
tabela_livros = []






def gerencia_categoria():
    print(menu_categorias)
    opcao_categorias = input('Digite a opção: ')
    match opcao_categorias:
        case '0':
            return  # encerra a execução desta função e retorna para onde foi chamada.
        case '1':
            if tabela_categorias == []:
                print("Nenhuma Categoria cadastrada.")
                input("Pressione <ENTER> para continuar.")
            else:
                print('Id | Nome')
                for index, categoria in enumerate(tabela_categorias):
                    print(f"{index} | {categoria['nome']}")
        case '2':
            nome_categoria = input('Digite o nome da categoria: ')
            nova_categoria = {
                'nome': nome_categoria
            }
            tabela_categorias.append(nova_categoria)
        case '3':
            if tabela_categorias == []:
                print("Nenhuma Categoria cadastrada.")
                input("Pressione <ENTER> para continuar.")
            else:
                try:
                    id = input('Digite o ID da categoria a ser excluída: ')
                    id = int(id)
                    tabela_categorias.pop(id)
                except:
                    print(f'Id da categoria "{id}" inválido.')

                print('Categoria excluída com sucesso!')
        case '4':
            if tabela_categorias == []:
                print("Nenhuma Categoria cadastrada.")
                input("Pressione <ENTER> para continuar.")
            else:
                try:
                    id = input('Digite o ID da categoria para buscar: ')
                    id = int(id)
                    categoria = tabela_categorias[id]
                    print('Id | Nome')
                    print(f"{id} | {categoria['nome']}")
                except:
                    print(f'Id da categoria "{id}" inválido.')

        case _:
            print('Opção inválida!')

    gerencia_categoria()



def gerencia_editora():
    print(menu_editoras)
    opcao_editoras = input('Digite a opção: ')
    match opcao_editoras:
        case '0':
            return  # encerra a execução desta função e retorna para onde foi chamada.
        case '1':
            if tabela_editoras == []:
                print("Nenhuma Editora cadastrada.")
                input("Pressione <ENTER> para continuar.")
            else:
                print('Id | Nome | Endereço | Telefone')
                for index, editora in enumerate(tabela_editoras):
                    print(f"{index} | {editora['nome']} | {editora['endereco']} | {editora['fone']}")
        case '2':
            nome_editora = input('Digite o nome da editora: ')
            endereco_editora = input('Digite o endereço da editora: ')
            fone_editora = input('Digite o telefone da editora: ')
            nova_editora = {}
            nova_editora['nome'] = nome_editora
            nova_editora['endereco'] = endereco_editora
            nova_editora['fone'] = fone_editora
            tabela_editoras.append(nova_editora)
            print('Editora adicionada com sucesso!')
        case '3':
            if tabela_editoras == []:
                print("Nenhuma Editora cadastrada.")
                input("Pressione <ENTER> para continuar.")
            else:
                try:
                    id = input('Digite o ID da editora a ser excluída: ')
                    id = int(id)
                    tabela_editoras.pop(id)
                except:
                    print(f'Id da editora "{id}" inválido.')

                print('Editora excluída com sucesso!')
        case '4':
            if tabela_editoras == []:
                print("Nenhuma Editora cadastrada.")
                input("Pressione <ENTER> para continuar.")
            else:
                try:
                    id = input('Digite o ID da editora para buscar: ')
                    id = int(id)
                    editora = tabela_editoras[id]
                    print('Id | Nome | Endereço | Telefone')
                    print(f"{id} | {editora['nome']} | {editora['endereco']} | {editora['fone']}")

                except:
                    print(f'Id da editora "{id}" inválido.')

        case _:  # opção default
            print('Opção inválida!')

    gerencia_editora()





def gerencia_livro():
    print(menu_livros)
    opcao_livros = input('Digite a opção: ')
    match opcao_livros:
        case '0':
            return  # encerra a execução desta função e retorna para onde foi chamada.
        case '1':
            if tabela_livros == []:
                print('Nenhum livro cadastrado.')
                input('Pressione <ENTER> para continuar.')
            else:
                print('Id | Título | Ano | Qtde páginas | ISBN | autor | categoria | editora')
                for index, livro in enumerate(tabela_livros):
                    print(f"{index} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
        case '2':
            if AutorService.tabela_autores == [] or tabela_categorias == [] or tabela_editoras == []:
                print('Necessário cadastrar pelo menos um autor, uma categoria, e uma editora.')
            else:
                titulo = input('Digite o título do livro: ')
                resumo = input('Digite o resumo do livro: ')
                ano = input('Digite o ano de publicação: ')
                paginas = input('Digite a quantidade de páginas: ')
                isbn = input('Digite o ISBN: ')

                print('Id | Nome | Email')
                for index, autor in enumerate(AutorService.tabela_autores):
                    print(f'{index} | {autor['nome']} | {autor['email']}')

                autor_id = int(input('Digite o Id do autor: '))

                print('Id | Nome')
                for index, categoria in enumerate(tabela_categorias):
                    print(f"{index} | {categoria['nome']}")

                categoria_id = int(input('Digite o Id da categoria: '))

                print('Id | Nome')
                for index, editora in enumerate(tabela_editoras):
                    print(f"{index} | {editora['nome']}")

                editora_id = int(input('Digite o Id da editora: '))
                novo_livro = {
                    'titulo': titulo,
                    'resumo': resumo,
                    'ano': ano,
                    'paginas': paginas,
                    'isbn': isbn,
                    'autor': AutorService.tabela_autores[autor_id],
                    'categoria': tabela_categorias[categoria_id],
                    'editora': tabela_editoras[editora_id]
                }
                tabela_livros.append(novo_livro)
                print('Livro adicionado com sucesso!')
        case '3':
            if tabela_livros == []:
                print('Nenhum livro cadastrado.')
                input('Pressione <ENTER> para continuar.')
            else:
                try:
                    id = input('Digite o ID do livro a ser excluido: ')
                    id = int(id)
                    tabela_livros.pop(id)
                except:
                    print(f'Id do livro "{id}" inválido.')

                print('Livro excluído com sucesso!')
        case '4':
            if tabela_livros == []:
                print('Nenhum livro cadastrado.')
                input('Pressione <ENTER> para continuar.')
            else:
                try:
                    id = input('Digite o ID do livro a ser excluido: ')
                    id = int(id)
                    livro = tabela_livros[id]
                    print('Id | Título | Ano | Qtde páginas | ISBN | autor | categoria | editora')
                    print(f"{index} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
                except:
                    print(f'Id do livro "{id}" inválido.')

        case _:
            print('Opção Inválida!')

    gerencia_livro()


def display_menu_principal():
    while True:
        print(menu_principal)

        print()  # Uma linha vazia.

        opcao_principal = input('Digite a opção: ')
        match opcao_principal:
            case '0':
                return  # encerra a execução desta função e retorna para onde foi chamada.
            case '1':
                gerencia_categoria()
            case '2':
                gerencia_editora()
            case '3':
                autor_service.menu()
            case '4':
                gerencia_livro()
            case _:
                print('Opção Inválida!')


display_menu_principal()
print('Programa Encerrado!')