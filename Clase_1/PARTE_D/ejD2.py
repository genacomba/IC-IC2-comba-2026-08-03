### 🟡 D2 — ¿Aprobó?
#Escribí `aprobo(notas)` que use `promedio()` por dentro y devuelva `True`/`False`.
#**Listo cuando:** una función usa a la otra (las funciones se combinan).

def promedio(notas):
    total= 0 
    for nota in notas:
        total = total + nota

    return total / len(notas)

def aprobo(notas):
    if promedio(notas) >= 6:
        return True
    else:
        return False
notas_genaro = [4,8,7,6,2,10]
notas_juan = [5,6,3,2]
print(aprobo(notas_genaro))
print(aprobo(notas_juan))
