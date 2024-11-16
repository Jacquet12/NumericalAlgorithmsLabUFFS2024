import sys
import os

# Adicionar o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.methods.integration.trapezoidal import trapezoidal_rule
from src.methods.integration.simpson import simpson_rule

import numpy as np

def func_a(x):
    """Função do problema (a): f(x) = e^(-x^2)"""
    return np.exp(-x**2)

def func_b(x):
    """Função do problema (b): f(x) = ln(x + sqrt(x + 1))"""
    return np.log(x + np.sqrt(x + 1))

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

        # Regra de Simpson
        integral_simp, points_simp = simpson_rule(f, a, b)
        print(f"Regra de Simpson: Integral = {integral_simp:.6f}")
        simp_table_file = os.path.join(results_dir, f"{name}_simpson_points.csv")
        np.savetxt(simp_table_file, points_simp, delimiter=',', header="x,y", comments='')
        print(f"Tabela de pontos salva em: {simp_table_file}")

if __name__ == "__main__":
    main()
