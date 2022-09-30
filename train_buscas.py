from classifica_buscas import *
from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas = resultado -  teste_marcacoes 

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100 * (total_de_acertos / total_de_elementos)

print(taxa_de_acerto)
print(total_de_elementos)
