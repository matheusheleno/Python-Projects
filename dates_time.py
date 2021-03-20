import datetime as dt


now = dt.datetime.now()
print(now)


data_escrita = now.strftime('%d-%B-%Y')

filename = 'arquivo.txt'

def create_time_file():
    with open(data_escrita, 'w') as file:
        file.write(str('Arquivo nomeado com sucesso!') + '\n')


create_time_file()