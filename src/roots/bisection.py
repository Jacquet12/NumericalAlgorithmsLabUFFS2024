import numpy as np

def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Método da Bisseção para encontrar raízes de funções não lineares.

    Parâmetros:
    - f: função contínua em [a, b]
    - a, b: extremos do intervalo [a, b] com f(a)*f(b) < 0
    - tol: tolerância para o critério de parada
    - max_iter: número máximo de iterações

    Retorna:
    - raiz aproximada da função f no intervalo [a, b]
    """
    if f(a) * f(b) >= 0:
        print("O método da bisseção falha: f(a) e f(b) devem ter sinais opostos.")
        return None

    # Cabeçalho da tabela
    print(f"{'Iteração':<10}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}")
    print("-" * 58)

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        fc = f(c)

        # Saída formatada
        print(f"{iter_count:<10}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<12.6f}")

        if fc == 0:
            return c
        elif f(a) * fc < 0:
            b = c  # A raiz está no intervalo [a, c]
        else:
            a = c  # A raiz está no intervalo [c, b]
        iter_count += 1

    # Última iteração
    c = (a + b) / 2
    fc = f(c)
    print(f"{iter_count:<10}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<12.6f}")
    print("-" * 58)

    return c

# Exemplo de uso
if __name__ == "__main__":
    # Defina a função cujo zero queremos encontrar
    def func(x):
        return x**3 - x - 2  # Exemplo: x^3 - x - 2 = 0

    # Intervalo inicial e tolerância
    a = 1
    b = 2
    tol = 1e-6

    # Chamada do método da bisseção
    raiz = bisection(func, a, b, tol)
    print(f"\nA raiz aproximada é: {raiz:.6f}")
