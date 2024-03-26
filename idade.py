age = int(input("Digite a idade: "))

if(age >= 0 and age <= 12) :
    print("Criança")
elif (age > 12 and age <= 18):
    print("Adolescente")
elif (age > 18):
    print("Adulto")
