# Prompts útiles para investigadores

Colección de prompts probados para usar con GitHub Copilot en VS Code.

---

## ⭐ Ejercicio en clase — Explorar el proyecto con Copilot (Ejer0)

> **Para el profesor:** ejercicio de calentamiento. Los alumnos abren la carpeta del proyecto
> en VS Code y usan `@workspace` para orientarse antes de tocar ningún archivo.
> Ideal para practicar la lectura asistida de un proyecto desconocido.

```
@workspace Explícame qué hace este proyecto: qué problema resuelve, cómo está organizado y cuáles son los archivos más importantes.
```

Una vez respondido, pide el registro de la exploración:

```
@workspace Genera un breve cuaderno de bitácora en formato Markdown que resuma:
- Qué archivos existen y para qué sirven
- Las dependencias externas encontradas
- El flujo de ejecución principal
Guárdalo como recursos/bitacora_ejer0.md
```

**Prompts adicionales de exploración:**
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

---

## ⭐ Ejercicio en clase — Traducir invernadero.m a Python (Ejer1a)

> **Para el profesor:** los alumnos abren `Ejercicios/Ejer1/invernadero.m` en el editor
> y pegan el prompt en el Chat de Copilot (modo **Agent**).
> El agente genera `invernadero.py` y al final crea el cuaderno de bitácora.

Abre `invernadero.m` y escribe este prompt en el Chat:

```
Traduce este script de MATLAB a Python 3.
Usa numpy para los cálculos numéricos, pandas para guardar el CSV
y matplotlib para todas las gráficas.
Mantén la misma estructura de secciones y los mismos comentarios.

Al terminar, crea el archivo Ejercicios/Ejer1/bitacora_ejer1a.md con un cuaderno de bitácora
que incluya:
- Fecha de generación
- Qué hace el script original y el traducido
- Decisiones de traducción (equivalencias MATLAB → Python usadas)
- Librerías Python necesarias
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
instalar requirements.txt si existe y ejecutar Ejercicios/Ejer1/invernadero.py.
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

## ⭐ Ejercicio en clase — Docker para reproducibilidad (Ejer1b)

> **Para el profesor:** una vez que los alumnos tienen `invernadero.py` generado (Ejer1),
> piden a Copilot que cree el entorno reproducible con Docker.
> El resultado es un `docker-compose.yml` funcional que ejecuta el script sin instalar Python localmente.

```
Tengo el archivo invernadero.py en la carpeta Ejercicios/Ejer1/ y un requirements.txt
con las dependencias necesarias.

Genera un docker-compose.yml mínimo para ejecutar este script con un único servicio.
Debe:
- Usar la imagen python:3.11-slim
- Montar la carpeta Ejercicios/Ejer1/ como /workspace dentro del contenedor
- Instalar requirements.txt si existe (pip install --no-cache-dir)
- Ejecutar invernadero.py al arrancar

No añadas Jupyter ni variables de entorno innecesarias.

Además, el script usa matplotlib para mostrar gráficas. Como Docker no tiene pantalla,
añade matplotlib.use('Agg') justo después de importar matplotlib y guarda cada figura
como PNG en la misma carpeta antes de plt.show().

Una vez generado el fichero, lanza el contenedor con docker compose up.

Al terminar, crea Ejercicios/Ejer1/bitacora_ejer1b.md con un cuaderno de bitácora que incluya:
- Archivos creados o modificados y por qué
- Imagen Docker elegida y motivo
- Cambios realizados en invernadero.py para el modo headless
- Comando para reproducir el entorno
```

---

## ⭐ Ejercicio en clase — Dashboard HTML con datos reales (Ejer2)

> **Para el profesor:** los alumnos abren la carpeta `Ejercicios/Ejer2/` que contiene solo
> `dataset_invernadero.csv`. Pegan este prompt con el CSV visible en el editor.
> En 1–2 minutos tendrán un dashboard funcional sin instalar nada.

```
Tengo el archivo Ejercicios/Ejer2/dataset_invernadero.csv con columnas:
dia, T_ext_C, T_int_C, H_ext_pct, H_int_pct, CO2_ppm, viento_ms
(7 días de sensores de invernadero, muestreo cada 15 min).

Crea un archivo Ejercicios/Ejer2/dashboard_invernadero.html autocontenido
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

Al terminar, crea Ejercicios/Ejer2/bitacora_ejer2.md con un cuaderno de bitácora que incluya:
- Archivos generados
- Componentes del dashboard y datos que muestra cada uno
- Decisiones de diseño (colores, umbrales de alerta, librería)
```

---

## ⭐ Ejercicio en clase — Identificación de modelo ARX (Ejer3)

> **Para el profesor:** los alumnos abren la carpeta `Ejercicios/Ejer3/` — solo contiene
> los dos `.mat`, sin código. El agente genera el script completo desde cero.
>
> ⚠️ **Toolbox:** `iddata()` y `arx()` requieren el **System Identification Toolbox** (licencia adicional).
> El prompt ya incluye la instrucción de usar mínimos cuadrados si no está disponible.
>
> 💡 **Directorio de trabajo:** `cd(fileparts(mfilename('fullpath')))` evita que MATLAB
> no encuentre los `.mat` al ejecutar desde VS Code o desde otra carpeta.

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

Al inicio del script añade cd(fileparts(mfilename('fullpath'))) para que MATLAB
encuentre los archivos .mat independientemente del directorio de trabajo.

Si no tengo el System Identification Toolbox, implementa el modelo ARX usando
mínimos cuadrados ordinarios con operaciones de matrices (sin iddata ni arx).

Al terminar, crea Ejercicios/Ejer3/bitacora_ejer3.md con un cuaderno de bitácora que incluya:
- Archivos .mat utilizados y variables extraídas
- Estructura del modelo ARX (orden, entradas, salida)
- Estrategia de identificación y validación aplicada
- Métricas de calidad del modelo (RMSE, FIT u otras)
```

