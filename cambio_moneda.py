monedas = {
    "usd": 1.09,
    "mxn": 21.62,
    "gbp": 0.83,
    "mad": 10.73
}

cant = int(input("Cantidad: "))
mon = input("Moneda: ")

if mon in monedas.keys():
    resultado = monedas[mon] * cant
    print(f"Resultado: {resultado}")