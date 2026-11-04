# Formulario / chuleta de Python y bioinformática

Resumen de consulta. Para aprender cada concepto desde cero, lee `Guia_desde_cero.md`. Las implementaciones de los cinco ejercicios están en `practica_bioinformatica.py`.

## 1. Archivo y ejecución

Guardar como texto UTF-8 con extensión `.py`, sin `.txt` al final. Desde la terminal, en la carpeta del archivo:

```powershell
python inicio.py
python practica_bioinformatica.py
python practica_bioinformatica.py --medir
```

La última orden mide y guarda `mediciones.json`. No escribas estas órdenes dentro de un archivo Python ni tras el indicador `>>>`.

## 2. Sintaxis que debes reconocer

| Necesito… | Escribo… |
|---|---|
| Comentar | `# explicación` |
| Guardar un valor | `s = "ATGC"` |
| Mostrar | `print(s)` |
| Medir longitud | `len(s)` |
| Contar una letra | `s.count("G")` |
| Comparar | `gc >= 50`, `n == 0` |
| Combinar condiciones | `s != "" and "N" not in s` |
| Obtener primer elemento | `datos[0]` |
| Dividir en mitades | `medio = len(datos) // 2` |
| Tomar izquierda/derecha | `datos[:medio]`, `datos[medio:]` |
| Acumular | `total += valor` |
| Añadir a lista | `resultados.append(valor)` |
| Leer diccionario | `informe["gc_alto"]` |
| Importar | `import threading` |
| Comprobar igualdad | `assert obtenido == esperado` |

`=` asigna; `==` compara. `:` inicia un bloque; usa cuatro espacios de sangría. El extremo derecho de un corte no se incluye. `len(secuencias)` cuenta secuencias; `len(s)` cuenta bases de una secuencia.

```python
def funcion(entrada):
    resultado = len(entrada)
    return resultado

for s in secuencias:
    if len(s) > 0:
        print(funcion(s))
```

`def` define; `funcion(...)` llama; `return` devuelve; `print` muestra. `int(True)=1`; `int(False)=0`. Una función sin `return` devuelve `None`.

## 3. Cuatro cálculos básicos

Supuesto: secuencias válidas, no vacías y en mayúsculas. Una colección vacía sí es válida para los agregados y produce cero.

```python
def contenido_gc(s):
    return 100 * (s.count("G") + s.count("C")) / len(s)

def contar_gc_alto(secuencias, umbral=50):
    return sum(contenido_gc(s) >= umbral for s in secuencias)

def contar_motivo(secuencias, motivo="ATG"):
    if not motivo:
        raise ValueError("Motivo vacío")
    return sum(s.count(motivo) for s in secuencias)

def longitud_total(secuencias):
    return sum(len(s) for s in secuencias)
```

**GC (%) = 100 × (G + C) / longitud.** GC alto incluye exactamente 50 %. Motivos: aquí SIN solapamiento, dentro de cada secuencia. `"AAAA".count("AA")` es `2`; con solapamiento serían `3`.

Lista del ZIP: `ATGC, GGCC, ATAT, CGCG, TTAA, GCTA, CCCC, AATT`.

Resultados de control: **5 secuencias con GC alto; 1 ATG; 32 nucleótidos**. Conteos de GC por mitades: `3 + 2 = 5`.

## 4. Conceptos y dependencias

| Concepto | Pregunta que responde |
|---|---|
| Descomposición | ¿En qué tareas divido el problema? |
| Dependencia | ¿Qué resultado necesita esta tarea para empezar? |
| Por funciones | ¿Qué operaciones diferentes puedo asignar? |
| Por datos | ¿Qué grupos reciben la misma operación? |
| Concurrencia | ¿Pueden progresar varias tareas durante un intervalo? |
| Paralelismo | ¿Se ejecutan efectivamente al mismo tiempo? |
| Recursión | ¿Resuelvo una instancia mediante llamadas a instancias menores? |

```text
Datos -> Validación -> {GC alto | Motivo | Longitud} -> Informe
```

Compartir datos de solo lectura no implica dependencia entre los análisis. La validación debe precederlos; el informe espera los tres resultados. Independencia permite paralelismo, pero no lo garantiza.

## 5. Hebras y procesos

| Aspecto | Hebras (`threading.Thread`) | Procesos (`multiprocessing.Process`) |
|---|---|---|
| Memoria | Compartida en el proceso | Espacios separados |
| Resultado | Objeto compartido y coordinación | Mensajes por `multiprocessing.Queue` |
| Inicio | Generalmente menor costo | Generalmente mayor costo |
| CPU | Depende del GIL y del código ejecutado | Pueden usar varios núcleos |
| Riesgo típico | Carrera sobre estado compartido | Copias, comunicación y espera de mensajes |

Orden correcto: **crear -> iniciar TODOS -> esperar/recibir -> combinar**.

```python
h = threading.Thread(target=trabajador, args=(datos,))
h.start()
h.join()
```

`target` recibe el nombre de la función, sin llamarla. `(datos,)` necesita la coma. `join()` espera, no obtiene el valor retornado. En procesos, `cola.put(...)` envía y `cola.get()` recibe. Etiquetar mensajes evita confundir el orden de llegada. Recibir mensajes antes de esperar a los procesos evita problemas con colas pendientes.

Funciones de procesos: a nivel del archivo. Arranque:

```python
if __name__ == "__main__":
    main()
```

GIL: la versión por sí sola no basta. La guía pide Python 3.15 free-threaded con GIL deshabilitado:

```python
import sys
import sysconfig
print(sys.version)
print(sysconfig.get_config_var("Py_GIL_DISABLED"))  # soporte: 1
print(sys._is_gil_enabled())                       # activo: False
```

La ejecución de comprobación entregada se hizo en Python 3.14.7 **con GIL habilitado**. No demuestra el rendimiento en 3.15 sin GIL. [Referencia oficial](https://docs.python.org/3/howto/free-threading-python.html).

## 6. Recursión por mitades

```python
def contar_gc_recursivo(secuencias):
    if len(secuencias) == 0:
        return 0
    if len(secuencias) == 1:
        return int(contenido_gc(secuencias[0]) >= 50)
    medio = len(secuencias) // 2
    izq = contar_gc_recursivo(secuencias[:medio])
    der = contar_gc_recursivo(secuencias[medio:])
    return izq + der
```

Tres requisitos: **caso base**, **reducción del problema**, **combinación**. Las llamadas hermanas son independientes; el padre espera ambas. Este código sigue siendo secuencial.

Para el ejercicio 4: crear **exactamente dos trabajadores en la división superior**. Cada trabajador ejecuta recursión secuencial. No crear trabajadores dentro de la función recursiva.

Los cortes crean listas de referencias: cuestan tiempo y memoria. Alternativa: misma lista más índices `inicio`, `fin`; evitar sublistas. No elimina automáticamente copias entre procesos.

## 7. Fórmulas de rendimiento

| Fórmula | Interpretación |
|---|---|
| `S = Ts / Tp` | Aceleración: mayor que 1 mejora; menor que 1 empeora |
| `E = S / p` | Eficiencia; `100 * E` da el porcentaje |
| `O = p * Tp - Ts` | Overhead definido por la guía |

`Ts` y `Tp`: medianas en segundos. `p`: trabajadores creados, no núcleos observados ni trabajadores más principal. En ejercicios 2, 3 y el pipeline funcional: `p=3`; en las ramas del ejercicio 4: `p=2`.

```python
inicio = time.perf_counter()
resultado = analizar_hebras(datos)
duracion = time.perf_counter() - inicio
```

Datos generados antes; impresión y `assert` después. Incluir creación, comunicación, sincronización y combinación. Ejercicio 3: `2000`, `20000`, `80000`, longitud `400`, mínimo cinco repeticiones por versión/tamaño. Usar mediana y registrar entorno.

Ejemplo hipotético: `Ts=12`, `Tp=5`, `p=3` -> `S=2.4`, `E=0.8`, `O=3`.

## 8. Qué entregar en cada ejercicio

| Ejercicio | Producto y comprobación |
|---|---|
| 1 | Tres operaciones, diccionario secuencial, grafo, comparación por funciones/datos |
| 2 | Tres hebras y tres procesos con cola; `assert`; diagramas de memoria; sincronización y elección justificada |
| 3 | Tres tamaños × tres versiones × cinco repeticiones; medianas, S, E, O; interpretar GIL y carga desigual |
| 4 | Recursión; árbol de ocho; dos hebras y dos procesos solo arriba; igualdad; costos de cortes y alternativa con índices |
| 5 | Validación -> análisis -> informe; dos versiones; igualdad; dos tamaños; métricas; dos riesgos y controles |

Restricción del ejercicio 2: **no usar ThreadPoolExecutor ni ProcessPoolExecutor**.

## 9. Método para resolver sin perderse

1. Escribe qué entra y qué debe salir.
2. Declara supuestos: vacías, caracteres válidos, mayúsculas, solapamiento.
3. Calcula un ejemplo pequeño a mano.
4. Implementa secuencial y comprueba.
5. Dibuja qué tarea necesita a cuál.
6. Introduce trabajadores y espera correctamente.
7. Comprueba igualdad antes de medir.
8. Explica el resultado observado sin generalizar a otros equipos o configuraciones.

Recordatorio: **dividir no ejecuta; recursión no paraleliza; más trabajadores no asegura menos tiempo**.
