import sys
import os

# Adicionar o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.methods.integration.trapezoidal import trapezoidal_rule
from src.methods.integration.simpson import simpson_rule
import numpy as np
import matplotlib.pyplot as plt

# Função do problema (a)
def func_a(x):
    return np.exp(-x**2)

# Função do problema (b)
def func_b(x):
    return np.log(x + np.sqrt(x + 1))

def plot_results(x, y, method, problem_name, results_dir):
    """
    Gera gráficos dos pontos (x, y) usados em cada método de integração.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"{method} Points", marker="o", linestyle="--")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Integration Points for {problem_name} - {method}")
    plt.legend()
    plt.grid(True)

    # Salvar o gráfico
    plot_file = os.path.join(results_dir, f"{problem_name}_{method.lower()}_plot.png")
    plt.savefig(plot_file)
    plt.close()
    print(f"Gráfico salvo em: {plot_file}")

def main():
    # Diretório para salvar resultados
    results_dir = "plots/integration"
    os.makedirs(results_dir, exist_ok=True)

    # Problemas
    problems = [
        (func_a, 0, 1, "problem_a"),
        (func_b, 1, 2, "problem_b")
    ]

    for f, a, b, name in problems:
        print(f"\n{name.upper()}: Integração no intervalo [{a}, {b}]")

        # Regra dos Trapézios
        integral_trap, points_trap = trapezoidal_rule(f, a, b)
        print(f"Regra dos Trapézios: Integral = {integral_trap:.6f}")
        trap_table_file = os.path.join(results_dir, f"{name}_trapezoidal_points.csv")
        np.savetxt(trap_table_file, points_trap, delimiter=',', header="x,y", comments='')
        print(f"Tabela de pontos salva em: {trap_table_file}")
        plot_results(points_trap[:, 0], points_trap[:, 1], "Trapezoidal", name, results_dir)

        # Regra de Simpson
        integral_simp, points_simp = simpson_rule(f, a, b)
        print(f"Regra de Simpson: Integral = {integral_simp:.6f}")
        simp_table_file = os.path.join(results_dir, f"{name}_simpson_points.csv")
        np.savetxt(simp_table_file, points_simp, delimiter=',', header="x,y", comments='')
        print(f"Tabela de pontos salva em: {simp_table_file}")
        plot_results(points_simp[:, 0], points_simp[:, 1], "Simpson", name, results_dir)

if __name__ == "__main__":
    main()