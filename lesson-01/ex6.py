geo_type = input("Qual figura geométrica você quer calcular? 1 - Cilindro, 2 - Retângulo").strip()

if geo_type == '1':
    radius = float(input("Qual o raio do cilindro? "))
    height = float(input("Qual a altura do cilindro? "))

    area = 3.1415 * radius ** 2
    volume = 3.1415 * radius ** 2 * height
    print(f"A área do cilindro é: {area}. O volume é: {volume}")
elif geo_type == '2':
    base = float(input("Qual a base do retângulo? "))
    height = float(input("Qual a altura do retângulo? "))
    width = float(input("Qual a largura do retângulo"))

    area = height * width
    volume = base * height * width
    print(f"A área do retângulo é: {area}. O volume é: {volume}")
else:
    print("Forma geométrica inválida")