# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0
#
# O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum
# candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve
# retornar uma mensagem para votar novamente.
#
# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a
# quantidade de votos de cada candidato, os brancos e nulos
candidato_x = 0
candidato_y = 0
candidato_z = 0
nulo = 0
operacao = ""
vencedor = 0
while operacao != "s":
    operacao = (input("\nDigite o número do seu candidato ou aperte 's' para sair\n"))
    match operacao:
        case "889":
            print("Registro voto no Candidato X\n")
            candidato_x += 1
        case "847":
            print("Registro voto no Candidato Y\n")
            candidato_y += 1
        case "515":
            print("Registro voto no Candidato Z\n")
            candidato_z += 1
        case "0":
            print("Registro Voto em branco\n")
            nulo += 1
        case "s":
            print("Você encerrou o programa\n")
        case default:
            print("Por favor digite um candidato válido")


candidatos = ["Candidato X", "Candidato Y", "Candidato Z", "Brancos ou Nulos"]
resultado = [candidato_x, candidato_y, candidato_z, nulo]
resultado_semnulo = [candidato_x, candidato_y, candidato_z] #deixando a array acima apenas, poderia gerar resultado vencedor para nulos ou brancos
vencedor = candidatos[resultado.index(max(resultado_semnulo))]
total_votos = sum(resultado)



print("foram apurados", total_votos, "votos nesta eleição")
print("X obteve", candidato_x, "votos")
print("Y obteve", candidato_y, "votos")
print("Z obteve", candidato_z, "votos")
print(nulo, "votos foram brancos ou nulos")
print("O vencedor da eleição foi", vencedor)
