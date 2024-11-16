from tabulate import tabulate

def finite_difference_table(x_points, y_points):
    """
    Calcula e imprime a tabela de diferenças finitas no formato de tabela.

    Parâmetros:
    - x_points: lista de pontos x conhecidos.
    - y_points: lista de valores f(x) correspondentes aos pontos x conhecidos.

    Retorna:
    - tabela: tabela de diferenças finitas.
    """
    n = len(y_points)
    # Inicializa a tabela de diferenças finitas
    tabela = [y_points[:]]
    for i in range(1, n):
        col = []
        for j in range(n - i):
            # Calcula a diferença finita
            diff = tabela[i - 1][j + 1] - tabela[i - 1][j]
            col.append(diff)
        tabela.append(col)

    # Formatando a tabela para exibição
    formatted_table = []
    for i in range(n):
        row = [x_points[i] if i < len(x_points) else None]
        for col in tabela:
            row.append(col[i] if i < len(col) else "")
        formatted_table.append(row)

    headers = ["x"] + [f"Nível {i}" for i in range(n)]
    print(tabulate(formatted_table, headers=headers, tablefmt="grid"))

    return tabela

# Exemplo de uso
if __name__ == "__main__":
    # Pontos conhecidos
    x_points = [1, 2, 3, 4]
    y_points = [1, 4, 9, 16]

    # Calcula a tabela de diferenças finitas e imprime
    finite_difference_table(x_points, y_points)

