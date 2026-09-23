from ast import parse


alunos = {}
menu = 0

def calc_media(notas):
    soma = 0
    for nota in notas.values():
        soma += float(nota)
    return soma / 4
    

while menu != 6:
    menu = int(input("\nEscolha uma opção: \n1-Add um novo aluno\n2-Remover um aluno\n3-Solicitar impressão da media de todos os alunos\n4-Solicitar Nome do aluno com maior media\n5-Listar todos os alunos\n6-Sair\n"))

    match menu:
        case 1:
            nome = input("Digite o nome do aluno: ")
            nota1 = input("Digite a nota 1: ")
            nota2 = input("Digite a nota 2: ")
            nota3 = input("Digite a nota 3: ")
            nota4 = input("Digite a nota 4: ")

            novo_aluno = {
                'nota1': nota1,
                'nota2': nota2,
                'nota3': nota3,
                'nota4': nota4,
            }

            alunos[nome] = novo_aluno
            # print

        case 2:
            aluno = input("\nDigite o nome do aluno que ira remover: ")

            if alunos.pop(aluno, None) is not None:
                print("\nAluno removido com sucesso!\n")
            else:
                print("\nAluno não encontrado!\n")

        case 3:
            print("\nMédias:")

            for aluno, notas in alunos.items():
                media = calc_media(notas)
                
                print(f"{aluno.title()}: {media:.2f}")

        case 4:
            print("Aluno com a maior média:")
            maior_media = 0
            aluno_maior_media = ""

            for nome, notas in alunos.items():
                media = calc_media(notas)

            if media > maior_media:
                maior_media = media
                aluno_maior_media = nome

            print(f"{aluno_maior_media.title()} com {maior_media} de média.")

        case 5:
            for aluno, notas in alunos.items():
                print(f"\nAluno: {aluno.title()}:")
                for titulo, nota in notas.items():
                    print(f"{titulo.title()}: {nota}")
                print("Media: ",calc_media(notas))

        case 6:
            break
    
        case _:
            print("Escolha uma opção válida")