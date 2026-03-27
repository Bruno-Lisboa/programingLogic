dívida = float(input("Dívida: "))
juros = float(input("Taxa de juros mensal: "))
pago = float(input("Valor a pagar mensalmente: "))
meses = 1
jurosAcumulado = 0
totalPago = dívida

while dívida >= pago:
    if pago <= dívida * (juros/100):
        print("Processo Cancelado!")
        break
    else:
        dívida = (dívida + (dívida * (juros/100))) - pago
        print(f"Valor da dívida após pagamento de R${pago:.2f} no mês {meses}: R${dívida:.2f}")
        meses += 1
        jurosAcumulado += dívida * (juros/100)

if jurosAcumulado > 0:
    print(f" Parcelas: {meses - 1}")
    print(f" Juros: R${jurosAcumulado:.2f}")
    print(f" Preço Final: R${totalPago + jurosAcumulado:.2f}")
