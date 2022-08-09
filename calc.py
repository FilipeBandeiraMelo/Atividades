def calculadora():
    operacao = ""
    while operacao != 0:
        operacao = int(input(
            "\nSelecione a operação desejada:\n\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair\n\n"))
        match operacao:
            case 1:
                print("\nSOMA\n")
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                print("Resultado: ", n1 + n2)
            case 2:
                print("\nSUBTRAÇÃO\n")
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                print("Resultado: ", n1 - n2)
            case 3:
                print("\nMULTIPLICAÇÃO\n")
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                print("Resultado: ", n1 * n2)
            case 4:
                print("\nDIVISÃO\n")
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                print("Resultado: ", n1 / n2)

            case 0:
                print("Conforme solicitado, o programa foi encerrado.")

            case default:
                print("Essa opção não existe:")
calculadora()
