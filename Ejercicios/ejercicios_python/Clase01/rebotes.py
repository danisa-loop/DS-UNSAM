# rebotes.py
# Archivo de ejemplo
# Ejercicio

tirada = 1
alt = 100

while tirada <= 10:
    tirada = tirada + 1    
    alt = alt * 3/5
    round_alt = round(alt, 4)
    print(round_alt)