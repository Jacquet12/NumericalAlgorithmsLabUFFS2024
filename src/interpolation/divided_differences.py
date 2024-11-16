from tabulate import tabulate
def divided_differences(x_points, y_points):
    """
    Calcula a tabela de diferenças divididas de Newton.

    Parâmetros:
    - x_points: lista de pontos x conhecidos.
    - y_points: lista de valores f(x) correspondentes aos pontos x conhecidos.

    Retorna:
    - tabela: tabela de diferenças divididas.
    """
    n = len(x_points)
    # Inicializa a tabela com os valores de y
    tabela = [[0] * n for _ in range(n)]
    for i in range(n):
        tabela[i][0] = y_points[i]

    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i + 1][j - 1] - tabela[i][j - 1]) / (x_points[i + j] - x_points[i])

    return tabela

def print_divided_differences_table(x_points, tabela):
    """
    Imprime a tabela de diferenças divididas de forma formatada.

    Parâmetros:
    - x_points: lista de pontos x conhecidos.
    - tabela: tabela de diferenças divididas.
    """
    headers = ["x"] + [f"Nível {i}" for i in range(len(x_points))]
    formatted_table = []

    for i in range(len(x_points)):
        row = [x_points[i]] + tabela[i][:len(x_points) - i]
        formatted_table.append(row)

    print(tabulate(formatted_table, headers=headers, tablefmt="grid"))

# Exemplo de uso
if __name__ == "__main__":
    # Pontos conhecidos
    x_points = [1, 2, 3, 4]
    y_points = [1, 4, 9, 16]

    # Calcula a tabela de diferenças divididas
    tabela_diferencas_divididas = divided_differences(x_points, y_points)

    # Imprime a tabela formatada
    print_divided_differences_table(x_points, tabela_diferencas_divididas)

