while True:
    try:
        nome = input("Digite seu nome: ")
        data_nascimento = int(input("Digite o ano em que nasceu: "))
        if data_nascimento < 1922 or data_nascimento > 2021:
            raise Exception("Software não desenvolvido para entidades paranormais. O ano de nascimento deve estar entre 1922 e 2021.")
        else:
            print(nome +", você tem atualmente ", 2022 - data_nascimento, " anos.")
            break
    except Exception as err:
        print("Ocorreu um erro inesperado: ", err)
        print("Tente novamente.")