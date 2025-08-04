#Calculadora mine

while True:
    print('='*30)
    option = int(input("Stack: \n[1] - 64 itens \n[2] - 16 itens\nOpção: "))
    if option in [1,2]:
        break
    else:
        print("Opção Invalida!")
while True:
    print('='*30)
    itens = int(input("Quantos itens ? "))
    resultado1 = resultado2 = 0
    if option == 1:
        if itens <= 64:
            print(f"{itens} itens")
        else:
            resultado1 = itens // 64 
            if itens % 64 != 0:
                resultado2 = itens - (resultado1 * 64) 
                print(f"{resultado1:.0f} Pack e {resultado2} itens")
            else:
                print(f"{resultado1} Pack")
    elif option == 2:
        if itens <= 16:
            print(f"{itens} itens")
        else:
            resultado1 = itens // 16 
            if itens % 16 != 0:
                resultado2 = itens - (resultado1 * 16) 
                print(f"{resultado1:.0f} Pack e {resultado2} itens")
            else:
                print(f"{resultado1} Pack")
    print('='*30)
    while True:
        continuar = str(input("Quer continuar[S/N] ou mudar stack[M]? ")).strip().upper()[0]
        if continuar in "SNM":
            break
    resultado1 = resultado2 = 0
    if continuar == "M":
        while True:
            print('='*30)
            option = int(input("Stack: \n[1] - 64 itens \n[2] - 16 itens\nOpção: "))
            if option in [1,2]:
                break
            else:
                print("Opção Invalida!")
    elif continuar == "N":
        break   