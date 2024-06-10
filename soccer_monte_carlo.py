import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_sheet1 = pd.read_excel('./soccer_stats.xlsx', sheet_name='Sheet 1')

goals_values = df_sheet1.iloc[:, 5].tolist()

mean_goals = np.mean(goals_values)
std_dev_goals = np.std(goals_values)

print(goals_values)

num_simulations = 20000

simulated_values = np.random.normal(mean_goals, std_dev_goals, num_simulations)

predicted_next_mean = np.mean(simulated_values)

plt.figure(figsize=(10, 6))
plt.hist(simulated_values, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(predicted_next_mean, color='red', linestyle='dashed', linewidth=2)
plt.title('Monte Carlo')
plt.xlabel('Média de gols')
plt.ylabel('Frequência')
plt.legend(['Próxima Média', 'Valores Simulados'])
plt.grid(True)
plt.xticks(np.arange(5.1, step=0.25))

plt.show()