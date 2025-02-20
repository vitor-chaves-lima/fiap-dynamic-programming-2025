weather = input("Qual é o clima: ").strip().lower()

if weather == "ensolarado":
    print("Dia de futebol e churrasco")
elif weather == "chuvoso":
    print("Dia de filme e série")
elif weather == "nublado":
    print("Dia de ler um livro")
elif weather == "nevando":
    print("Ótimo dia para tomar um café ou chocolate")
else:
    print("Não consegui entender")