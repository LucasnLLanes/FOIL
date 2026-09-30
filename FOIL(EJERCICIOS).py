# ============================================================
# TRABAJO PRÁCTICO: ALGORITMO FOIL
# Autor: Lucas Nahuel Llanes
# Descripción: Implementación del algoritmo FOIL y cálculo
#              de la Ganancia FOIL sobre distintos atributos.
# ============================================================

import math


# ============================================================
# EJERCICIO 1: Inducción de regla FOIL
# Dataset: empleados en formación
# ============================================================

def ejercicio_1_induccion():
    """Induce una regla que distingue empleados en formación."""

    empleados = [
        {"edad": 22, "departamento": "IT",       "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 24, "departamento": "IT",       "nivel_educativo": "universitario", "en_formacion": True},
        {"edad": 21, "departamento": "RRHH",     "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 35, "departamento": "IT",       "nivel_educativo": "universitario", "en_formacion": False},
        {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría",      "en_formacion": False},
        {"edad": 29, "departamento": "RRHH",     "nivel_educativo": "universitario", "en_formacion": False},
        {"edad": 23, "departamento": "IT",       "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False},
    ]

    def inducir_regla(pos, neg):
        atributos = ["edad", "departamento", "nivel_educativo"]
        regla = {}

        for attr in atributos:
            v_pos = set(p[attr] for p in pos)
            v_neg = set(n[attr] for n in neg)

            if attr == "edad":
                validos = [v for v in v_pos if v not in v_neg]
            else:
                validos = list(v_pos - v_neg)

            if validos:
                regla[attr] = validos

        return regla

    casos_pos = [e for e in empleados if e["en_formacion"]]
    casos_neg = [e for e in empleados if not e["en_formacion"]]

    regla_final = inducir_regla(casos_pos, casos_neg)

    print("Regla inducida para identificar empleados en formación:")
    for k, v in regla_final.items():
        print(f"- {k} debe ser uno de: {v}")


# ============================================================
# EJERCICIO 2: Ganancia FOIL — atributo nivel_educativo
# Condición aplicada: nivel_educativo == "terciario"
# ============================================================

def ejercicio_2_ganancia_nivel_educativo():
    """Calcula la Ganancia FOIL para la condición nivel_educativo == terciario."""

    registros = [
        {"edad": 22, "departamento": "IT",       "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 24, "departamento": "IT",       "nivel_educativo": "universitario", "en_formacion": True},
        {"edad": 21, "departamento": "RRHH",     "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 35, "departamento": "IT",       "nivel_educativo": "universitario", "en_formacion": False},
        {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría",      "en_formacion": False},
        {"edad": 29, "departamento": "RRHH",     "nivel_educativo": "universitario", "en_formacion": False},
        {"edad": 23, "departamento": "IT",       "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False},
    ]

    def log_seguro(x):
        return math.log2(x) if x > 0 else float('-inf')

    P_total = sum(1 for r in registros if r["en_formacion"])
    N_total = sum(1 for r in registros if not r["en_formacion"])

    subconjunto = [r for r in registros if r["nivel_educativo"] == "terciario"]
    p_sub = sum(1 for r in subconjunto if r["en_formacion"])
    n_sub = sum(1 for r in subconjunto if not r["en_formacion"])

    ganancia = p_sub * (log_seguro(p_sub / (p_sub + n_sub)) - log_seguro(P_total / (P_total + N_total)))

    print(f"p = {p_sub}, n = {n_sub}")
    print(f"P = {P_total}, N = {N_total}")
    print(f"p / (p + n) = {p_sub / (p_sub + n_sub):.3f}")
    print(f"P / (P + N) = {P_total / (P_total + N_total):.3f}")
    print(f"log2(p / (p + n)) = {log_seguro(p_sub / (p_sub + n_sub)):.3f}")
    print(f"log2(P / (P + N)) = {log_seguro(P_total / (P_total + N_total)):.3f}")
    print(f"FOIL Gain = {ganancia:.3f}")


# ============================================================
# EJERCICIO 3: Ganancia FOIL — atributo edad
# Condición aplicada: edad <= 23
# ============================================================

def ejercicio_3_ganancia_edad():
    """Calcula la Ganancia FOIL para la condición edad <= 23."""

    base_datos = [
        {"edad": 22, "departamento": "IT",       "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 24, "departamento": "IT",       "nivel_educativo": "universitario", "en_formacion": True},
        {"edad": 21, "departamento": "RRHH",     "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 35, "departamento": "IT",       "nivel_educativo": "universitario", "en_formacion": False},
        {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría",      "en_formacion": False},
        {"edad": 29, "departamento": "RRHH",     "nivel_educativo": "universitario", "en_formacion": False},
        {"edad": 23, "departamento": "IT",       "nivel_educativo": "terciario",     "en_formacion": True},
        {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False},
    ]

    def log2_seguro(valor):
        return math.log2(valor) if valor > 0 else float('-inf')

    P = sum(1 for x in base_datos if x["en_formacion"])
    N = sum(1 for x in base_datos if not x["en_formacion"])

    menores_23 = [x for x in base_datos if x["edad"] <= 23]
    p = sum(1 for x in menores_23 if x["en_formacion"])
    n = sum(1 for x in menores_23 if not x["en_formacion"])

    foil_gain = p * (log2_seguro(p / (p + n)) - log2_seguro(P / (P + N)))

    print(f"p = {p}, n = {n}")
    print(f"P = {P}, N = {N}")
    print(f"p / (p + n) = {p / (p + n):.3f}")
    print(f"P / (P + N) = {P / (P + N):.3f}")
    print(f"log2(p / (p + n)) = {log2_seguro(p / (p + n)):.3f}")
    print(f"log2(P / (P + N)) = {log2_seguro(P / (P + N)):.3f}")
    print(f"FOIL Gain = {foil_gain:.3f}")


# ============================================================
# EJECUCIÓN DE LOS TRES EJERCICIOS
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("EJERCICIO 1: INDUCCIÓN DE REGLA FOIL")
    print("=" * 60)
    ejercicio_1_induccion()

    print()
    print("=" * 60)
    print("EJERCICIO 2: GANANCIA FOIL (nivel_educativo == 'terciario')")
    print("=" * 60)
    ejercicio_2_ganancia_nivel_educativo()

    print()
    print("=" * 60)
    print("EJERCICIO 3: GANANCIA FOIL (edad <= 23)")
    print("=" * 60)
    ejercicio_3_ganancia_edad()