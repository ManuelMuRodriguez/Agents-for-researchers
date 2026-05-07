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
