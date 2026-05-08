# Cuaderno de bitácora — Ejer1a: Traducción MATLAB → Python

**Fecha de generación:** 8 de mayo de 2026  
**Archivo origen:** `Ejercicios/Ejer1/invernadero.m`  
**Archivo generado:** `Ejercicios/Ejer1/invernadero.py`

---

## ¿Qué hace el script original?

`invernadero.m` genera un dataset sintético de 7 días de sensores de invernadero (muestras cada 15 min). Simula temperatura interior/exterior, humedad relativa, CO₂ y viento. Incluye dos fallos simulados (calefacción en día 3, ventilación en día 5), guarda el resultado en CSV y produce dos figuras de visualización.

## ¿Qué hace el script traducido?

`invernadero.py` replica exactamente la misma lógica con las mismas secciones y comentarios, usando las librerías estándar de Python para ciencia de datos. Además, como puede ejecutarse en entornos sin pantalla (Docker), guarda las figuras como PNG en lugar de mostrarlas en ventana.

---

## Decisiones de traducción (equivalencias MATLAB → Python)

| MATLAB | Python | Motivo |
|---|---|---|
| `rng(7)` | `np.random.default_rng(7)` | Semilla reproducible; `default_rng` es la API moderna de NumPy |
| `randn(N,1)` | `rng.standard_normal(N)` | Ruido gaussiano con la misma semilla |
| `rand(N,1)` | `rng.random(N)` | Uniforme [0,1) |
| `(0 : dt : 7-dt)'` | `np.arange(0, 7, dt)` | Vector de tiempo equivalente |
| `max(a, b)` elemento a elemento | `np.maximum(a, b)` | Versión vectorizada de NumPy |
| `min(a, b)` / `max(a,b)` combinados | `np.clip(array, min, max)` | Más idiomático en NumPy |
| `linspace(1,0,n)'` | `np.linspace(1, 0, n)` | Identical |
| `table(...)` + `writetable` | `pd.DataFrame(...)` + `.to_csv()` | Equivalente pandas |
| `fileparts(mfilename('fullpath'))` | `os.path.dirname(os.path.abspath(__file__))` | Ruta del propio script |
| `fullfile(dir, file)` | `os.path.join(dir, file)` | Construcción de rutas portable |
| `fprintf(...)` | `print(f'...')` | f-string equivalente |
| `figure(...)` + `subplot(4,1,i)` | `plt.subplots(4, 1, sharex=True)` | `sharex=True` equivale a `linkaxes` |
| `linkaxes([...], 'x')` | `sharex=True` en `subplots` | Sincronización de eje X |
| `yline(1200,'r--',...)` | `ax.axhline(1200, ...)` | Línea horizontal de referencia |
| `xline(3,'k--',...)` | `ax.axvline(3, ...)` | Línea vertical de referencia |
| `xticks` / `xticklabels` | `ax.set_xticks` / `ax.set_xticklabels` | Etiquetas de eje X |
| `figure.savefig` (implícito) | `fig.savefig(path, dpi=150)` | Las figuras se guardan como PNG |
| `matplotlib.use('Agg')` | Añadido explícitamente | Necesario para modo headless (Docker) |

---

## Librerías Python necesarias

```
numpy==2.4.3
pandas==2.3.3
matplotlib==3.10.8
```

Ya recogidas en `Ejercicios/Ejer1/requirements.txt`.

---

## Archivos generados al ejecutar el script

| Archivo | Descripción |
|---|---|
| `dataset_invernadero.csv` | Dataset de 672 filas con las 7 variables de sensores |
| `invernadero_general.png` | Figura con visión general de los 7 días (4 subplots) |
| `invernadero_zoom_eventos.png` | Figura de zoom sobre los dos eventos anómalos |

---

## Comando para ejecutar

```bash
cd Ejercicios/Ejer1
pip install -r requirements.txt
python invernadero.py
```

O con Docker (ver `bitacora_ejer1b.md` cuando se complete el Ejer1b):

```bash
docker compose up
```
