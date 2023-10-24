from Bank_account import BankAccount
i = 1
print("Introduce el número de cuenta y su balance correspondiente: ")
m = str(input())
n = int(input())
cuenta1 = BankAccount(m,n)
while i == 1:
    print("Que desea hacer: ")
    print("1. Añadir fondos: ")
    print("2. Retirar fondos: ")
    print("3. Pedir un préstamo: ")
    a = int(input())
    if a == 1:
        print("Introduce la cantidad que desea añadir", )
        b = int(input())
        cuenta1.add_funds(b)
        cuenta1.get_balance()
    if a == 2:
        print("Introduce la cantidad que desea retirar", )
        b = int(input())
        if b > cuenta1.get_balance():
            print("No hay saldo disponible ")
        else: 
            cuenta1.add_withdraws(b)
            cuenta1.get_balance()
    if a == 3:
        print("Introduce la cantidad del préstamo, y los meses que tardaría en devolverlo: ")
        c = int(input())
        x = int(input())
        d = x/12
        e = c * (((13**d)*1.25)/((13**d)-1))
        print(f"Pagarías {e/x}$ al mes, lo que significa que tendrías que pagar {e} en total")
    print("Desea continuar: ")
    print("1. Si: ")
    print("2. No: ")
    i = int(input())   
