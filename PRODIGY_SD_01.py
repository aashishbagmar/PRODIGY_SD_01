print("Temperature Conversion")
temp = float(input("Enter temperature value: "))

Unit = input("Enter the unit (Celcius, Fahrenheit, Kelvin): ")

if Unit.lower() == "celsius":
    fahrenheit = round((temp * 1.8) + 32, 2)
    kelvin = round(temp + 273.15, 2)
    print(f"Temperature in Fahrenheit: {fahrenheit}")
    print(f"Temperature in Fahrenheit: {kelvin}")

elif Unit.lower() == "fahrenheit":
    Celsius = round(((temp - 32))*(5/9), 2)
    kelvin = round((temp - 32) * (5/9) + 273.15, 2)
    print(f"Temperature in Celsius: {Celsius}")
    print(f"Temperature in Kelvin: {kelvin}")

elif Unit.lower() == "kelvin":
    Celsius = round(temp - 273.15, 2)
    fahrenheit = round((temp - 273.15)*(9/5) + 32, 2)
    print(f"Temperature in Celsius: {Celsius}")
    print(f"Temperature in Fahrenheit: {fahrenheit}")

