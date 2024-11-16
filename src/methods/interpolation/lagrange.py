def lagrange_interpolation(x_points, y_points, x):
    """
    Método de Interpolação de Lagrange.

    Parâmetros:
    - x_points: lista de pontos x conhecidos.
    - y_points: lista de valores f(x) correspondentes aos pontos x conhecidos.
    - x: ponto onde deseja-se estimar o valor interpolado.

    Retorna:
    - Valor estimado de f(x) no ponto fornecido.
    """
    n = len(x_points)
    if n != len(y_points):
        raise ValueError("Os vetores x_points e y_points devem ter o mesmo tamanho.")

    # Calcula o valor interpolado
    interpolated_value = 0
    for i in range(n):
        # Calcula o L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        interpolated_value += L_i * y_points[i]

    return interpolated_value

# Exemplo de uso
if __name__ == "__main__":
    # Pontos conhecidos
    x_points = [1, 2, 3, 4]
    y_points = [1, 4, 9, 16]

    # Ponto onde deseja-se estimar f(x)
    x = 2.5

    # Estimativa usando Interpolação de Lagrange
    result = lagrange_interpolation(x_points, y_points, x)
    print(f"O valor interpolado em x = {x} é aproximadamente: {result:.6f}")

