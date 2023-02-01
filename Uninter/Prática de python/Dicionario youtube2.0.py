galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa['Nome'] = str(input('Qual o seu Nome ? '))
    while True:
        pessoa['Sexo'] = str(input('Qual o seu Sexo ? [M/F]')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Digite M ou F')
    pessoa['Idade'] = int(input('Qual a sua idade '))
    soma += pessoa['Idade']
    resp = str(input('Quer Cadastrar Mais pessoas ? [S/N]')).upper()[0]
    while True:
        if resp in 'NS':
            galera.append(pessoa.copy())
            break
    if resp == 'N':
        break

media = float(soma / len (galera))
print(galera)
print(soma)
print(media)
for item in galera:
    if item['Sexo'] == 'M':
        print(item["Nome"], end=' ')
    print('\n')