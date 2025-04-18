import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Supondo que 'df' seja o DataFrame com os dados preparados
X = df[['gols_marcados', 'gols_sofridos', 'posse_bola', 'escanteios', 'chutes_a_gol']]
y = df['gols_time_casa']  # ou 'gols_time_fora', dependendo da previsão desejada

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print(f"Erro Quadrático Médio: {mean_squared_error(y_test, y_pred)}")
