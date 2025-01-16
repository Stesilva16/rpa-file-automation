# 🛠️ RPA com Python: Automatizando Processos Repetitivos  

Este repositório apresenta um caso prático de automação de processos usando Python. Durante a migração de sistemas na empresa, precisávamos diariamente mover arquivos CSV para um novo diretório e adicionar uma coluna com a data da extração. Este script simplifica essa tarefa e mostra como o RPA pode ser aplicado no dia a dia.

## 🚀 Funcionalidades  
- Localiza arquivos com base na data atual.  
- Move arquivos do diretório de origem para o destino.  
- Processa os arquivos adicionando uma nova coluna com a data da extração.  

## 📂 Estrutura  
- **`origem/`**: Diretório onde os arquivos são armazenados inicialmente.  
- **`destino/`**: Diretório onde os arquivos processados são armazenados.  

## ⚙️ Como usar  
1. Instale as dependências necessárias:  
   ```bash  
   pip install pandas  
   ```  
2. Ajuste os caminhos dos diretórios no código.  
3. Execute o script:  
   ```bash  
   python mover_processar_arquivos.py  
   ```  

## 📌 Observação  
Este script é apenas um exemplo. Certifique-se de personalizá-lo para atender às necessidades específicas do seu caso. 

* *By: Stefany Gracy 💛*
