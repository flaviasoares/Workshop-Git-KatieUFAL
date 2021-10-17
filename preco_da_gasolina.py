quant_litros = float(input())
tipo_combustivel = input().upper()

if tipo_combustivel == "A":
    if quant_litros <= 20.0:
        desconto = quant_litros * 1.9 * 0.03
        total_pagar = quant_litros * 1.9 - desconto
    else:
        desconto = quant_litros * 1.9 * 0.05
        total_pagar = quant_litros * 1.9 - desconto

elif tipo_combustivel == "G":
    if quant_litros <= 20.0:
        desconto = quant_litros * 2.5 * 0.04
        total_pagar = quant_litros * 2.5 - desconto
    else:
        desconto = quant_litros * 2.5 * 0.06
        total_pagar = quant_litros * 2.5 - desconto

else:
    if quant_litros <= 25.0:
        total_pagar = quant_litros * 1.66
    else:
        desconto = quant_litros * 1.66 * 0.04
        total_pagar = quant_litros * 1.66 - desconto

print(f"R$ {total_pagar:.2f}")