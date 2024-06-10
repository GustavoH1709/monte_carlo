import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_sheet1 = pd.read_excel('./soccer_stats.xlsx', sheet_name='Sheet 1')

valores = df_sheet1.iloc[:, 5].tolist()

media = np.mean(valores)
desvio_padrao = np.std(valores)

qtd_simulacoes = 1_000_000

simulacao = np.random.normal(media, desvio_padrao, qtd_simulacoes)

previsao = np.mean(simulacao)

plt.figure(figsize=(10, 6))
plt.hist(simulacao, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(previsao, color='red', linestyle='dashed', linewidth=2)
plt.title('Monte Carlo')
plt.xlabel('Média de gols')
plt.ylabel('Frequência')
plt.legend(['Próxima Média', 'Valores Simulados'])
plt.grid(True)
plt.xticks(np.arange(5.1, step=0.25))

plt.show()