import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

df = sns.load_dataset('tips')
print("Dataset 'Tips' carregado com sucesso!")

q1 = df['total_bill'].quantile(0.25)
q2 = df['total_bill'].median()
q3 = df['total_bill'].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = df[(df['total_bill'] < limite_inferior) | (df['total_bill'] > limite_superior)]

print(f"\n--- Resultados do Exercício 3.1 ---")
print(f"Q1: {q1:.2f} | Q3: {q3:.2f} | IQR: {iqr:.2f}")
print(f"Limite Superior: {limite_superior:.2f}")
print(f"Quantidade de Outliers encontrados: {len(outliers)}")
print("\nExemplos de registros considerados outliers:")
print(outliers.head())