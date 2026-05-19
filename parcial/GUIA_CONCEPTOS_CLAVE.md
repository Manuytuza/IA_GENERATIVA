# 📚 GUÍA DE CONCEPTOS CLAVE - EXAMEN PYTHON

---

## 🎯 PARTE P1: MANEJO DE ARCHIVOS CSV SIN PANDAS

### ❌ ERRORES COMUNES:

```python
# ❌ MALO: No cierra el archivo
f = open('datos.csv', 'r')
reader = csv.reader(f)

# ✅ CORRECTO: Se cierra automáticamente
with open('datos.csv', 'r') as f:
    reader = csv.reader(f)
```

### ✅ FORMA CORRECTA: Leer CSV

```python
import csv

# Leer el archivo
with open('datos.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)  # fila es una lista
```

**Puntos clave:**
- `with` cierra automáticamente el archivo
- `csv.reader()` retorna filas como LISTAS
- `encoding='utf-8'` para caracteres especiales
- `.newline=''` es crítico en Windows

### ✅ FORMA CORRECTA: Escribir CSV (append)

```python
import csv

nuevas_filas = [
    ['32550', '32', 'Private', ...],
    ['32551', '43', 'Private', ...],
]

# APPEND: agregar sin borrar
with open('datos.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for fila in nuevas_filas:
        writer.writerow(fila)  # UNA fila
        
    # O todas a la vez:
    # writer.writerows(nuevas_filas)  # VARIAS filas
```

**Modos de apertura:**
- `'r'` → leer
- `'w'` → escribir (borra todo antes)
- `'a'` → append (agrega al final)
- `'newline=''` → obligatorio en CSV para evitar líneas dobles en Windows

### ✅ VERIFICACIÓN: Contar filas

```python
# Contar total de filas en un CSV
with open('datos.csv', 'r') as f:
    reader = csv.reader(f)
    total = sum(1 for _ in reader)  # Itera sin cargar todo en memoria
    print(f"Total de filas: {total}")
```

---

## 📊 PARTE P2: ANÁLISIS CON PANDAS

### ✅ CARGACIÓN Y ESTRUCTURA

```python
import pandas as pd

# Cargar CSV
df = pd.read_csv('datos.csv')

# Verificar estructura
print(df.shape)           # (filas, columnas)
print(df.columns)         # Nombres de columnas
print(df.dtypes)          # Tipos de datos
print(df.head())          # Primeras filas
print(df.tail())          # Últimas filas
```

### ✅ ELIMINAR COLUMNAS

```python
# Si hay columna Unnamed: 0 (copia del índice)
df = df.drop('Unnamed: 0', axis=1)

# Verificar el cambio
print(df.shape)
print(df.columns)
```

### ✅ FILTRAR FILAS (por condición)

```python
# Filtrar hombres (note: puede haber espacios ' Male')
hombres = df[df['sex'].str.strip() == 'Male']

# Filtrar por edad
mayores_30 = df[df['age'] > 30]

# Múltiples condiciones
condicion = (df['age'] > 30) & (df['sex'].str.strip() == 'Male')
resultado = df[condicion]
```

**Importante:** `.str.strip()` elimina espacios antes/después

### ✅ CALCULAR PROMEDIOS

```python
# Promedio simple
edad_promedio = df['age'].mean()

# Promedio por grupo (filtrado)
hombres = df[df['sex'].str.strip() == 'Male']
edad_promedio_hombres = hombres['age'].mean()

# Con 2 decimales
edad_redondeada = round(edad_promedio, 2)
# O
edad_formateada = f"{edad_promedio:.2f}"
```

### ✅ CONTAR Y CALCULAR PORCENTAJES

```python
# Contar registros que cumplen condición
cubanos = (df['country'].str.strip() == 'Cuba').sum()
total = len(df)
porcentaje = (cubanos / total) * 100

print(f"El porcentaje de cubanos es: {porcentaje:.2f}%")
```

**Nota:** `.sum()` en una máscara booleana cuenta True como 1, False como 0

### ✅ GROUPBY Y AGREGACIÓN

```python
# Agrupar y contar
conteos = df['income'].value_counts()
print(conteos)

# Agrupar y calcular promedio
promedio_por_grupo = df.groupby('income')['age'].mean()
```

---

## 📈 PARTE PE1: GRÁFICO PIE

```python
import matplotlib.pyplot as plt

# Contar categorías
conteos = df['income'].value_counts()

# Crear gráfico
plt.figure(figsize=(8, 6))
plt.pie(conteos.values,
        labels=[x.strip() for x in conteos.index],  # Limpiar espacios
        autopct='%1.1f%%',                          # Mostrar porcentajes
        colors=['#ff9999', '#66b3ff'])              # Colores personalizados
        
plt.title('Título del gráfico')
plt.axis('equal')  # Para que sea círculo (no elipse)
plt.tight_layout()
plt.show()
```

**Puntos clave:**
- `.value_counts()` cuenta ocurrencias automáticamente
- `autopct='%1.1f%%'` muestra 1 decimal
- `.strip()` limpia espacios en los labels
- `axis='equal'` hace que sea círculo perfecto

---

## 🎲 PARTE PE2: SIMULACIÓN MONEDA TRUCADA

```python
import numpy as np

# Parámetros
np.random.seed(42)  # Para reproducibilidad
num_lanzamientos = 50
prob_cara = 0.7

# Simular: 1=cara (70% probable), 0=cruz (30% probable)
lanzamientos = np.random.binomial(n=1, p=0.7, size=50)
# Resultado: [1, 0, 1, 1, 0, ...]

# Análisis
total_caras = lanzamientos.sum()           # Contar 1s
porcentaje = (total_caras / 50) * 100
print(f"Caras: {total_caras}, Porcentaje: {porcentaje:.2f}%")

# Gráfico: mostrar convergencia a 70%
caras_acumuladas = np.cumsum(lanzamientos)  # Suma acumulada
porcentaje_acumulado = (caras_acumuladas / np.arange(1, 51)) * 100

plt.figure(figsize=(12, 6))
plt.plot(range(1, 51), porcentaje_acumulado, marker='o')
plt.axhline(y=70, color='red', linestyle='--', label='70% esperado')
plt.xlabel('Lanzamiento')
plt.ylabel('Porcentaje de caras (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Conceptos:**
- `np.random.binomial(n, p, size)` → simula n pruebas con probabilidad p, size veces
- `np.cumsum()` → suma acumulada (ver la convergencia)
- `np.arange()` → crea array de índices para dividir

---

## 🔢 PARTE PE3: PRIMOS DE MERSENNE

### Definición

Un **primo de Mersenne** es un número que:
1. **Es primo** (solo divisible por 1 y por sí mismo)
2. **Se expresa como 2^p - 1** donde p también es primo

### Ejemplos

```
2:  NO es Mersenne (2^p - 1 nunca da 2 con p primo)
3:  SÍ es Mersenne (3 = 2^2 - 1, donde 2 es primo)
5:  NO es Mersenne (5 ≠ 2^p - 1 para ningún p primo)
7:  SÍ es Mersenne (7 = 2^3 - 1, donde 3 es primo)
31: SÍ es Mersenne (31 = 2^5 - 1, donde 5 es primo)
```

### Código solución

```python
def es_primo(n):
    """Verifica si n es primo"""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def encontrar_mersenne(limite):
    """Encuentra primos de Mersenne < limite"""
    resultado = []
    
    # Para cada número primo menor al límite
    for candidato in range(2, limite):
        if not es_primo(candidato):
            continue
        
        # Buscar p primo tal que 2^p - 1 = candidato
        p = 2
        while True:
            valor_mersenne = (2 ** p) - 1
            
            if valor_mersenne > candidato:
                break
            
            if valor_mersenne == candidato and es_primo(p):
                resultado.append((candidato, p))
                break
            
            p += 1
            while not es_primo(p):
                p += 1
    
    return resultado

# Ejecutar
mersenne = encontrar_mersenne(100)
for numero, p in mersenne:
    print(f"{numero} = 2^{p} - 1")
    
# Resultado esperado:
# 3 = 2^2 - 1
# 7 = 2^3 - 1
# 31 = 2^5 - 1
```

---

## 🚨 ERRORES MÁS COMUNES EN EL EXAMEN

### 1. ❌ Olvidar `.strip()` al filtrar

```python
# ❌ INCORRECTO: Los espacios causan fallos
hombres = df[df['sex'] == ' Male']  # No encuentra nada si está ' Male'

# ✅ CORRECTO
hombres = df[df['sex'].str.strip() == 'Male']
```

### 2. ❌ Modo de apertura de archivo

```python
# ❌ INCORRECTO: Crea líneas dobles en Windows
with open('datos.csv', 'a') as f:
    writer = csv.writer(f)
    
# ✅ CORRECTO
with open('datos.csv', 'a', newline='') as f:
    writer = csv.writer(f)
```

### 3. ❌ Confundir csv.reader vs csv.DictReader

```python
# csv.reader: retorna LISTAS
with open('datos.csv') as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila[0])  # Acceso por índice

# csv.DictReader: retorna DICCIONARIOS
with open('datos.csv') as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(fila['nombre'])  # Acceso por clave
```

### 4. ❌ Dividir por 0

```python
# ❌ Si cubanos_count es 0, este da ZeroDivisionError
porcentaje = (cubanos_count / total) * 100

# ✅ Siempre verificar
if total > 0:
    porcentaje = (cubanos_count / total) * 100
```

### 5. ❌ Comparación de números como strings

```python
# ❌ INCORRECTO: '32' > 30 causa TypeError
if df['age'] > 30:  # age debe ser numérico

# ✅ CORRECTO: asegurarse que es numérico
df['age'] = df['age'].astype(int)
if df['age'] > 30:
```

---

## 📋 CHECKLIST ANTES DE ENTREGAR

- [ ] **P1.1**: Archivo se lee correctamente con `with`
- [ ] **P1.2**: Se agregaron exactamente 10 filas (verificadas)
- [ ] **P2.1**: `tail(15)` muestra las 10 nuevas + 5 previas
- [ ] **P2.2**: Dimensiones mostradas: filas y columnas
- [ ] **P2.3**: Columna duplicada eliminada ✓
- [ ] **P2.4**: Edad de hombres con `.str.strip()`
- [ ] **P2.5**: Porcentaje con 2 decimales exactos
- [ ] **P2.6**: Dos edades promedio (>50K y <=50K)
- [ ] **PE1 ó PE2 ó PE3**: Al menos UNA sección electiva completada
- [ ] **Gráficos**: Guardados con `plt.savefig()` o mostrados
- [ ] **Código**: Comentado y explicado claramente
- [ ] **Link Colab**: Compartido como "cualquiera con el link"

---

## 🎓 RESUMEN DE PUNTOS TOTALES

```
OBLIGATORIAS (15 pts):
├── P1.1: 1 pt
├── P1.2: 3 pts
├── P2.1: 1 pt
├── P2.2: 1 pt
├── P2.3: 1 pt
├── P2.4: 2 pts
├── P2.5: 3 pts
└── P2.6: 3 pts

ELECTIVAS (7 pts) — elige 1 opción:
├── Opción A:
│   ├── PE1: 3.5 pts
│   └── PE2: 3.5 pts
└── Opción B:
    └── PE3: 7 pts

TOTAL: 22 puntos máximo (bonus)
APROBACIÓN: 11 puntos (50%)
```

---

## 💡 TIPS FINALES

1. **Siempre verifica los datos** después de cada paso
2. **Usa `print()`** extensivamente para debuggear
3. **Copypaste menos, escribe más**: Entenderás mejor el código
4. **Los espacios en archivos CSV son traicioneros** → `.strip()`
5. **En Pandas, diferencia entre `df.copy()` y referencias**
6. **Guarda gráficos ANTES de .show() (a veces .show() en Colab los borra)**

---

**¡Mucho éxito en el examen! 🚀**
