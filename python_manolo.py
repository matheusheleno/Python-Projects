import time
class Carro:
    def __init__(self, marca, modelo, ano, kilo, tracao, HP, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilo = kilo
        self.tracao = tracao
        self.HP = HP
        self.preco = preco

    def InformacoesCarro(self):
        print('Este carro é da Marca ' + self.marca + ', o modelo é o ' + self.modelo +
              ';\nFabricado no ano de ' + self.ano + ' o peso da sua carroceria é de apróximadamente ' + self.kilo +
              ';\nA tração dele é ' + self.tracao +
              ';\nEmbaixo do capo estão os incríveis ' + self.HP + ' Cavalos de potência para você andar com estilo !'
              ';\nTudo isso pode ser seu por apenas :\nR$' + self.preco + ' .')


carro1 = Carro('Wolksvagem', 'Jetta GLI T', '2021', '1.432 KG', 'FWD', '230', '178.490,00')
carro2 = Carro('Subaru', 'WRX STi 2.5 T', '2020', '1.530 KG', 'AWD', '310', '243.100,00')
carro3 = Carro('Toyota', 'Supra GT', '2021', '1.541 KG', 'RWD', '340', '240.050,00')

print('*' * 20)
time.sleep(0.3)
print('Seja bem-vindo a escolha do seu próximo carro dos sonhos')
time.sleep(1)
print('Hoje vou lhe ajudar nessa dificil missão pois as escolhas são excelentes !')
time.sleep(0.3)
print('Nós temos atualmente 3 modelos a pronta entrega..')
time.sleep(0.3)
print('Entre eles temos um (1) Jetta GLI, (2)Subaru WRX e (3) O Supra GT.')
time.sleep(0.3)
time.sleep(0.1)
print('*' * 20)

choice = ''
while '1' or '2' or '3' == choice:
    time.sleep(0.3)
    choice = input('Qual carro você gostaria de ver, (1), (2) ou (3) ?')

    if choice == '1':
        carro1.InformacoesCarro()
        resp = input('Você gostaria de ver outro modelo?').lower()
        if resp == 'não':
            break
        else:
            continue
    elif choice == '2':
        carro2.InformacoesCarro()
        resp = input('Você gostaria de ver outro modelo?').lower()
        if resp == 'não':
            break
        else:
            continue

    elif choice == '3':
        carro3.InformacoesCarro()
        resp = input('Você gostaria de ver outro modelo?').lower()
        if resp == 'não':
            break
        else:
            continue

    else:
        print('Não temos este modelo')
        resp = print('Você gostaria de ver outro modelo que nós temos?')
        if resp == 'não':
            break
        else:
            continue

#alteracao codigo teste #
