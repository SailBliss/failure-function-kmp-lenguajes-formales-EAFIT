# failure.py
# Implementacion de la funcion de fallo (Figura 3.19)


def f_s(palabra):
    """
    Calcula f(1..n) para una palabra clave.
    Devuelve una lista con los valores de la funcion de fallo.
    """
    if palabra is None:
        raise ValueError("palabra no debe ser None")

    if palabra == "":
        return []

    n = len(palabra)

    #indices desde 1: b[1]..b[n]
    b = " " + palabra

    # Usamos f[1]..f[n], f[0] se ignora
    f = [0] * (n + 1)

    t = 0
    f[1] = 0

    for s in range(1, n):
        while t > 0 and b[s + 1] != b[t + 1]:
            t = f[t]
        if b[s + 1] == b[t + 1]:
            t = t + 1
            f[s + 1] = t
        else:
            f[s + 1] = 0

    return f[1:]


def f_s_table(palabra, values):
    if palabra == "":
        return "Palabra vacia !!!"

    n = len(palabra)
    s_row = "s:   " + " ".join(f"{i:>2}" for i in range(1, n + 1))
    f_row = "f(s) " + " ".join(f"{v:>2}" for v in values)
    return f"palabra: {palabra}\n{s_row}\n{f_row}"


def main():
    palabras = ["abababaab", "aaaaaa", "abbaabb"]

    for kw in palabras:
        values = f_s(kw)
        print(f_s_table(kw, values))
        print("-" * 50)


if __name__ == "__main__":
    main()
