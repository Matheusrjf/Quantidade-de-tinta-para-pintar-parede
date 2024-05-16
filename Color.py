def main():
    # Entrada de dados
    comprimento = float(input("Digite o comprimento do cômodo em metros: "))
    largura = float(input("Digite a largura do cômodo em metros: "))
    altura = float(input("Digite a altura do cômodo em metros: "))
    demaos = int(input("Digite a quantidade de demãos desejada: "))
    cobertura_por_litro = float(input("Digite a cobertura da tinta por litro em metros quadrados: "))

    # Chamada da função para calcular a quantidade de tinta necessária
    quantidade_necessaria = calcular_quantidade_de_tinta(comprimento, largura, altura, demaos, cobertura_por_litro)

    # Saída de resultados
    print("Você precisará de", quantidade_necessaria, "litros de tinta para pintar o cômodo.")

if __name__ == "__main__":
    main()
