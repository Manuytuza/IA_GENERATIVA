"""
EXAMEN PARCIAL 1 - IA GENERATIVA CON PYTHON
Solución paso a paso con explicaciones
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 80)
print("PARTE OBLIGATORIA")
print("=" * 80)

# ============================================================================
# P1. MANEJO DE ARCHIVOS CSV CON MÉTODO WITH (SIN PANDAS)
# ============================================================================

print("\n" + "=" * 80)
print("P1.1 - LEER EL ARCHIVO datos_examen.csv")
print("=" * 80)

# Primero, verificar que el archivo existe y leer primeras filas
try:
    with open('datos_examen.csv', 'r', encoding='utf-8') as f:
        # Leer primeras 5 filas para verificar estructura
        reader = csv.reader(f)
        filas_leidas = []
        for i, fila in enumerate(reader):
            if i < 5:
                filas_leidas.append(fila)
                print(f"Fila {i}: {len(fila)} columnas")
        
        print(f"\nPrimeras filas del archivo:")
        for fila in filas_leidas[:3]:
            print(fila[:5], "...")  # Mostrar solo primeras 5 columnas
            
except FileNotFoundError:
    print("⚠️  Archivo no encontrado. Asegúrate de que 'datos_examen.csv' esté en el directorio actual.")

print("\n" + "=" * 80)
print("P1.2 - AGREGAR 10 FILAS AL FINAL DEL ARCHIVO")
print("=" * 80)

# Las 10 filas a agregar
nuevas_filas = [
    ['32550', '32', 'Private', '34066', '10th', '6', 'Married-civ-spouse', 'Handlers-cleaners', 'Husband', 'Amer-Indian-Eskimo', 'Male', '0', '0', '40', 'United-States', '<=50K'],
    ['32551', '43', 'Private', '84661', 'Assoc-voc', '11', 'Married-civ-spouse', 'Sales', 'Husband', 'White', 'Male', '0', '0', '45', 'United-States', '<=50K'],
    ['32552', '32', 'Private', '116138', 'Masters', '14', 'Never-married', 'Tech-support', 'Not-in-family', 'Asian-Pac-Islander', 'Male', '0', '0', '11', 'Taiwan', '<=50K'],
    ['32553', '53', 'Private', '321865', 'Masters', '14', 'Married-civ-spouse', 'Exec-managerial', 'Husband', 'White', 'Male', '0', '0', '40', 'United-States', '>50K'],
    ['32554', '22', 'Private', '310152', 'Some-college', '10', 'Never-married', 'Protective-serv', 'Not-in-family', 'White', 'Male', '0', '0', '40', 'United-States', '<=50K'],
    ['32555', '27', 'Private', '257302', 'Assoc-acdm', '12', 'Married-civ-spouse', 'Tech-support', 'Wife', 'White', 'Female', '0', '0', '38', 'United-States', '<=50K'],
    ['32556', '40', 'Private', '154374', 'HS-grad', '9', 'Married-civ-spouse', 'Machine-op-inspct', 'Husband', 'White', 'Male', '0', '0', '40', 'United-States', '>50K'],
    ['32557', '58', 'Private', '151910', 'HS-grad', '9', 'Widowed', 'Adm-clerical', 'Unmarried', 'White', 'Female', '0', '0', '40', 'United-States', '<=50K'],
    ['32558', '22', 'Private', '201490', 'HS-grad', '9', 'Never-married', 'Adm-clerical', 'Own-child', 'White', 'Male', '0', '0', '20', 'United-States', '<=50K'],
    ['32559', '52', 'Self-emp-inc', '287927', 'HS-grad', '9', 'Married-civ-spouse', 'Exec-managerial', 'Wife', 'White', 'Female', '15024', '0', '40', 'United-States', '>50K'],
]

print(f"📝 Agregando {len(nuevas_filas)} nuevas filas al archivo...")

# OPCIÓN 1: Usar 'append' mode (a) - agregar al final sin borrar
try:
    with open('datos_examen.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for fila in nuevas_filas:
            writer.writerow(fila)
    print("✅ Filas agregadas exitosamente al archivo 'datos_examen.csv'")
except Exception as e:
    print(f"❌ Error al agregar filas: {e}")

# Verificar que se agregaron correctamente 
print("\n📊 VERIFICACIÓN: Contando filas en el archivo...")
try:
    with open('datos_examen.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        total_filas = sum(1 for _ in reader)
    print(f"✅ Total de filas en el archivo: {total_filas}")
    print(f"   (Esto incluye el encabezado si existe)")
except Exception as e:
    print(f"❌ Error al contar filas: {e}")

# Mostrar las últimas 12 filas (10 nuevas + 2 previas para verificar)
print("\n📋 Últimas 12 filas del archivo (para verificar que se agregaron):")
try:
    with open('datos_examen.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        filas = list(reader)
        for i, fila in enumerate(filas[-12:], start=len(filas)-11):
            # Solo mostrar primeras 5 columnas para claridad
            print(f"Fila {i}: {fila[0]} | {fila[1]} | {fila[9]} | {fila[-1]}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "=" * 80)
print("PARTE 2: PROCESAMIENTO CON PANDAS")
print("=" * 80)

# Cargar el dataset completo con Pandas
print("\n🔄 Cargando dataset con Pandas...")
df = pd.read_csv('datos_examen.csv')
print("✅ Dataset cargado correctamente")

# ============================================================================
# P2.1 - MOSTRAR LAS 15 FILAS FINALES
# ============================================================================
print("\n" + "-" * 80)
print("P2.1 - MOSTRAR LAS 15 FILAS FINALES")
print("-" * 80)
print("\nÚltimas 15 filas del dataset:")
print(df.tail(15))

# ============================================================================
# P2.2 - DIMENSIONES DEL DATAFRAME
# ============================================================================
print("\n" + "-" * 80)
print("P2.2 - DIMENSIONES DEL DATAFRAME")
print("-" * 80)
filas, columnas = df.shape
print(f"\n📊 Dimensiones del DataFrame:")
print(f"   Filas: {filas}")
print(f"   Columnas: {columnas}")
print(f"\nNombres de las columnas:")
for i, col in enumerate(df.columns):
    print(f"   {i}: {col}")

# ============================================================================
# P2.3 - ELIMINAR COLUMNA QUE COPIA EL ÍNDICE
# ============================================================================
print("\n" + "-" * 80)
print("P2.3 - ELIMINAR COLUMNA QUE COPIA EL ÍNDICE")
print("-" * 80)

# Identificar la columna que es copia del índice
# Generalmente es la primera columna sin nombre o con nombre genérico
print("\n🔍 Identificando columna que duplica el índice...")
print("Primeras filas del DataFrame original:")
print(df.head(3))

# La primera columna (índice 0) parece ser: Unnamed: 0 o tiene valores 0, 1, 2...
# Buscar columnas que sean exactamente iguales al índice
if 'Unnamed: 0' in df.columns:
    print("\n✅ Encontrada columna 'Unnamed: 0' que duplica el índice")
    df = df.drop('Unnamed: 0', axis=1)
else:
    # Alternativamente, buscar si la primera columna es idéntica al índice
    if (df.iloc[:, 0].values == df.index.values).all():
        col_name = df.columns[0]
        print(f"\n✅ Columna '{col_name}' es idéntica al índice")
        df = df.drop(col_name, axis=1)

print("\nDataFrame después de eliminar la columna duplicada:")
print(f"Nuevas dimensiones: {df.shape}")
print(df.head(3))

# ============================================================================
# P2.4 - EDAD PROMEDIO DEL SEXO MASCULINO
# ============================================================================
print("\n" + "-" * 80)
print("P2.4 - EDAD PROMEDIO DEL SEXO MASCULINO")
print("-" * 80)

# Identificar la columna de edad y sexo
print("\nColumnas del DataFrame:")
print(df.columns.tolist())

# Buscar columnas con 'age' o 'edad' en el nombre
age_col = None
sex_col = None

for col in df.columns:
    if 'age' in col.lower():
        age_col = col
    if 'sex' in col.lower() or 'gender' in col.lower():
        sex_col = col

print(f"\n📌 Columna de edad: {age_col}")
print(f"📌 Columna de sexo: {sex_col}")

# Calcular edad promedio de hombres
if age_col and sex_col:
    # Filtrar solo hombres (generalmente "Male")
    hombres = df[df[sex_col] == ' Male']
    edad_promedio_hombres = hombres[age_col].mean()
    
    print(f"\n✅ Edad promedio del sexo masculino:")
    print(f"   {edad_promedio_hombres:.2f} años")
    print(f"   (Calculado sobre {len(hombres)} registros de hombres)")
else:
    print("❌ No se encontraron las columnas requeridas")

# ============================================================================
# P2.5 - PORCENTAJE DE CUBANOS
# ============================================================================
print("\n" + "-" * 80)
print("P2.5 - PORCENTAJE DE CUBANOS")
print("-" * 80)

# Buscar columna de país
country_col = None
for col in df.columns:
    if 'country' in col.lower():
        country_col = col

print(f"\n📌 Columna de país: {country_col}")

if country_col:
    # Mostrar países únicos (primeros 20)
    print(f"\nPaíses únicos en el dataset (primeros 20):")
    paises = df[country_col].unique()[:20]
    for pais in paises:
        print(f"   '{pais}'")
    
    # Contar cubanos (nota: buscar "Cuba" en la columna)
    # Algunos datasets tienen espacios al inicio
    cubanos_count = (df[country_col] == ' Cuba').sum()
    if cubanos_count == 0:
        # Intentar sin espacios
        cubanos_count = (df[country_col] == 'Cuba').sum()
    
    total_registros = len(df)
    porcentaje_cubanos = (cubanos_count / total_registros) * 100
    
    print(f"\n✅ Resultados:")
    print(f"   Total de cubanos: {cubanos_count}")
    print(f"   Total de registros: {total_registros}")
    print(f"   El porcentaje de cubanos es: {porcentaje_cubanos:.2f}%")
else:
    print("❌ No se encontró columna de país")

# ============================================================================
# P2.6 - EDAD PROMEDIO POR RANGO SALARIAL
# ============================================================================
print("\n" + "-" * 80)
print("P2.6 - EDAD PROMEDIO POR RANGO SALARIAL")
print("-" * 80)

# Buscar columna de ingreso
income_col = None
for col in df.columns:
    if 'income' in col.lower() or '50k' in col.lower():
        income_col = col

print(f"\n📌 Columna de ingreso: {income_col}")

if age_col and income_col:
    # Edad promedio de los que ganan > 50K
    mas_de_50k = df[df[income_col] == ' >50K']
    edad_prom_mas_50k = mas_de_50k[age_col].mean()
    
    # Edad promedio de los que ganan <= 50K
    hasta_50k = df[df[income_col] == ' <=50K']
    edad_prom_hasta_50k = hasta_50k[age_col].mean()
    
    print(f"\n✅ Resultados:")
    print(f"   Edad promedio de quienes ganan >50K: {edad_prom_mas_50k:.2f} años")
    print(f"      (Basado en {len(mas_de_50k)} registros)")
    print(f"   Edad promedio de quienes ganan <=50K: {edad_prom_hasta_50k:.2f} años")
    print(f"      (Basado en {len(hasta_50k)} registros)")
    print(f"\n   Diferencia: {abs(edad_prom_mas_50k - edad_prom_hasta_50k):.2f} años")
else:
    print("❌ No se encontraron las columnas requeridas")

print("\n" + "=" * 80)
print("PARTE ELECTIVAS")
print("=" * 80)

# ============================================================================
# PE1 - GRÁFICO PIE DE INGRESO
# ============================================================================
print("\n" + "-" * 80)
print("PE1 - GRÁFICO PIE DE INGRESOS (<=50K vs >50K)")
print("-" * 80)

if income_col:
    # Contar registros por categoría de ingreso
    conteos = df[income_col].value_counts()
    print(f"\nConteo por categoría de ingreso:")
    print(conteos)
    
    # Crear gráfico pie
    plt.figure(figsize=(8, 6))
    colores = ['#ff9999', '#66b3ff']
    plt.pie(conteos.values, 
            labels=[label.strip() for label in conteos.index],
            autopct='%1.1f%%',
            colors=colores,
            startangle=90)
    plt.title('Distribución de Ingresos: <=50K vs >50K', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('grafico_ingresos_pie.png', dpi=100, bbox_inches='tight')
    print("\n✅ Gráfico guardado como 'grafico_ingresos_pie.png'")
    plt.show()

# ============================================================================
# PE2 - SIMULACIÓN MONEDA CON TRUCO
# ============================================================================
print("\n" + "-" * 80)
print("PE2 - SIMULACIÓN MONEDA TRUCADA (70% cara)")
print("-" * 80)

# Simular 50 lanzamientos donde cara sale 70% de las veces
np.random.seed(42)  # Para reproducibilidad
lanzamientos = 50
probabilidad_cara = 0.7

# 1 = cara, 0 = cruz
resultados = np.random.binomial(n=1, p=probabilidad_cara, size=lanzamientos)

# Calcular caras acumuladas
caras_acumuladas = np.cumsum(resultados)
porcentaje_caras = (caras_acumuladas / np.arange(1, lanzamientos + 1)) * 100

print(f"\nSimulación de {lanzamientos} lanzamientos:")
print(f"Cara (1): {resultados}")
print(f"\nTotal de caras: {resultados.sum()}")
print(f"Porcentaje de caras: {(resultados.sum() / lanzamientos) * 100:.2f}%")
print(f"Porcentaje esperado: 70%")

# Crear gráfico de línea
plt.figure(figsize=(12, 6))
plt.plot(range(1, lanzamientos + 1), porcentaje_caras, 
         marker='o', linestyle='-', linewidth=2, markersize=4, color='#2E86AB')
plt.axhline(y=70, color='red', linestyle='--', linewidth=2, label='Probabilidad esperada (70%)')
plt.xlabel('Número de lanzamiento', fontsize=12)
plt.ylabel('Porcentaje de caras (%)', fontsize=12)
plt.title('Moneda Trucada: Convergencia a 70% caras en 50 lanzamientos', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig('grafico_moneda_simulacion.png', dpi=100, bbox_inches='tight')
print("\n✅ Gráfico guardado como 'grafico_moneda_simulacion.png'")
plt.show()

# ============================================================================
# PE3 - PRIMOS DE MERSENNE MENORES QUE 100
# ============================================================================
print("\n" + "-" * 80)
print("PE3 - PRIMOS DE MERSENNE MENORES QUE 100")
print("-" * 80)

def es_primo(n):
    """Verifica si un número es primo"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def encontrar_primos_mersenne(limite):
    """
    Encuentra primos de Mersenne menores que 'limite'
    
    Un primo de Mersenne es:
    1. Un número primo
    2. Se expresa como 2^p - 1, donde p también es primo
    """
    primos_mersenne = []
    
    # Buscar números primos menores al límite
    for candidato in range(2, limite):
        if not es_primo(candidato):
            continue
        
        # Verificar si este primo es de Mersenne
        # Buscar un p primo tal que 2^p - 1 = candidato
        p = 2
        while True:
            mersenne_value = (2 ** p) - 1
            
            if mersenne_value > candidato:
                break
            
            if mersenne_value == candidato and es_primo(p):
                primos_mersenne.append({
                    'numero': candidato,
                    'formula': f'2^{p} - 1',
                    'p': p
                })
                break
            
            # Siguiente número primo
            p += 1
            while not es_primo(p):
                p += 1
    
    return primos_mersenne

# Encontrar primos de Mersenne menores a 100
print("\n🔍 Buscando primos de Mersenne menores a 100...\n")

primos_mersenne = encontrar_primos_mersenne(100)

if primos_mersenne:
    print(f"✅ Se encontraron {len(primos_mersenne)} primos de Mersenne:\n")
    for primo in primos_mersenne:
        print(f"   {primo['numero']:3d} = {primo['formula']} (p={primo['p']})")
        # Verificación
        verificacion = (2 ** primo['p']) - 1
        print(f"        Verificación: 2^{primo['p']} - 1 = {verificacion} ✓")
else:
    print("❌ No se encontraron primos de Mersenne")

print("\n" + "=" * 80)
print("✅ EXAMEN COMPLETO")
print("=" * 80)
