apostila-python-orientacao-a-objetos pg 71/220: FUNÇÃO	COM	RETORNO


* Comentários *

- Para comentar uma linha, basta usar o caracter "#";

- Para comentar várias linhas, podemos utilizar o caracter '''
ex: ''' este é um
     comentários de
	várias linhas '''

_______________________________________________________________
	
* Quebra de linha em textos *

Utiliza o '\n' ex: print('Primeira linha \n Segunda linha')

_______________________________________________________________

* Imprimindo variaveis com texto *

Ex:

dia = 14
mes = 3
ano = 1993

print('Data Nascimento: ',dia,'/',mes,'/',ano)

Saída: 
	Data Nascimento:  14 / 3 / 1993

_______________________________________________________________

Imprimindo números float's (formatanbdo casa decimais):

print('exemplo {:.2f}'.format(variavel_float))

Onde: ":.2f" significa que são duas casas decimais após o ponto 


*Módulos*:

import nome_modulo
ex: import math 

ou importar um objeto específico do módulo:
ex:  from math import sqrt

- Número Randomicos:

import random

random.random() # Gera qualquer número

- Randomizar entre faixas de números inteiros:

random.randint(faixa_ini, faixa_fim)

- Randomizar um item de uma lista criada:

lista = [1,2,3,4]

sorteado = random.choice(lista)

- Truncando número:
import math ou from math import trunc

math.trunc(valor)

ou apenas convertendo explicitamente:

int(valor)


_______________________________________________________________
*Strings*

Caixa alta/baixa:

Caixa Alta :  variavel.upper()
Caixa Baixa:  variavel.lower()

Substituindo valores:

#Substitui por padrão  espaços em branco por vírgula:

variavel = "Olá mundo !"
print(variavel.split())

Saída:

	['Olá','mundo','!']

Colocando um caracter separado entre as variáveis de um print (sep), exemplo:
ex:
var_a = 'a' 
var_b =	'b'

print(a , b, sep='-')

Saída:

a - b

Podemos também utilizar o "end" para inserir uma informação no final, ex:

print('teste', end = 'end')

Saída:

teste end 


_______________________________________________________________

* Listas *

- Adicionando elemento no final de uma lista(append):
	
	lista = [1,2,3]
	
	lista.append(novo_valor)

- Adicionando varios valores de uma única vez em uma lista:

lista.extend(['valor1', 'valor2'])	

- Adicionando elemento em qualquer posição da lista:

	lista.insert(posição, novo_valor)


- Removendo um valor no final da lista:

	lista.pop()

- Removendo um valor em uma posição específica da lista:

	lista.pop(indice/posição) ou del lista[indice]


- Ordenando uma lista de forma crescente:
	
	lista.sort()

- Ordenando uma lista de forma descrescente:

	lista.sort(reverse = True)

- Invertendo os valores em uma lista:

lista.reverse()

- Função que calcula a quantidade de itens em uma lista (len())

	quantidade = len(lista)

- Retornando o maior valor em uma Lista:

maior_elemento.max(lista);

- Retornando o menor valor em uma Lista:

lista.min()

- Verificando se existe um valor em uma lista:

item in lista ou "elemento" in lista;

Vai retornar um boleano (True ou False) como resultado.	

- Retornar um índice de um determinado valor na lista:

lista.index(valor)

- Embaralhando os elementos de uma lista:

 import random ou from random import shuffle

 lista[1,2,3,4,5]

 random.shuffle(lista)

 Exemplo:

import random

lista = [1, 2, 3, 4, 5]
lista_embaralhada = []

lista_embaralhada = lista.copy()
random.shuffle(lista_embaralhada)

print(lista_embaralhada)

Saída:

[5, 1, 4, 2, 3]

- Transformando uma string em uma lista, função list():

lista = list('teste')

Saída:
	['t','e','s','t','e']

Copiando os valores de uma lista para outra:

new_list = old_list[:]

ou

for item in old_list:
	new_list.append(item)

Observação: se fizer "new_list = old_list" estaremos referenciando new_list para old_list, se qualquer lista for alterada, ambas serão.




_______________________________________________________________

* Conjuntos *

Observação1: Um conjunto não pode ser alterado como uma lista;
Observação2: Um conjunto não pode conter elementos repetidos

- Criando um conjunto: usuarios = {"Iza", "Sebastian"}

- Transformando um conjunto em uma lista: usuarios = set["Iza", "Sebastian"]

_______________________________________________________________

* Tuplas *

Tuplas são estruturas imutáveis, e são criadas da seguinte forma:

tupla = (v1, v2, v3) ou tupla = v1, v2, v3

- Acessando um elmento em uma tupla:
tupla[posição] -> tupla[0]

- Convertendo tupla para lista (para realizar alterações):

tupla_1(1,2,3)

lista_tupla_1 = list(tupla_1)

- Convertendo a lista para uma tupla:

new_tupla = tuple(lista_tupla_1)






_______________________________________________________________

* Conjuntos *

- Não admite elementos duplicados;

exemplo: 

conjunto_nome = {'valor_1','valor_2','valor_3'}

ou tranformando uma lista em conjunto com o método "set":

lista = set(["valor_1", "valor_2"])

- Adicionando um elemento:

conjunto_nome.add("novo_valor") 

Observação: Podemos pegar uma lista com valores repetidos e transforma-la em um conjunto afim de remover as duplicatas:

lista = [1,2,3,4,5,2,3,3]

tratar_duplicata = set(lista)

print(tratar_duplicata)

Saída:
	{1, 2, 3, 4, 5}

- União de conjuntos:

	numeros_1 = {1, 2, 3}
	numeros_2 = {4, 5, 6}

uniao = numeros_1.union(numeros_2)

print(uniao)

Saída: {1, 2, 3, 4, 5, 6}

ou

uniao = numeros_1 | numeros_2

A saída será a mesma

- Intersecção de conuntos (elementos comuns em ambas):

numeros_1.intersection(numeros_2) ou intersect = numeros_1 & numeros_2

- Diferença entre conjuntos:
	
	numeros_1.difference(numeros_2) ou diferenca = numeros_1 - numeros_2









_______________________________________________________________
Dicionarios:

- Pode ser acessado pela chave:

dic = {'Chave':'valor'}
pessoa = {'Nome':'Fulano', 'Idade':30}

- Acessando a chave 'nome':

pessoa['nome']

- adicionando um elemento em uma chave:

pais['nome'] = 'Brasil'

- Alterar chave em um dicionário:
dicionario[""]

- Retornar as chaves de um dicionário, usamos o método keys():

pais.keys();

- Retornar os valores de um dicionário, usamos o método values():

pais.values()

- Retornar todos os elementos de um dicionario:
nome_dic.items()

- Retornando um valor de uma chave específica:

nome_dic.get('nome_chave')

- Retornando um valor padrão caso a chave não for encontrada?

nome_dic.get('nome_chave','valor não encontrado')

- Unindo/atualizando dicionários distintos (update):
	
	dic_1.update(dic_2)

Iterando sobre uma chave específica (nota) no dicionário:
	
	alunos = [
    {
     'nome': 'Alice',
     'nota': 8,
    },
    {
     'nome': 'Bop',
     'nota': 7,
    },
    {
     'nome': 'Carlos',
     'nota': 9,
    }
]

total = 0

for nota in alunos:
    total += nota['nota']

print(total / len(alunos))

- Verficando se um determinado valor/variável está em um dicionário:

dicionario = {'nome': 'Fulano', 'idade':30}

	if 'nome' in dicionario:
		print('Nome: {}'.format(dicionario['nome']))
		

- deletar uma chave em um dicionário:

del dicionario['nome_chave']		

______________________________________________________________






	



	
