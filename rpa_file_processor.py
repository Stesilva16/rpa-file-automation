import os
import shutil
import pandas as pd
from datetime import datetime

# Diretórios
origem = "caminho/para/diretorio/origem"
destino = "caminho/para/diretorio/destino"

def mover_e_processar_arquivos():
    # Data atual no formato AAAA-MM-DD
    data_atual = datetime.now().strftime('%Y-%m-%d')

    for arquivo in os.listdir(origem):
        # Verifica se o arquivo é CSV e contém a data de hoje
        if arquivo.endswith('.csv') and data_atual in arquivo:
            caminho_origem = os.path.join(origem, arquivo)
            caminho_destino = os.path.join(destino, arquivo)
            
            # Lê o arquivo CSV
            df = pd.read_csv(caminho_origem)
            
            # Adiciona a nova coluna com a data da extração
            df['Data_Extracao'] = data_atual
            
            # Salva o arquivo processado no destino
            df.to_csv(caminho_destino, index=False)
            
            print(f"Arquivo '{arquivo}' movido e processado com sucesso!")

if __name__ == "__main__":
    mover_e_processar_arquivos()
