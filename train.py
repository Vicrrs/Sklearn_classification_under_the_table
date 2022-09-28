from classificacao import *

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
#fit -> adequar/encaixar
modelo.fit(dados, marcacoes)
resultado = modelo.predict(testes)
print(resultado)

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(testes)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(resultado)
print(diferencas)
print(taxa_de_acerto)
