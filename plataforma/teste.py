
info =['2022', '2021', '2020', '2019', '2018', '2017']
dados=['disponivel', 'indisponivel', 'indisponivel', 'indisponivel', 'indisponivel', 'indisponivel']

lista = info, dados

for a , b in zip(info, dados):
    print(a ,b)