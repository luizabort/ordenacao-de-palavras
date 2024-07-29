# Case 2
## Ordenação de palavras por frequência de caracteres  🐍
A tarefa solicita a utilização de Python para ordenar um array de strings com base na quantidade de vezes que um determinado caractere aparece na palavra, em ordem decrescente.

O array escolhido continha as strings "Gama", "Matematica", "Vestibular", "IA" e o caractere escolhido foi a letra "a".

Utilizou-se a função .sort() para ordenar a lista. Foi fornecido como key value uma função lambda, que retornará a quantidade de caracteres específicos encontrados em cada elemento (palavra).  

Para a verificação, as letras serão convertidas em minúsculas com o .lower(), uma vez que as letras minúsculas e maiúsculas possuem valores diferentes, podendo não ser reconhecido.

A função .count() recebe como parâmetro a variável caractere, que representa nosso letra buscada, e retorna a frequência da mesma em cada elemento do array. Por fim, para estabelecer a ordem decrescente, foi utilizado o parâmetro reverse.

O array é então exibido com a função print().

