print("Temperature Conversion")
temp = float(input("Enter temperature value: "))

Unit = input("Enter the unit (Celcius, Fahrenheit, Kelvin): ")

if Unit.lower() == "celsius":
    fahrenheit = (temp * 1.8) + 32
    kelvin = temp + 273.15
    print(f"Temperature in Fahrenheit: {fahrenheit}")
    print(f"Temperature in Fahrenheit: {kelvin}")

elif Unit.lower() == "fahrenheit":
    Celsius = ((temp - 32))*(5/9)
    kelvin = (temp - 32) * (5/9) + 273.15
    print(f"Temperature in Celsius: {Celsius}")
    print(f"Temperature in Kelvin: {kelvin}")

elif Unit.lower() == "kelvin":
    Celsius = temp - 273.15
    fahrenheit = (temp - 273.15)*(9/5) + 32
    print(f"Temperature in Celsius: {Celsius}")
    print(f"Temperature in Kelvin: {fahrenheit}")

