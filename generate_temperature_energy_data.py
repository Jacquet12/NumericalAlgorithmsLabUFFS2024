import numpy as np
import os

def generate_temperature_energy_data(file_path='data/data.csv'):
    """
    Gera um banco de dados simulando a relação entre temperatura e consumo de energia elétrica.

    Parâmetros:
    - file_path: caminho para salvar o arquivo CSV.
    """
    # Garantir que o diretório existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Gerar dados
    np.random.seed(42)  # Garantir reprodutibilidade
    x = np.linspace(10, 35, 50)  # Temperatura de 10°C a 35°C (50 pontos)
    y = 5 * x - 20 + np.random.normal(0, 10, len(x))  # Consumo com ruído aleatório

    # Salvar os dados no arquivo CSV
    np.savetxt(file_path, np.column_stack((x, y)), delimiter=',', header='x,y', comments='', fmt='%.2f')
    print(f"Banco de dados gerado e salvo em: {file_path}")

if __name__ == "__main__":
    generate_temperature_energy_data()
