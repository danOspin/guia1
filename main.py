# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = 10
    b = -5
    c = "Hola "
    d = [1, 2, 3]

    print(a * 5)
    print(a - b)
    print(c + "Mundo")
    print(c * 2)
    print(d + d)
    print((c + "mundo") * 5)

    nota_1 = 0
    nota_2 = 5
    nota_3 = 1.1
    nota_final = (nota_1 + nota_2 + nota_3) / 3
    print("Su nota final es: " + str(nota_final))

    Lista = []
    Lista.append(nota_1)
    Lista.append(nota_2)
    Lista.append(nota_3)
    print(Lista)

    arroz = 12500
    papa = 23000
    harina = 5300

    total = arroz + papa + harina
    iva = total * 0.19
    print('Debe pagar un total de : {2}, consistente en una suma de productos de {0} y un iva de {1}'.format(total, iva, total + iva))

    numero_1 = int("9")
    numero_2 = int("3")
    numero_3 = int("6")

    media = (numero_1 + numero_2 + numero_3) / 3
    print("La nota media es", media)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
