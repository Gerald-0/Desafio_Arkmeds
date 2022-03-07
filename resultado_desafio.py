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

        # Condição para verificar quais nomes serao acima de 25 caracteres

        if len(str(nome)) > 25:
            print(f'\033[0;31m Erro! o nome do usuario {nome} está acima de 25 caracteres \033[m')

        # Variavel usando regex
        # Condição para verificar datas no formato desejado
        pattern_data = '^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(.|-|/)([1-9]|0[1-9]|1[0-2])(.|-|/)([0-9][0-9]|19[0-9][' \
                       '0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(.|-|/)([1-9]|0[1-9]|1[0-2])(' \
                       '.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$ '

        if re.match(pattern_data, data_nascimento) is None:
            print(
                f"\033[0;31m Erro! data de nascimento do {data_nascimento} usuario {nome} não é o formato desejado "
                f"dd/MM/YYYY\033[m")

        if re.match(pattern_data, data_cadastro) is None:
            print(f'\033[0;31m Erro! a data de cadastro {data_cadastro} está incorreta \033[m')

        # Condição para verificar formato desejado de cpf

        pattern_cpf = '^\d{3}.\d{3}.\d{3}-\d{2}$'
        if re.match(pattern_cpf, cpf) is None:
            print(f'\033[0;31m Erro! o cpf {cpf} é incorreto \033[m')

        # retira todos os caracteres especiais da string
        format_string = ''.join(ch for ch in unicodedata.normalize('NFKD', nome) if not unicodedata.combining(ch))
        email_split = email.split('@')
        nome_email = format_string.split()
        nome_split = nome_email[0], '.', nome_email[-1]
        nome_join = ''.join(nome_split).lower()
        # Verifica de a condicao é contraria ao formato desejado
        if not email_split[0] == nome_join:
            print(f'\033[0;31m Erro! o email {email} não segue a regra para o formato desejado \033[m')

        # Variavel para validar celular
        pattern_cellular = '^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$'
        # condicao para verificar celulares com erro no formato
        if re.match(pattern_cellular, celular) is None:
            print(f'\033[0;31m Erro! o celular {celular} do usuario {nome} é incorreto \033[m')
