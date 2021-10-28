## Contar frequencia dos termos

A partir de um dado texto, calcula a frequência dos termos por artigo e por frase.

Ex:
~~~
a. palavra_1: {contagem: [occurência_frase_1, occurência_frase_2, ... N]}
b. palavra_2: ...
c. ...
~~~

## Configuração
Virtualenv
~~~
python -m venv env
source ./env/bin/activate
~~~

Instalar nltk ([Help](https://www.nltk.org/install.html))
~~~
pip install nltk
~~~

Download dos arquivos nltk
~~~
python -m nltk.downloader punkt
~~~

## Como executar
~~~
cd app
python main.py -f files/small.txt
~~~

## Exemplo:

Input small.txt:
~~~
yy. foo foo foo! nbaz baz foo. bar? xx.
~~~

Output:
~~~
a. yy: {1: [1]}
b. foo: {4: [2, 3]}
c. nbaz: {1: [3]}
d. baz: {1: [3]}
e. bar: {1: [4]}
f. xx: {1: [5]}
~~~