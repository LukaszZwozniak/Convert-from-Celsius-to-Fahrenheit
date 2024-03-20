def convert_celsius_to_fahrenheit(celsius_temps):
      fahrenheit_temps = list(map(lambda x: (9/5) * x + 32, celsius_temps))
      print(fahrenheit_temps)


convert_celsius_to_fahrenheit([-17, -9, -1, 0, 12, 25, 38])