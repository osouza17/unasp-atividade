while True:
    salario = float(input("Digite seu salário: "))
    cargo = input("Digite o nível do cargo: ")

    if cargo == "junior":
        novo_salario = salario * 0.10
    elif cargo == "pleno":
        novo_salario = salario * 0.20
    elif cargo == "senior":
        novo_salario = salario * 0.30
    else:
        print("Cargo não especificado. O salário permanecerá o mesmo.")
        novo_salario = salario
    filhos = input("Você tem filhos? ")
    if filhos == "sim":
        novo_salario += 500

    print(f"O meu salário é de R${salario:.2f}, mas com o meu cargo de {cargo}, meu novo salário será de R${novo_salario:.2f}!")

    exit = input("Deseja sair? (sim/não) ")
    if exit == "não":
        continue
    elif exit == "sim":
        break