import numpy as np
import matplotlib.pyplot as plt
import os

# Função para o termo independente da equação diferencial
def f(x):
    return -np.exp(x) * (x**2 + 1)

# Método de diferenças finitas centradas para resolver o PVC
def finite_difference_method(h, x_start, x_end, y0, y1):
    """
    Método de diferenças finitas centradas para resolver PVC.
    
    Parâmetros:
    - h: tamanho do passo
    - x_start, x_end: limites do intervalo
    - y0, y1: condições de contorno (y(x_start), y(x_end))
    
    Retorna:
    - x_values: pontos x no intervalo
    - y_values: solução aproximada em cada ponto x
    """
    # Discretização do intervalo
    x_values = np.arange(x_start, x_end + h, h)
    n = len(x_values) - 2  # Número de pontos internos

    # Matriz tridiagonal A
    A = np.zeros((n, n))
    for i in range(n):
        xi = x_values[i + 1]  # Ponto interno correspondente
        if i > 0:
            A[i, i - 1] = 1 / h**2 - 1 / (2 * h)  # Coeficiente de y_{i-1}
        A[i, i] = -2 / h**2 - xi  # Coeficiente de y_i
        if i < n - 1:
            A[i, i + 1] = 1 / h**2 + 1 / (2 * h)  # Coeficiente de y_{i+1}

    # Vetor b
    b = f(x_values[1:-1])  # Avaliar f(x) nos pontos internos
    b[0] -= y0 * (1 / h**2 - 1 / (2 * h))  # Ajuste da condição de contorno em x_start
    b[-1] -= y1 * (1 / h**2 + 1 / (2 * h))  # Ajuste da condição de contorno em x_end

    # Resolver o sistema linear
    y_internal = np.linalg.solve(A, b)

    # Adicionar os valores das condições de contorno
    y_values = np.concatenate(([y0], y_internal, [y1]))
    return x_values, y_values

# Função para salvar os resultados numéricos
def save_results(results, h_values, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for i, (x, y) in enumerate(results):
        filename = os.path.join(output_dir, f"solution_h_{h_values[i]}.txt")
        np.savetxt(filename, np.column_stack((x, y)), header="x y", comments="")
        print(f"Resultado salvo em: {filename}")

# Função para plotar as soluções
def plot_solutions(solutions, h_values, output_path):
    plt.figure(figsize=(10, 6))
    for i, (x, y) in enumerate(solutions):
        plt.plot(x, y, label=f"h = {h_values[i]}")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.title("Soluções do PVC com diferenças finitas")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()
    print(f"Gráfico salvo em: {output_path}")

# Função principal para executar o exercício 5
def main():
    # Parâmetros do PVC
    x_start, x_end = 0, 1  # Intervalo de solução
    y0, y1 = 0, np.exp(1)  # Condições de contorno
    h_values = [0.1, 0.05, 0.01]  # Valores de h solicitados

    # Resolver o PVC para cada valor de h
    solutions = [finite_difference_method(h, x_start, x_end, y0, y1) for h in h_values]

    # Diretório para salvar resultados
    results_dir = "plots/pvc"
    os.makedirs(results_dir, exist_ok=True)

    # Salvar os resultados numéricos
    save_results(solutions, h_values, results_dir)

    # Salvar o gráfico das soluções
    plot_solutions(solutions, h_values, os.path.join(results_dir, "pvc_solutions.png"))

if __name__ == "__main__":
    main()
