# Importa bibliotecas
import random
import string

# Quantidade de caracteres da senha
tamanho = int(input('Digite o número de caracteres da senha que deseja: '))

# Caracteres: letras maiúsculas e minúsculas, números de 0 a 9, caracteres especiais
chars = string.ascii_letters + string.digits + '!@#$%*_=+'

# Cria um objeto SystemRandom da biblioteca random para geração de números aleatórios criptograficamente seguros
rnd = random.SystemRandom()

# Mostra a senha criada: join é usado para unir os caracteres aleatórios gerados em uma única string
# rnd.choice(chars) é usado para escolher aleatoriamente um caractere da sequência 'chars'
# for i in range(tamanho) é usado para iterar os caracteres, um de cada vez, até que o tamanho definido seja atingido
senha = (''.join(rnd.choice(chars) for i in range(tamanho)))
print(senha)
