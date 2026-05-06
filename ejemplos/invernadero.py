# =========================================================
# Monitorización de sensores de invernadero
# Dataset sintético de 7 días (muestras cada 15 min)
# Variables: temperatura, humedad, CO2 y viento (interior/exterior)
# Incluye dos eventos: fallo de calefacción y fallo de ventilación
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

rng = np.random.default_rng(seed=7)  # Semilla fija → resultados reproducibles

# --- 1. Vector de tiempo ---
inicio  = datetime(2024, 4, 1)       # Lunes de referencia
minutos = np.arange(0, 7 * 24 * 60, 15)
fechas  = [inicio + timedelta(minutes=int(m)) for m in minutos]
N       = len(minutos)
t_horas = minutos / 60               # Horas desde el inicio

# Función de ciclo diario (seno con pico a la hora "pico")
def ciclo(pico):
    return np.sin(2 * np.pi * (t_horas - pico) / 24)

# --- 2. Temperatura (°C) ---
T_ext = 15 + 8 * ciclo(14) + 1.5 * rng.standard_normal(N)
T_int = 22 + 1.2 * ciclo(16) + 0.3 * (T_ext - 15) + 0.4 * rng.standard_normal(N)

# --- 3. Humedad relativa (%) ---
H_ext = np.clip(60 - 15 * ciclo(14) + 5 * rng.standard_normal(N), 20, 100)
H_int = np.clip(70 -  5 * ciclo(16) + 2 * rng.standard_normal(N), 40, 95)

# --- 4. CO2 interior (ppm) ---
# Cae de día (fotosíntesis) y sube de noche (respiración)
luz     = np.maximum(0, ciclo(13))
CO2_int = np.maximum(400, 800 - 320 * luz + 50 * rng.standard_normal(N))

# --- 5. Viento exterior (m/s) ---
viento = np.abs(3 + 2 * rng.standard_normal(N))
# Racha de viento el día 2 (3 horas)
i_racha = slice(round(2 * 24 * 4), round(2 * 24 * 4 + 3 * 4))
viento[i_racha] += 8 * rng.random(len(viento[i_racha]))

# --- 6. Eventos anómalos ---
# Evento A: fallo de calefacción en día 3 (2 horas) → bajada brusca T_int
i_fallo = slice(round(3 * 24 * 4), round(3 * 24 * 4 + 2 * 4))
n_fallo = len(T_int[i_fallo])
T_int[i_fallo] -= 6 * np.linspace(1, 0, n_fallo)

# Evento B: fallo de ventilación en día 5 (3 horas) → pico de CO2
i_vent = slice(round(5 * 24 * 4), round(5 * 24 * 4 + 3 * 4))
n_vent = len(CO2_int[i_vent])
CO2_int[i_vent] += 700 * np.linspace(0, 1, n_vent)

# --- 7. Guardar dataset en CSV ---
df = pd.DataFrame({
    "fecha":      fechas,
    "T_ext_C":    T_ext,
    "T_int_C":    T_int,
    "H_ext_pct":  H_ext,
    "H_int_pct":  H_int,
    "CO2_ppm":    CO2_int,
    "viento_ms":  viento,
})
df.to_csv("dataset_invernadero.csv", index=False)
print(f"Dataset guardado: dataset_invernadero.csv ({N} filas)")

# --- 8. Figura principal: 7 días completos ---
fig, axes = plt.subplots(4, 1, figsize=(14, 9), sharex=True)
fig.suptitle("Invernadero — visión general", fontsize=13)

axes[0].plot(fechas, T_ext, color="0.6", lw=0.8, label="Exterior")
axes[0].plot(fechas, T_int, color="red",  lw=1.5, label="Interior")
axes[0].set_ylabel("T (°C)"); axes[0].set_title("Temperatura")
axes[0].legend(loc="upper left"); axes[0].grid(True)

axes[1].plot(fechas, H_ext, color="0.6", lw=0.8, label="Exterior")
axes[1].plot(fechas, H_int, color="blue", lw=1.5, label="Interior")
axes[1].set_ylabel("HR (%)"); axes[1].set_title("Humedad relativa")
axes[1].legend(loc="upper left"); axes[1].grid(True)

axes[2].plot(fechas, CO2_int, color="#2d9e2d", lw=1.2)
axes[2].axhline(1200, color="red", linestyle="--", label="Límite alerta")
axes[2].set_ylabel("CO₂ (ppm)"); axes[2].set_title("CO₂ interior")
axes[2].legend(loc="upper left"); axes[2].grid(True)

axes[3].plot(fechas, viento, color="#5555cc", lw=1.0)
axes[3].set_ylabel("Viento (m/s)"); axes[3].set_title("Viento exterior")
axes[3].grid(True)

axes[3].xaxis.set_major_locator(mdates.DayLocator())
axes[3].xaxis.set_major_formatter(mdates.DateFormatter("%a"))
plt.tight_layout()

# --- 9. Figura de zoom: eventos anómalos ---
fig2, (az1, az2) = plt.subplots(1, 2, figsize=(13, 4))
fig2.suptitle("Zoom — eventos anómalos", fontsize=13)

# Zoom fallo calefacción (día 3, ventana ±6 horas)
zoom_fallo = [inicio + timedelta(days=3, hours=-6),
              inicio + timedelta(days=3, hours=9)]
az1.plot(fechas, T_int, color="red", lw=1.4)
az1.axvline(inicio + timedelta(days=3), color="black", linestyle="--", label="Fallo")
az1.set_xlim(zoom_fallo)
az1.set_ylabel("T interior (°C)"); az1.set_title("Evento A — Fallo calefacción (día 3)")
az1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M\n%a"))
az1.legend(); az1.grid(True)

# Zoom fallo ventilación (día 5, ventana ±6 horas)
zoom_vent = [inicio + timedelta(days=5, hours=-6),
             inicio + timedelta(days=5, hours=10)]
az2.plot(fechas, CO2_int, color="#2d9e2d", lw=1.4)
az2.axvline(inicio + timedelta(days=5), color="black", linestyle="--", label="Fallo")
az2.axhline(1200, color="red", linestyle="--", label="Límite alerta")
az2.set_xlim(zoom_vent)
az2.set_ylabel("CO₂ (ppm)"); az2.set_title("Evento B — Fallo ventilación (día 5)")
az2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M\n%a"))
az2.legend(); az2.grid(True)

plt.tight_layout()
plt.show()
