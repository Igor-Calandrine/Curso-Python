# Verificar se um texto tem menos de 100 caracteres.

limite_caracteres = 300

texto = "A inteligência artificial transforma nosso mundo. Com avanços rápidos, ela impacta desde a medicina até a comunicação, otimizando processos e abrindo novas fronteiras. É uma era de inovações constantes."

caracteres = len(texto)
print(caracteres)

if caracteres <= limite_caracteres:
    print(f"O texto {texto} tem menos de {limite_caracteres} caracteres")
else:
    print(f"O texto tem mais de {limite_caracteres} caracteres")