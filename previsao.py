novo_jogo = pd.DataFrame([{
    'posse_casa': 55,
    'chutes_casa': 14,
    'escanteios_casa': 5,
    'posse_fora': 45,
    'chutes_fora': 10,
    'escanteios_fora': 3
}])

gols_previstos = model_casa.predict(novo_jogo)
print(f"Gols previstos para o time da casa: {gols_previstos[0]:.1f}")
