"""
Exercício 21

Nome: Números repetidos
Objetivo: Criar uma lista com alguns números e detectar números repetidos dentro da lista.
Dificuldade: Avançado

1 - Crie uma lista com 20 números quaisquer (certifique-se de que alguns números são repetidos). Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.
2 - Exiba a quantidade de elementos que a lista possui.
3 - Varra todos os números da lista utilizando o for e exiba na tela apenas os números repetidos. Certifique-se de que cada número repetido apareça apenas uma vez.
4 - Declare uma nova lista e insira 20 números (de 1 a 30) de forma aleatória utilizando a biblioteca random, com o método random.randint(inicio, limite). Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela. Consulte a documentação da biblioteca em caso de dúvidas.
5 - Pegue o código de varredura da lista com o for declarado no item 3 e coloque-o em uma função chamada 'detectar_numeros_repetidos(lista)' que recebe um argumento referente a lista de números e retorna apenas os números repetidos. Execute a função para a lista de números criada no item 1 e exiba-a na tela.
6 - Execute a função declarada no item 5 para a lista de números criada no item 4.
7 - Crie uma função que receba uma lista de números e exiba na tela a quantidade de vezes que o número aparece repetido. Exiba a mensagem apenas para números repetidos e uma só vez por número. Dica: utilize o método 'lista.count(elemento)'.
8 - Crie uma função que receba uma lista de números e retorne um dicionário para cada número, onde a chave do dicionário é o número em questão e o valor do dicionário é a quantidade de vezes que o número se repete. Utilize o método 'lista.count(elemento)'. Se o item não se repetir, exiba a mensagem "O número X não se repete.", caso contrário, exiba a mensagem "O número X se repete Y vezes.".
9 - Faça a mesma coisa que no item 9, porém, em vez de utilizar o método 'count()', faça a checagem para saber se o item em questão está no dicionário utilizando a checagem do método 'dicionário.get(chave)'. Caso a checagem seja negativa (o dicionário ainda não possui o numero) adicione-o no dicionário utilizando 'dicionario[numero] = 1'. Caso a checagem seja positiva, atribua um valor adicional à posição do dicionário utilizando: 'dicionario[numero] = dicionario[numero] + 1'.
10 - Crie uma função que insere 20 números aleatórios (de 1 a 30) em uma lista certificando de que NENHUM número é repetido. Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.
"""
