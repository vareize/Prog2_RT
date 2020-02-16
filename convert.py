# Imports
import tools_convert

# Fonctions
def celsius2fahrenheit(temperature_degré_celcius):
    res = temperature_degré_celcius
    res = (1.8*res)+32
    return res

def celsius2kelvin(temperature_degré_celcius):
    res = temperature_degré_celcius
    res += 273.15
    return res

# Programme principal
def main():
    temp = tools_convert.get_temperature()
    celsius = str(round(temp, 1))
    kelvin = str(round(celsius2kelvin(temp), 1))
    fahrenheit = str(round(celsius2fahrenheit(temp), 1))
    print('La température à Grenoble est de :')
    print('> ' + celsius + '°C')
    print('> ou de manière équivalente, ' + fahrenheit + '°F et ' + kelvin + '°K')

if __name__ == '__main__':
    main()
# Fin
