def chord_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Método das Cordas (Falsa Posição) para encontrar raízes de funções não lineares.

    Parâmetros:
    - f: função contínua.
    - a, b: extremos do intervalo [a, b] com f(a)*f(b) < 0.
    - tol: tolerância para o critério de parada.
    - max_iter: número máximo de iterações.

    Retorna:
    - raiz aproximada da função f no intervalo [a, b].
    """
    # Verifica se o intervalo inicial é válido
    if f(a) * f(b) >= 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos.")
        return None

    # Cabeçalho da tabela
    print(f"{'Iteração':<10}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}{'Erro':<12}")
    print("-" * 70)

    iter_count = 0
    c_old = a  # Valor inicial para calcular o erro na primeira iteração

    while iter_count < max_iter:
        # Calcula o ponto de interseção da reta secante com o eixo x
        c = b - f(b) * (b - a) / (f(b) - f(a))
        fc = f(c)
        error = abs(c - c_old)

        # Saída formatada
        print(f"{iter_count:<10}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<12.6f}{error:<12.6f}")

        # Critério de parada
        if error < tol or abs(fc) < tol:
            print("-" * 70)
            return c

        # Atualiza o intervalo com base no sinal de f(c)
        if f(a) * fc < 0:
            b = c  # Raiz está no intervalo [a, c]
        else:
            a = c  # Raiz está no intervalo [c, b]

        c_old = c
        iter_count += 1

    print("-" * 70)
    print("Número máximo de iterações atingido.")
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

    # Chamada do método das cordas
    raiz = chord_method(func, a, b, tol)
    print(f"\nA raiz aproximada é: {raiz:.6f}")
