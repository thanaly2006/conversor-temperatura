# Perguntar ao usuário qual a temperatura e a unidade de origem

temperatura = float(input("Digite a temperatura que deseja converter: "))

unidade_origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ").lower()


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


if unidade_origem == "celsius":
    print(f"{temperatura} °C equivale a {celsius_para_fahrenheit(temperatura)} °F")
    print(f"{temperatura} °C equivale a {celsius_para_kelvin(temperatura)} K")

elif unidade_origem == "fahrenheit":
    print(f"{temperatura} °F equivale a {fahrenheit_para_celsius(temperatura)} °C")
    print(f"{temperatura} °F equivale a {fahrenheit_para_kelvin(temperatura)} K")

elif unidade_origem == "kelvin":
    print(f"{temperatura} K equivale a {kelvin_para_celsius(temperatura)} °C")
    print(f"{temperatura} K equivale a {kelvin_para_fahrenheit(temperatura)} °F")

else:
    print("Unidade de origem inválida. Escolha entre Celsius, Fahrenheit ou Kelvin.")
