nome = input('Nome: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = ((nota1+nota2+nota3)/3)
situacao = ''

if media >= 7:
    situacao += f'Aprovado'

elif media >= 5 and media <= 6.9:

    situacao += f'Recuperação'
else:
    situacao += f'Reprovado'

print('===== RESULTADO =====')
print(f'Aluno: {nome}\n')
print(f'Média: {media:.2f}\n')
print(f'Situação: {situacao}')
print('======================')