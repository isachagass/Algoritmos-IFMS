def main():
    def gerar_nota(produtos):
        total = 0
        maior_custo = 0
        tupla_maior_custo = []
        for item in produtos:
            custo = item[1] * item[2]
            total += custo
            if custo > maior_custo:
                maior_custo = custo
                tupla_maior_custo = (item[0], custo)
        return total, tuple(tupla_maior_custo)


    produtos = (
        (101, 15, 29.90),
        (102, 8, 149.99),
        (103, 50, 4.50),
        (104, 3, 890.00),
        (105, 12, 12.00)
    )
    preco_final, produto_mais_caro = gerar_nota(produtos)
    print(f"Valor Total: R${preco_final:.2f}")
    print(f"\nProduto Mais Caro: \nCódigo:{produto_mais_caro[0]} \nCusto Final: R${produto_mais_caro[1]:.2f}")
main()