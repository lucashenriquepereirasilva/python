media = float(input("Digite a nota media do aluno:"))

if media >= 6:

    print("Aluno com media {media} está aprovado")
elif media <= 4:
    print(" Aluno com media {media} está reprovado")
else:
    print("aluno com media {media} está em recuperação")