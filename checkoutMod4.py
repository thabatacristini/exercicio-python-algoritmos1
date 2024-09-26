def leProdutos():
    listaProdutos = []

    while True:
        produto = input(
            "Cadastre um produto (ou digite 'consultar' para buscar o preço de algum produto): ").lower()

        if produto == 'consultar':
            break

        valor = float(input("Qual o valor desse produto? (Ex.: 5.25)"))

        if any(produto == item[0].lower() for item in listaProdutos):
            print("Produto já cadastrado.")
        else:
            listaProdutos.append((produto, valor))

        print("\nProdutos cadastrados até o momento:")
        for item in listaProdutos:
            print(f"- {item[0].capitalize()}: R$ {item[1]}")

    return listaProdutos


def buscaPreco(listaProdutos):
    while True:
        produto = input(
            "Digite o nome do produto para consultar o preço (ou 'fim' para encerrar): ")

        if produto.lower() == 'fim':
            break

        for item in listaProdutos:
            if item[0].lower() == produto.lower():
                print(f"O preço de {produto} é: {item[1]}")
                break
        else:
            print("Produto não cadastrado.")
            desejaCadastrar = input(
                "Deseja cadastrar o produto? (sim/não): ").strip().lower()
            if desejaCadastrar == 'sim':
                listaProdutos = leProdutos()
            elif desejaCadastrar == 'não':
                print("Encerrando o programa.")
                break


produtos = leProdutos()

buscaPreco(produtos)
