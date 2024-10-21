import requests

# Función para obtener las tasas de cambio actualizadas
def obtener_tasas(base="USD"):
    url = f"https://v6.exchangerate-api.com/v6/71585e2274ffc21825359c38/latest/{base}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']
    else:
        print("Error al obtener las tasas de cambio")
        return None

# Función para mostrar un menú de monedas organizadas por país
def mostrar_menu_monedas(tasas):
    monedas_disponibles = {
        "Estados Unidos (USD)": "USD",
        "México (MXN)": "MXN",
        "Reino Unido (GBP)": "GBP",
        "Marruecos (MAD)": "MAD",
        # Agrega más países y monedas según la respuesta de la API
        "Eurozona (EUR)": "EUR",
        "Japón (JPY)": "JPY",
        "Canadá (CAD)": "CAD",
        "Suiza (CHF)": "CHF",
        "China (CNY)": "CNY"
    }
    
    print("\nMonedas disponibles:")
    for i, (pais, moneda) in enumerate(monedas_disponibles.items(), start=1):
        if moneda in tasas:
            print(f"{i}. {pais} - {moneda}")
    
    return monedas_disponibles

# Función para que el usuario elija la moneda por número
def seleccionar_moneda(monedas_disponibles):
    while True:
        try:
            seleccion = int(input("\nSelecciona el número de la moneda: "))
            monedas_lista = list(monedas_disponibles.values())
            if 1 <= seleccion <= len(monedas_lista):
                return monedas_lista[seleccion - 1]
            else:
                print("Selección no válida, intenta de nuevo.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")

# Función para convertir monedas
def convertir_moneda(cant, tasa_origen, tasa_destino):
    return (cant / tasa_origen) * tasa_destino

# Obtener las tasas de cambio desde USD
tasas = obtener_tasas()

if tasas:
    # Mostrar el menú de monedas disponibles
    monedas_disponibles = mostrar_menu_monedas(tasas)

    # Seleccionar la moneda de origen
    print("\n--- Moneda de origen ---")
    moneda_origen = seleccionar_moneda(monedas_disponibles)

    # Seleccionar la moneda de destino
    print("\n--- Moneda de destino ---")
    moneda_destino = seleccionar_moneda(monedas_disponibles)

    # Pedir cantidad a convertir
    cantidad = float(input("\nCantidad a convertir: "))

    # Verificar si las monedas seleccionadas existen en las tasas de cambio
    if moneda_origen in tasas and moneda_destino in tasas:
        tasa_origen = tasas[moneda_origen]
        tasa_destino = tasas[moneda_destino]

        # Convertir la cantidad
        resultado = convertir_moneda(cantidad, tasa_origen, tasa_destino)
        print(f"\n{cantidad} {moneda_origen} equivalen a {resultado:.2f} {moneda_destino}")
    else:
        print("Moneda no reconocida.")
else:
    print("No se pudieron obtener las tasas de cambio.")
