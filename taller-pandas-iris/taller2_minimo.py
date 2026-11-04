import random
import statistics
import threading
import time


def generar_secuencias(n, longitud, semilla=2026):
    rng = random.Random(semilla)
    bases = "ACGT"
    return [
        "".join(rng.choices(bases, k=longitud))
        for _ in range(n)
    ]


def contenido_gc(secuencia):
    gc = secuencia.count("G") + secuencia.count("C")
    return 100 * gc / len(secuencia)


def analizar_gc(secuencias):
    return sum(contenido_gc(s) >= 55 for s in secuencias)


def analizar_atg(secuencias):
    return sum(s.count("ATG") for s in secuencias)


def analizar_tata(secuencias):
    return sum("TATA" in s for s in secuencias)


def analizar_longitud(secuencias):
    return sum(len(s) for s in secuencias)


def analizar_secuencial(secuencias):
    return {
        "gc_alto": analizar_gc(secuencias),
        "atg": analizar_atg(secuencias),
        "tata": analizar_tata(secuencias),
        "longitud_total": analizar_longitud(secuencias),
    }


def analizar_hebras(secuencias):
    resultados = {}
    candado = threading.Lock()

    def trabajar(clave, funcion):
        valor = funcion(secuencias)
        with candado:
            resultados[clave] = valor

    tareas = [
        ("gc_alto", analizar_gc),
        ("atg", analizar_atg),
        ("tata", analizar_tata),
        ("longitud_total", analizar_longitud),
    ]
    hebras = [threading.Thread(target=trabajar, args=tarea) for tarea in tareas]
    for hebra in hebras:
        hebra.start()
    for hebra in hebras:
        hebra.join()
    return resultados


def medir(funcion, datos):
    tiempos = []
    for _ in range(3):
        inicio = time.perf_counter()
        funcion(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def main():
    datos = generar_secuencias(20000, 400)
    esperado = analizar_secuencial(datos)
    obtenido = analizar_hebras(datos)
    print("Secuencial:", esperado)
    print("Hebras:", obtenido)
    assert obtenido == esperado

    ts = medir(analizar_secuencial, datos)
    tp = medir(analizar_hebras, datos)
    speedup = ts / tp
    print(f"Secuencial: {ts:.5f} s")
    print(f"Hebras: {tp:.5f} s")
    print("Trabajadores: 4")
    print(f"Speedup: {speedup:.3f}")
    print(f"Eficiencia: {speedup / 4:.3f}")


if __name__ == "__main__":
    main()
