from pandas import *

valores = [10, 10, 20, 30, 40, 50, 10]
valores_serie = DataFrame(valores)
print(valores_serie)

aluno_1 = {'Nome': 'João', 'Matemática': 6, 'Português': 7}
aluno_2 = {'Nome': 'Maria', 'Matemática': 8, 'Português': 8}
aluno_3 = {'Nome': 'Pedro', 'Matemática': 4, 'Português': 5.3}
aluno_4 = {'Nome': 'Suzana', 'Matemática': 5.8, 'Português': 6.5}
aluno_5 = {'Nome': 'Yago', 'Matemática': 6, 'Português': 7}
df = DataFrame([aluno_1, aluno_2, aluno_3, aluno_4, aluno_5])
print(df)
