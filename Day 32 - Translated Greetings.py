import random

# This is a simple project that translates the Romanian greeting "Salut" into 5 different languages.

salutInRomana = "Salut"
traducere_salut_in_5_limbi = ["Hello", "Salve", "Hola", "wah gwaan", "Hoi"]

salutTradus = random.randint(0, 4)
if salutTradus == 0:
    print(f"The Romanian greeting of {salutInRomana} is the equivalent of {traducere_salut_in_5_limbi[0]} in English")
elif salutTradus == 1:
    print(f"The Romanian greeting of {salutInRomana} is the equivalent of {traducere_salut_in_5_limbi[1]} in Italian")
elif salutTradus == 2:
    print(f"The Romanian greeting of {salutInRomana} is the equivalent of {traducere_salut_in_5_limbi[2]} in Spanish")
elif salutTradus == 3:
    print(f"The Romanian greeting of {salutInRomana} is the equivalent of {traducere_salut_in_5_limbi[3]} in Jamaican Patwah")
elif salutTradus == 4:
    print(f"The Romanian greeting of {salutInRomana} is the equivalent of {traducere_salut_in_5_limbi[4]} in Dutch")
