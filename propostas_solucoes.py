import csv
import re
import unicodedata

# Abrir o arquivo, modo leitura
with open("cadastros.csv", "r", encoding='UTF-8') as arquivo:
    # Ler a tabela
    reader = csv.reader(arquivo, delimiter=",", quotechar='|')
    next(reader)
    # Navegar pela tabela
    for [nome, email, cpf, celular, idade, data_nascimento, data_cadastro] in reader:
        '{} - {} - {} - {} - {} - {}- {}'.format(nome, email, cpf, celular, idade, data_nascimento, data_cadastro)

        if len(str(nome)) > 25:
            nome_split = nome.split()

            maximo = len(nome_split) - 1
            nome_abreviado = ""
            for i in range(len(nome_split)):
                if i == 0:
                    nome_abreviado = nome_split[i]
                elif i == maximo:
                    if (len(nome_abreviado) + len(nome_split[i])) > 25:
                        nome_abreviado = nome_abreviado + " " + nome_split[i][0:1] + "."
                    else:
                        nome_abreviado = nome_abreviado + " " + nome_split[i]
                elif len(nome_split[i]) > 2:
                    nome_abreviado = nome_abreviado + " " + nome_split[i][0:1] + "."
                else:
                    nome_abreviado = nome_abreviado + " " + nome_split[i]
            print(f'Devido a ultrapassar a quantidade de caracteres permitidos '
                  f'o nome no formato desejado será {nome_abreviado}')

        pattern_cellular = '^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$'
        if re.match(pattern_cellular, celular) is None:
            celular = re.sub('[^0-9]', '', celular)
            telFormatado = '({}) {}-{}'.format(celular[0:2], celular[2:7], celular[7:])
            print(f'O formato correto do celular do usuario {nome} será {telFormatado}')

        format_string = ''.join(ch for ch in unicodedata.normalize('NFKD', nome) if not unicodedata.combining(ch))
        email_split = email.split('@')
        nome_email = format_string.split()
        nome_split = nome_email[0], '.', nome_email[-1]
        nome_join = ''.join(nome_split).lower()
        if not email_split[0] == nome_join:
            print(f'O email correto será {nome_join}@{email_split[-1]}')

        pattern_data = '^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(.|-|/)([1-9]|0[1-9]|1[0-2])(.|-|/)([0-9][0-9]|19[0-9][' \
                       '0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(.|-|/)([1-9]|0[1-9]|1[0-2])(' \
                       '.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$ '

        if re.match(pattern_data, data_nascimento) is None:
            data_nascimento = re.sub('[^0-9]', '', data_nascimento)
            data_nascimento_formatado = '{}/{}/{}'.format(data_nascimento[0:2], data_nascimento[2:4],
                                                          data_nascimento[4:8])
            print(f'A data de nascimento correta será {data_nascimento_formatado}')

        if re.match(pattern_data, data_cadastro) is None:
            data_cadastro = re.sub('[^0-9]', '', data_cadastro)
            data_cadastro_formatado = '{}/{}/{}'.format(data_cadastro[0:2], data_cadastro[2:4], data_cadastro[4:8])
            print(f'A data de cadastro correta será {data_nascimento_formatado}')
