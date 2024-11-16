import numpy as np

def jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Método de Jacobi para resolver sistemas lineares Ax = b.

    Parâmetros:
    - A: matriz de coeficientes (n x n).
    - b: vetor de constantes (n x 1).
    - x0: vetor inicial de aproximações (n x 1). Se None, inicia com zeros.
    - tol: tolerância para o critério de parada.
    - max_iter: número máximo de iterações.

    Retorna:
    - x: solução aproximada do sistema.
    - iter_count: número de iterações realizadas.
    """
    # Verifica se a matriz A é quadrada
    n = len(A)
    if A.shape[0] != A.shape[1]:
        raise ValueError("A matriz A deve ser quadrada.")
    if len(b) != n:
        raise ValueError("O vetor b deve ter o mesmo número de linhas que A.")

    # Inicialização
    x = np.zeros(n) if x0 is None else x0
    iter_count = 0

    # Iterações
    for iter_count in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            sum_1 = sum(A[i, j] * x[j] for j in range(n) if j != i)  # Somatório para j ≠ i
            x_new[i] = (b[i] - sum_1) / A[i, i]  # Atualização de x_i

        # Critério de parada
        error = np.linalg.norm(x_new - x, ord=np.inf)
        print(f"Iteração {iter_count + 1}: x = {x_new}, Erro = {error:.6e}")
        if error < tol:
            return x_new, iter_count + 1

        x = x_new

    print("Número máximo de iterações atingido.")
    return x, iter_count + 1

# Exemplo de uso
if __name__ == "__main__":
    # Matriz de coeficientes A e vetor b
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)

    # Aproximação inicial (opcional)
    x0 = np.zeros(len(b))

    # Resolvendo o sistema
    tol = 1e-6
    x, iterations = jacobi(A, b, x0, tol)
    print(f"\nSolução aproximada: x = {x}")
    print(f"Número de iterações: {iterations}")
