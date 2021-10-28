## Contar frequencia dos termos

## Descrição do desafio

### Concordância

"Dado um documento de texto arbitrário escrito em inglês, escreva um programa que gere uma
concordância, ou seja, uma lista alfabética de todas as ocorrências de palavras, rotuladas
com frequências de palavras.

Bônus: rotule cada palavra com os números das frases em que cada ocorrência apareceu."

Imprima alfabeticamente, uma por linha, no seguinte formato:
~~~~
a. palavra_1: {contagem: [occurência_frase_1, occurência_frase_2, ... N]}
b. palavra_2: ...
c. ...
~~~~

Exemplo ao executar o arquivo "small.txt"
~~~~
**-- CONCORDANCIA --*
a. bar: {1: [4]}
b. baz: {1: [3]}
c. foo: {4: [2,2]}
d. nbaz: {1: [3]}
e. xx: {1: [5]}
f. yy: {1: [1]}
**-- FINAL DA CONCORDANCIA --*
~~~~


Arquivo "small.txt"
~~~~
yy. foo foo foo! nbaz baz foo. bar? xx.
~~~~

Arquivo "big.txt" exemplo
[http://norvig.com/big.txt](http://norvig.com/big.txt)