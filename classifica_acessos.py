from dados import carregar_acessos

X, Y = carregar_acessos()
# Separando em grupo de treino e grupo de teste

# dados de treino e marcacoes de treino
treino_dados = X[:90]
treino_marcacoes = Y[:90]
# dados de teste e marcacoes de teste
teste_dados = X[-9:]
teste_marcacoes = Y[-9:]
