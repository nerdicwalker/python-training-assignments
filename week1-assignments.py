# Welke operator gebruiken we voor optellen? En welke voor vermenigvuldigen, delen en
# machtsverheffen?

# optellen '+'
print(9+9)

# vermenigvuldigen '*'
print(9*9)

# machtsverheffen '^'
print(9**9)


# Stel we hebben een rechthoek met lengte 5 en breedte 3. 
# Gebruik een operator om de oppervlakte te berekenen en 
# druk het resultaat af op het scherm met print.

length = 5
width = 3
surface_area = length * width
print(f"De oppervlakte is: {surface_area}.")

# Stel we hebben een pizza met 8 punten en we willen die 
# verdelen onder 5 hardwerkende programmeurs. 
# Hoeveel pizza punten krijgt elke programmeur? 
# Gebruik een operator om het aantal pizza punten 
# te berekenen en druk het resultaat af op het scherm met print.

slices = 8 
programmers = 5
amount_of_pizza = slices / programmers
print(f"Iedere hardwerkende programmeur krijg: {amount_of_pizza} pizza punt.")

# Zo kunnen we bijvoorbeeld strings optellen / samenvoegen met de operator +.
# Type: print("Hello" + "World")

print("Hello" + "World") # output: HelloWorld

# Dat is nog niet ideaal: er ontbreekt een spatie tussen Hello en World. 
# Kun je het voorgaande commando aanpassen om wel een spatie tussen de 
# twee woorden te krijgen, 
# zonder de strings "Hello" en "World" zelf te veranderen?

print("Hello" + " World") # output: Hello World

# Een leuke truc is, om strings te vermenigvuldigen. 
# Stel: je hebt 100 uitroeptekens nodig. 
# Een echte programmeur is natuurlijk te lui om dat met de hand in te typen, 
# en wil dat automatiseren!
# Type: print(100 * "!")

print(100 * "!") # '!' (100 times)

# Strings beginnen en eindigen met quotes: "string". Dat is een probleem als er quotes
# in de string zelf voorkomen.
# 4. Probeer de volgende string te printen, inclusief de quotes om 
# "Python is leuk": Guido zei: "Python is leuk".
# print("Guido zei: "Python is leuk".") # SyntaxError: invalid syntax
print('Guido zei: "Python is leuk".')

# Hiermee is het probleem niet helemaal opgelost. 
# Wat nu, als je een string wil afdrukken met zowel enkele als dubbele quotes er in? 
# Dan kun je gebruik maken van een escape sequence door een backslash: \ voor een bijzonder 
# karakter te zetten.

print("Hello \nWorld!") # '\n' new line

# Een string is eigenlijk een serie letters. Soms wil je één bepaalde letter uit een string 
# gebruiken. Dat kan door achter de string het nummer van de gewenste letter in 
# blokhaken: [ ] te zetten. De letters worden van links naar rechts geteld vanaf 0. Probeer maar:
# print( "hallo"[0] ) geeft: h print( "hallo"[1] ) geeft: a
# 1. Pas het onderstaande commando aan om te zorgen dat er een kleine letter e wordt geprint:

print("Python4Ever"[9])

# We kunnen de twee datatypes int en string naar elkaar omzetten met de functies: int en str. 
# We hebben al eerder een functie gebruikt, namelijk print. Net als bij print geven we de 
# benodigde informatie mee tussen haakjes: ( ). Probeer maar:
# int( "216") geeft: 216 str( 216 ) geeft: '216'
# We kunnen in principe van elke int een string maken, maar kun je ook van elke string een int maken?
# 1. Bekijk de volgende twee commando’s 
print( int("4") + int("2") )
print( str(4) + str(2) )


