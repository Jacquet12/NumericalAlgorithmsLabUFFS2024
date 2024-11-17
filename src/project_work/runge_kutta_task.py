import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.methods.differentialEquations.runge_kutta_4th import runge_kutta_fourth_order

# Derivada dada pelo PVI
def dydx(x, y):
    return y / x - (y / x)**2

# Solução analítica
def analytical_solution(x):
    return x / (1 + np.log(x))

# Gráfico comparativo
def plot_comparison(x_exact, y_exact, solutions, h_values, output_path):
    plt.figure(figsize=(10, 6))
    plt.plot(x_exact, y_exact, label="Solução Analítica", color="black", linewidth=2)
    for i, (x, y) in enumerate(solutions):
        plt.plot(x, y, label=f"Runge-Kutta (h={h_values[i]})", linestyle="--", marker="o")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.title("Comparação: Solução Analítica vs Método de Runge-Kutta")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()
    print(f"Gráfico comparativo salvo em: {output_path}")

# Gráfico de erro
def plot_error(x_exact, y_exact, solutions, h_values, output_path):
    plt.figure(figsize=(10, 6))
    for i, (x, y) in enumerate(solutions):
        y_interp = np.interp(x, x_exact, y_exact)  # Interpolar solução analítica nos pontos de Runge-Kutta
        error = np.abs(y - y_interp)
        plt.plot(x, error, label=f"Erro (h={h_values[i]})", linestyle="--", marker="o")
    plt.xlabel("x")
    plt.ylabel("Erro |y_analítico - y_runge_kutta|")
    plt.title("Erro: Método de Runge-Kutta vs Solução Analítica")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()
    print(f"Gráfico de erro salvo em: {output_path}")

# Resolução do problema
def main():
    x0, y0 = 1, 1  # Condição inicial
    x_end = 3
    h_values = [0.25, 0.1, 0.05]

    # Solução analítica
    x_exact = np.linspace(x0, x_end, 1000)
    y_exact = analytical_solution(x_exact)

    # Soluções aproximadas pelo método de Runge-Kutta
    solutions = [runge_kutta_fourth_order(dydx, x0, y0, h, x_end) for h in h_values]

    # Diretório de saída para gráficos
    results_dir = "plots/pvi_runge_kutta"
    os.makedirs(results_dir, exist_ok=True)

    # Gráfico comparativo
    plot_comparison(
        x_exact, y_exact, solutions, h_values,
        output_path=f"{results_dir}/comparison_plot_rk.png"
    )

    # Gráfico de erro
    plot_error(
        x_exact, y_exact, solutions, h_values,
        output_path=f"{results_dir}/error_plot_rk.png"
    )

if __name__ == "__main__":
    main()
