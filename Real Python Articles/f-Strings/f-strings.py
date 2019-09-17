"""
Real Python - Python f-Strings

https://realpython.com/python-f-strings/
"""
# Antes da versão 3.6:
# %-formatting
# str.format

# %-formatting
# Na linguagem desde o começo. Não recomendado. Cheio de quirks.
# Messy with too many variables

name = 'Eric'
print("Hello, %s." % name)

# Para inserir mais de uma variável, inserir uma tupla dessas variáveis

name = 'Eric'
age = 74
print("Hello, %s. You are %s" % (name, age))

# str.format()
# Introduzido em Python 2.6
# É extensível através do método __format__() no objeto sendo convertido
# para uma string

print("Hello, {}. You are {}.".format(age, name))

# Se inserir o nome da variável, pode passar objetos e então referenciar
# parâmetros e métodos entre as chaves

person = {'name': 'Gabriel', 'age': 74}
print("Hello {name}. You are {age}.".
      format(name=person['name'], age=person['age']))

# Também pode user ** para fazer esse truque com dicionários
print("Hello, {name}. You have {age}.".format(**person))
