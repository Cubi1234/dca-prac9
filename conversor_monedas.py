moneda=input('¿Que tipo de moneda quieres convertir? ')

if moneda == ('euro'):
    cantidad=int(input('Dime la cantidad de dinero que quieres convertir '))
    conversion=input('¿A que moneda lo quieres convertir? ')
    if conversion == ('dolar'):
        resultado_conversion = cantidad*1.18
        print(cantidad, '€ en $ son ', resultado_conversion, '$')
    if conversion == ('peso dominicano'):
        resultado_conversion = cantidad*67.34
        print(cantidad, '€ en RD$ son', resultado_conversion, 'RD$')
    if conversion == ('yen'):
        resultado_conversion=cantidad*138.91
        print(cantidad, '€ en ¥ son ', resultado_conversion, '¥')
    if conversion == ('libra'):
        resultado_conversion=cantidad*0.89
        print(cantidad, '€ en £ son ', resultado_conversion, '£')
    if conversion == ('rupia'):
        resultado_conversion=cantidad*78.73
        print(cantidad, '€ en ₹ son ', resultado_conversion, '₹')
 
elif moneda == ('dolar'):
    cantidad=int(input('Dime la cantidad de dinero que quieres convertir '))
    conversion=input('¿A que moneda lo quieres convertir? ')
    if conversion == ('euro'):
        resultado_conversion = cantidad*0.85
        print(cantidad, '$ en € son', resultado_conversion, '€')
    if conversion == ('yen'):
        resultado_conversion=cantidad*143.34
        print(cantidad, '$ en ¥ son ', resultado_conversion, '¥')
    if conversion == ('libra'):
        resultado_conversion=cantidad*0.92
        print(cantidad, '$ en £ son ', resultado_conversion, '£')
    if conversion == ('rupia'):
        resultado_conversion=cantidad*81.24
        print(cantidad, '$ en ₹ son ', resultado_conversion, '₹')
    if conversion == ('peso dominicano'):
        resultado_conversion = cantidad*53.45
        print(cantidad, '$ en RD$ son', resultado_conversion, 'RD$')
 
elif moneda == ('peso dominicano'):
    cantidad=int(input('Dime la cantidad de dinero que quieres convertir '))
    conversion=input('¿A que moneda lo quieres convertir? ')
    if conversion == ('euro'):
        resultado_conversion = cantidad*0.015
        print(cantidad, 'RD$ en € son', resultado_conversion, '€')
    if conversion == ('yen'):
        resultado_conversion=cantidad*2.68
        print(cantidad, 'RD$ en ¥ son ', resultado_conversion, '¥')
    if conversion == ('libra'):
        resultado_conversion=cantidad*0.017
        print(cantidad, 'RD$ en £ son ', resultado_conversion, '£')
    if conversion == ('rupia'):
        resultado_conversion=cantidad*1.52
        print(cantidad, 'RD$ en ₹ son ', resultado_conversion, '₹')
    if conversion == ('dolar'):
        resultado_conversion = cantidad*0.019
        print(cantidad, 'RD$ en $ son ', resultado_conversion, '$')
        
elif moneda == ('yen'):
    cantidad = int(input("Dime la cantidad de dinero que quieres invertir "))
    conversion=input('¿A que moneda lo quieres convertir? ')
    if conversion == ('euro'):
        resultado_conversion = cantidad/138.91
        print(cantidad, '¥ en € son', resultado_conversion, '€')
    if conversion == ('libra'):
        resultado_conversion=cantidad*0.0064
        print(cantidad, '¥ en £ son ', resultado_conversion, '£')
    if conversion == ('rupia'):
        resultado_conversion=cantidad*0.57
        print(cantidad, '¥ en ₹ son ', resultado_conversion, '₹')
    if conversion == ('dolar'):
        resultado_conversion = cantidad*0.007
        print(cantidad, '¥ en $ son ', resultado_conversion, '$')
    if conversion == ('peso dominicano'):
        resultado_conversion = cantidad*0.37
        print(cantidad, '¥ en RD$ son', resultado_conversion, 'RD$')

elif moneda == ('libra'):
    cantidad=int(input("Dime la cantidad de dinero que quieres invertir "))
    conversion=input('¿A que moneda lo quieres convertir? ')
    if conversion == ('euro'):
        resultado_conversion = cantidad/0.89
        print(cantidad, '£ en € son', resultado_conversion, '€')
    if conversion == ('rupia'):
        resultado_conversion=cantidad*88.21
        print(cantidad, '£ en ₹ son ', resultado_conversion, '₹')
    if conversion == ('dolar'):
        resultado_conversion = cantidad*1.09
        print(cantidad, '£ en $ son ', resultado_conversion, '$')
    if conversion == ('peso dominicano'):
        resultado_conversion = cantidad*58.04
        print(cantidad, '£ en RD$ son', resultado_conversion, 'RD$')
    if conversion == ('yen'):
        resultado_conversion=cantidad*156.04
        print(cantidad, '£ en ¥ son ', resultado_conversion, ¥)

elif moneda == ('rupia'):
    cantidad=int(input("Dime la cantidad de dinero que quieres invertir "))
    conversion=input('¿A que moneda lo quieres convertir? ')
    if conversion == ('euro'):
        resultado_conversion = cantidad/78.73
        print(cantidad, '₹ en € son', resultado_conversion, '€')
    if conversion == ('dolar'):
        resultado_conversion = cantidad*0.012
        print(cantidad, '₹ en $ son ', resultado_conversion, '$')
    if conversion == ('peso dominicano'):
        resultado_conversion = cantidad*0.66
        print(cantidad, '₹ en RD$ son', resultado_conversion, 'RD$')
    if conversion == ('yen'):
        resultado_conversion=cantidad*1.76
        print(cantidad, '₹ en ¥ son ', resultado_conversion, '¥')
    if conversion == ('libra'):
        resultado_conversion=cantidad*0.0011
        print(cantidad, '₹ en £ son ', resultado_conversion, '£')
        
else:
    print('Esa moneda no está registrada')
