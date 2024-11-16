def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Método da Secante para encontrar raízes de funções não lineares.

    Parâmetros:
    - f: função contínua.
    - x0, x1: aproximações iniciais.
    - tol: tolerância para o critério de parada.
    - max_iter: número máximo de iterações.

    Retorna:
    - raiz aproximada da função f.
    """
    # Cabeçalho da tabela
    print(f"{'Iteração':<10}{'x0':<12}{'x1':<12}{'f(x0)':<12}{'f(x1)':<12}{'Erro':<12}")
    print("-" * 70)

    iter_count = 0

    while iter_count < max_iter:
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Verifica se há divisão por zero
        if (f_x1 - f_x0) == 0:
            print("Divisão por zero detectada. Método não pode continuar.")
            return None

        # Calcula o próximo valor
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = abs(x_new - x1)

        # Saída formatada
        print(f"{iter_count:<10}{x0:<12.6f}{x1:<12.6f}{f_x0:<12.6f}{f_x1:<12.6f}{error:<12.6f}")

        # Critério de parada
        if error < tol:
            print("-" * 70)
            return x_new

        # Atualiza x0 e x1
        x0, x1 = x1, x_new
        iter_count += 1

    print("-" * 70)
    print("Número máximo de iterações atingido.")
    return x1

# Exemplo de uso
if __name__ == "__main__":
    # Defina a função cujo zero queremos encontrar
    def func(x):
        return x**3 - x - 2  # Exemplo: x^3 - x - 2 = 0

    # Aproximações iniciais
    x0 = 1
    x1 = 2
    tol = 1e-6

    # Chamada do método da secante
    raiz = secant_method(func, x0, x1, tol)
    print(f"\nA raiz aproximada é: {raiz:.6f}")
