from classificacao import *

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
#fit -> adequar/encaixar
modelo.fit(dados, marcacoes)
print(modelo.predict(teste))
