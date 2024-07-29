# Case 2
## Ordenação de palavras por frequência de caracteres  🐍
A tarefa solicita a utilização de Python para ordenar um array de strings com base na quantidade de vezes que um determinado caractere aparece na palavra, em ordem decrescente.

O array escolhido continha as strings "Gama", "Matematica", "Vestibular", "IA" e o caractere escolhido foi a letra "a".

Utilizou-se a função .sort() para ordenar a lista, criando um novo array. Foi fornecido como key value uma nova função anônima (lambda), que percorrerá os elementos do array original (palavras). 

Para cada elemento (palavra), as letras serão convertidas em minúsculas com o .lower(), uma vez que as letras minúsculas e maiúsculas possuem número de ordem diferente, não considerando somente a ordem alfabética. 

A função .count() recebe como parâmetro a variável caracter e realiza a contagem do mesmo em cada elemento do array. Por fim, para estabelecer a ordem decrescente, foi utilizado o parâmetro reverse e seu valor foi True.

O novo array é então printado com a função print().

