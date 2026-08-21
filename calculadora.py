import soma
import subtrai
import multiplica
import divide


def main():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")

    if operador == "+":
        resultado = soma.somaf(n1, n2)
    elif operador == "-":
        resultado = subtrai.subtraif(n1, n2)
    elif operador == "*":
        resultado = multiplica.multiplicaf(n1, n2)
    elif operador == "/":
        resultado = divide.dividef(n1, n2)
    else:
        print("Operador inválido.")
        return

    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
