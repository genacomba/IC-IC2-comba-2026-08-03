### 🟢 A3 — Conversión de temperatura
#Pedí (o fijá) una temperatura en Celsius e imprimí su equivalente en Fahrenheit (`F = C * 9/5 + 32`).
#**Listo cuando:** 0 °C da 32 °F y 100 °C da 212 °F.
celsius= float(input("Ingrese la temperatura en Celsius: "))

fahrenheit = celsius * 9/5 + 32
print("La temperatura en Fahrenheit es:", fahrenheit)
