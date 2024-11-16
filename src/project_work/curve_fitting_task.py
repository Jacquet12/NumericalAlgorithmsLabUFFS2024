import numpy as np
import matplotlib.pyplot as plt
import os

def run_curve_fitting_task():
    # Caminho absoluto para o banco de dados
    file_path = os.path.join(os.path.dirname(__file__), "../../data/data.csv")

    # Carregar o banco de dados
    try:
        data = np.loadtxt(file_path, delimiter=',', skiprows=1)
        x, y = data[:, 0], data[:, 1]
        print("Banco de dados carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o banco de dados: {e}")
        return

    # Criar o diretório para salvar gráficos
    plots_dir = "plots/curve_fitting"
    os.makedirs(plots_dir, exist_ok=True)

    # Ajuste Linear
    linear_coef = np.polyfit(x, y, 1)  # Grau 1
    y_linear = np.polyval(linear_coef, x)
    r2_linear = r_squared(y, y_linear)

    # Ajuste Exponencial
    try:
        log_y = np.log(y - np.min(y) + 1)  # Normalizar para evitar log de valores negativos
        exp_coef = np.polyfit(x, log_y, 1)
        a_exp, b_exp = np.exp(exp_coef[1]), exp_coef[0]
        y_exp = a_exp * np.exp(b_exp * x)
        r2_exp = r_squared(y, y_exp)
    except Exception as e:
        print(f"Erro no ajuste exponencial: {e}")
        y_exp, r2_exp = None, None

    # Ajuste Polinomial (grau 3)
    poly_coef = np.polyfit(x, y, 3)  # Grau 3
    y_poly = np.polyval(poly_coef, x)
    r2_poly = r_squared(y, y_poly)

    # Gerar Gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label="Dados Originais", color="black")
    plt.plot(x, y_linear, label=f"Linear (R²={r2_linear:.4f})", color="blue")
    if y_exp is not None:
        plt.plot(x, y_exp, label=f"Exponencial (R²={r2_exp:.4f})", color="green")
    plt.plot(x, y_poly, label=f"Polinomial (R²={r2_poly:.4f})", color="red")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Consumo de Energia (kWh)")
    plt.title("Ajuste de Curvas - Temperatura vs Consumo de Energia")
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(plots_dir, "curve_fitting.png"))
    plt.close()  # Fecha o gráfico para liberar memória

    # Exibir coeficientes
    print("\nCoeficientes Obtidos:")
    print(f"Ajuste Linear: {linear_coef}")
    if y_exp is not None:
        print(f"Ajuste Exponencial: a = {a_exp:.4f}, b = {b_exp:.4f}")
    print(f"Ajuste Polinomial: {poly_coef}")

    # Salvar matrizes em arquivo
    matrices_file = os.path.join(plots_dir, "curve_fitting_matrices.txt")
    with open(matrices_file, "w") as f:
        f.write("Coeficientes Obtidos:\n")
        f.write(f"Ajuste Linear: {linear_coef}\n")
        if y_exp is not None:
            f.write(f"Ajuste Exponencial: a = {a_exp:.4f}, b = {b_exp:.4f}\n")
        f.write(f"Ajuste Polinomial: {poly_coef}\n")
        f.write("\nValores de R²:\n")
        f.write(f"R² Linear: {r2_linear:.4f}\n")
        if y_exp is not None:
            f.write(f"R² Exponencial: {r2_exp:.4f}\n")
        f.write(f"R² Polinomial: {r2_poly:.4f}\n")

    print(f"Resultados salvos em: {plots_dir}/")

def r_squared(y_real, y_pred):
    """
    Calcula o coeficiente de determinação R².
    """
    ssr = np.sum((y_real - y_pred) ** 2)
    sst = np.sum((y_real - np.mean(y_real)) ** 2)
    return 1 - ssr / sst

if __name__ == "__main__":
    run_curve_fitting_task()
