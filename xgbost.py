from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Suponha que seu dataframe tem colunas como:
# ['time_casa', 'time_fora', 'gols_casa', 'gols_fora', 'posse_casa', 'chutes_casa', ...]

# Pré-processar os dados
features = df[['posse_casa', 'chutes_casa', 'escanteios_casa', 'posse_fora', 'chutes_fora', 'escanteios_fora']]
target_casa = df['gols_casa']
target_fora = df['gols_fora']

X_train, X_test, y_train, y_test = train_test_split(features, target_casa, test_size=0.2)

model_casa = XGBRegressor()
model_casa.fit(X_train, y_train)
predictions = model_casa.predict(X_test)

print("RMSE:", np.sqrt(mean_squared_error(y_test, predictions)))
