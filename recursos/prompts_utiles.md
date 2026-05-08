# Prompts útiles para investigadores

Colección de prompts probados para usar con GitHub Copilot en VS Code.

---

## Entender un proyecto existente

Antes de tocar nada, pide a Copilot que te oriente. Especialmente útil cuando el proyecto tiene muchos archivos o lleva tiempo sin tocarse.

```
@workspace Explícame qué hace este proyecto: qué problema resuelve, cómo está organizado y cuáles son los archivos más importantes.
```
```
@workspace ¿Cuál es el flujo principal del código? ¿Por dónde empieza la ejecución y qué pasos sigue?
```
```
@workspace Tengo que modificar la parte que calcula [X]. ¿En qué archivos está esa lógica y qué debería tener en cuenta antes de cambiarla?
```
```
@workspace ¿Qué dependencias externas usa este proyecto y para qué sirve cada una?
```
```
@workspace Explícame este archivo como si fuera la primera vez que lo veo. ¿Qué hace, por qué existe y cómo encaja con el resto del proyecto?
```

---

## Traducción de código

```
Traduce este script de MATLAB a Python 3 manteniendo los mismos comentarios y la misma lógica
```
```
Convierte esta función de R a Python usando numpy/pandas donde sea equivalente
```
```
Explícame este script línea a línea como si no supiera [MATLAB/R/Python]
```

### Ejercicio guiado — invernadero.m → Python

Abre `invernadero.m` y escribe este prompt en el Chat:

```
Traduce este script de MATLAB a Python 3.
Usa numpy para los cálculos numéricos, pandas para guardar el CSV
y matplotlib para todas las gráficas.
Mantén la misma estructura de secciones y los mismos comentarios.
```

---

## Documentación

```
Añade docstrings a todas las funciones de este archivo
```
```
Genera un README para este proyecto con instrucciones de instalación y uso
```
```
Escribe un mensaje de commit para los cambios que acabo de hacer
```

---

## Reproducibilidad

```
Genera un docker-compose.yml mínimo para este proyecto con un único servicio.
Debe usar python:3.11-slim, montar la carpeta actual en /workspace,
instalar requirements.txt si existe y ejecutar ejemplos/invernadero.py.
No añadas Jupyter ni variables de entorno.
```
```
Genera un Dockerfile para ejecutar este script con Python 3.11
```
```
Crea un docker-compose.yml que incluya Python 3.11 y Jupyter Notebook
```
```
¿Qué librerías necesita este script? Genera un requirements.txt
```

---

## Depuración

```
Este código da el siguiente error: [pega el error]. ¿Qué lo causa y cómo lo soluciono?
```
```
Refactoriza esta función para que sea más legible sin cambiar su comportamiento
```
```
¿Hay algún caso límite que este código no maneje correctamente?
```

---

## Funcionalidades seleccionadas (para pegar sobre invernadero.m)

```
Añade mapas de calor (heatmaps) por hora del día vs día de la semana
para T_int_C, H_int_pct y CO2_ppm.
Usa una figura con 3 subplots (uno por variable), colorbar en cada subplot
y títulos listos para una presentación.
```

```
Calcula un resumen diario de métricas para todos los sensores
(T_ext_C, T_int_C, H_ext_pct, H_int_pct, CO2_ppm, viento_ms):
mínimo, máximo y media por día.
Guárdalo en resumen_diario_invernadero.csv.
```

```
Calcula la matriz de correlación de Pearson entre todos los sensores
y muéstrala como tabla y también como heatmap con etiquetas legibles.
Además, guarda la matriz en correlacion_sensores.csv.
```

---

## ⭐ Ejercicio en clase — Identificación de modelo ARX (Ejer2)

> **Para el profesor:** los alumnos solo necesitan la carpeta `Ejercicios/Ejer2/` con los dos `.mat` dentro.
> Sin ningún archivo de código, piden al agente que lo genere desde cero. El resultado es el `Identifica_ARX_221.m` del repo.

```
En esta carpeta hay varios archivos .mat que contienen datos reales de invernadero.
Las variables de interés son XTINV, que es la temperatura interior del invernadero,
PRAD, la radiación solar, PVV, la velocidad del viento, y UVENT_cen, la apertura de ventilación.

Me gustaría crear un código de MATLAB que cargue los datos del archivo "2020_11_15.mat"
y los utilizase para obtener un modelo ARX de orden 221 para simular como salida
la temperatura del invernadero considerando como entradas la radiación, la apertura de ventilación
y la velocidad del viento.

Una vez obtenido, me gustaría validar los resultados con los datos del archivo "2020_11_16.mat".

El tiempo de muestreo de los datos se debe definir en una variable Ts=30 y en base a esto
crear un vector de tiempo T considerando la longitud de los vectores datos anteriormente mencionados.
```

---

## ⭐ Ejercicio en clase — Dashboard HTML con datos reales

> **Para el profesor:** di a los alumnos que abran el Chat de Copilot con el archivo
> `dataset_invernadero.csv` visible en el editor y que peguen este prompt.
> En 1–2 minutos tendrán un dashboard funcional sin instalar nada.

```
Tengo el archivo ejemplos/dataset_invernadero.csv con columnas:
dia, T_ext_C, T_int_C, H_ext_pct, H_int_pct, CO2_ppm, viento_ms
(7 días de sensores de invernadero, muestreo cada 15 min).

Crea un archivo ejemplos/dashboard_invernadero.html autocontenido
(sin servidor, sin dependencias locales) que muestre:

1. CARDS de resumen con los valores de las últimas 24 horas:
   temperatura interior, humedad interior, CO₂ y viento.
   Cada card debe mostrar valor actual, promedio, mínimo y máximo.
   Añade un badge de alerta si CO₂ > 1200 ppm o viento > 10 m/s.

2. GRÁFICAS TEMPORALES de los 7 días completos:
   - Temperatura interior vs exterior (líneas)
   - Humedad interior vs exterior (líneas)
   - CO₂ interior con línea de umbral en 1200 ppm
   - Viento exterior (barras, resalta las rachas altas)

Diseño dark-mode. Usa Chart.js desde CDN.
Incrusta los datos del CSV directamente en el HTML como arrays JavaScript
(no necesito leer el CSV en tiempo de ejecución).
```
