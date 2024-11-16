def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raízes de funções não lineares.

    Parâmetros:
    - f: função contínua.
    - df: derivada da função f.
    - x0: aproximação inicial.
    - tol: tolerância para o critério de parada.
    - max_iter: número máximo de iterações.

    Retorna:
    - raiz aproximada da função f.
    """
    # Cabeçalho da tabela
    print("{:<10}{:<12}{:<12}{:<12}{:<12}".format("Iteração", "x", "f(x)", "f'(x)", "Erro"))
    print("-" * 58)

    x = x0
    iter_count = 0

    while iter_count < max_iter:
        fx = f(x)
        dfx = df(x)
        
        # Verifica se a derivada é zero (evita divisão por zero)
        if dfx == 0:
            print("Derivada igual a zero. Método não pode continuar.")
            return None

        # Calcula a próxima aproximação
        x_new = x - fx / dfx
        error = abs(x_new - x)

        # Saída formatada
        print("{:<10}{:<12.6f}{:<12.6f}{:<12.6f}{:<12.6f}".format(iter_count, x, fx, dfx, error))

        # Critério de parada
        if error < tol:
            print("-" * 58)
            return x_new

        # Atualiza x para a próxima iteração
        x = x_new
        iter_count += 1

    print("-" * 58)
    print("Número máximo de iterações atingido.")
    return x

# Exemplo de uso
if __name__ == "__main__":
    # Defina a função e sua derivada
    def func(x):
        return x**3 - x - 2  # Exemplo: x^3 - x - 2 = 0

    def dfunc(x):
        return 3*x**2 - 1  # Derivada: 3x^2 - 1

    # Aproximação inicial
    x0 = 1.5
    tol = 1e-6

    # Chamada do método de Newton-Raphson
    raiz = newton_method(func, dfunc, x0, tol)
    print(f"\nA raiz aproximada é: {raiz:.6f}")
