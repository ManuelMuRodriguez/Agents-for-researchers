# =========================================================
# Monitorización de sensores de invernadero
# Dataset sintético de 7 días (muestras cada 15 min)
# Variables: temperatura, humedad, CO2 y viento (interior/exterior)
# Incluye dos eventos: fallo de calefacción y fallo de ventilación
#
# Ejecutar: python invernadero.py
# =========================================================

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Modo sin pantalla (Docker / servidores sin display)
import matplotlib.pyplot as plt

# Semilla fija → resultados reproducibles
rng = np.random.default_rng(7)

# --- 1. Vector de tiempo ---
dt      = 15 / (60 * 24)                      # 15 min expresados en días
t_dias  = np.arange(0, 7, dt)                 # 7 días
N       = len(t_dias)
t_horas = t_dias * 24                         # Para cálculos de ciclos diarios

# Función de ciclo diario (seno con pico a la hora "pico")
def ciclo(pico):
    return np.sin(2 * np.pi * (t_horas - pico) / 24)

# --- 2. Temperatura (°C) ---
T_ext = 15 + 8 * ciclo(14) + 1.5 * rng.standard_normal(N)           # Exterior: ciclo diario ±8°C
T_int = 22 + 1.2 * ciclo(16) + 0.3 * (T_ext - 15) + 0.4 * rng.standard_normal(N)  # Interior: controlada ~22°C

# --- 3. Humedad relativa (%) ---
H_ext = 60 - 15 * ciclo(14) + 5 * rng.standard_normal(N)            # Exterior: más alta de noche
H_int = 70 -  5 * ciclo(16) + 2 * rng.standard_normal(N)            # Interior: controlada ~70%
H_ext = np.clip(H_ext, 20, 100)
H_int = np.clip(H_int, 40, 95)

# --- 4. CO2 interior (ppm) ---
# Cae de día (fotosíntesis) y sube de noche (respiración)
luz     = np.maximum(0, ciclo(13))
CO2_int = 800 - 320 * luz + 50 * rng.standard_normal(N)
CO2_int = np.maximum(400, CO2_int)

# --- 5. Viento exterior (m/s) ---
viento = np.abs(3 + 2 * rng.standard_normal(N))
# Racha de viento el día 2 (3 horas)
i_racha = np.arange(round(2 * 24 * 4), round(2 * 24 * 4 + 3 * 4) + 1)
viento[i_racha] = viento[i_racha] + 8 * rng.random(len(i_racha))

# --- 6. Eventos anómalos ---
# Evento A: fallo de calefacción en día 3 (2 horas) → bajada brusca T_int
i_fallo = np.arange(round(3 * 24 * 4), round(3 * 24 * 4 + 2 * 4) + 1)
T_int[i_fallo] = T_int[i_fallo] - 6 * np.linspace(1, 0, len(i_fallo))

# Evento B: fallo de ventilación en día 5 (3 horas) → pico de CO2
i_vent = np.arange(round(5 * 24 * 4), round(5 * 24 * 4 + 3 * 4) + 1)
CO2_int[i_vent] = CO2_int[i_vent] + 700 * np.linspace(0, 1, len(i_vent))

# --- 7. Guardar dataset en CSV ---
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path   = os.path.join(script_dir, 'dataset_invernadero.csv')

df = pd.DataFrame({
    'dia':       t_dias,
    'T_ext_C':   T_ext,
    'T_int_C':   T_int,
    'H_ext_pct': H_ext,
    'H_int_pct': H_int,
    'CO2_ppm':   CO2_int,
    'viento_ms': viento,
})
df.to_csv(csv_path, index=False)
print(f'Dataset guardado: {csv_path} ({N} filas)')

# --- 8. Figura principal: 7 días completos ---
fig1, (ax_T, ax_H, ax_C, ax_V) = plt.subplots(4, 1, figsize=(12, 8), sharex=True)
fig1.canvas.manager.set_window_title('Invernadero — visión general') if hasattr(fig1.canvas, 'manager') else None

ax_T.plot(t_dias, T_ext, color=(0.6, 0.6, 0.6), linewidth=0.8, label='Exterior')
ax_T.plot(t_dias, T_int, 'r', linewidth=1.5, label='Interior')
ax_T.set_ylabel('T (°C)')
ax_T.set_title('Temperatura interior vs exterior')
ax_T.legend(loc='upper left')
ax_T.grid(True)

ax_H.plot(t_dias, H_ext, color=(0.6, 0.6, 0.6), linewidth=0.8, label='Exterior')
ax_H.plot(t_dias, H_int, 'b', linewidth=1.5, label='Interior')
ax_H.set_ylabel('HR (%)')
ax_H.set_title('Humedad relativa')
ax_H.legend(loc='upper left')
ax_H.grid(True)

ax_C.plot(t_dias, CO2_int, color=(0.2, 0.6, 0.2), linewidth=1.2)
ax_C.axhline(1200, color='r', linestyle='--', label='Límite alerta')
ax_C.set_ylabel('CO₂ (ppm)')
ax_C.set_title('CO₂ interior')
ax_C.legend(loc='upper left')
ax_C.grid(True)

ax_V.plot(t_dias, viento, color=(0.4, 0.4, 0.8), linewidth=1.0)
ax_V.set_ylabel('Viento (m/s)')
ax_V.set_xlabel('Día')
ax_V.set_title('Viento exterior')
ax_V.grid(True)

ax_V.set_xticks(range(8))
ax_V.set_xticklabels(['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom', 'Lun'])

fig1.tight_layout()
fig1_path = os.path.join(script_dir, 'invernadero_general.png')
fig1.savefig(fig1_path, dpi=150)
print(f'Figura guardada: {fig1_path}')

# --- 9. Figura de zoom: eventos anómalos ---
fig2, (ax_z1, ax_z2) = plt.subplots(1, 2, figsize=(11, 5))

# Zoom fallo calefacción (día 3, ventana ±6 horas)
ax_z1.plot(t_dias, T_int, 'r', linewidth=1.4)
ax_z1.set_xlim(3 - 0.25, 3 + 0.35)
ax_z1.set_xlabel('Día')
ax_z1.set_ylabel('T interior (°C)')
ax_z1.set_title('Evento A — Fallo calefacción (día 3)')
ax_z1.axvline(3, color='k', linestyle='--', label='Fallo')
ax_z1.legend()
ax_z1.grid(True)

# Zoom fallo ventilación (día 5, ventana ±6 horas)
ax_z2.plot(t_dias, CO2_int, color=(0.2, 0.6, 0.2), linewidth=1.4)
ax_z2.set_xlim(5 - 0.25, 5 + 0.40)
ax_z2.set_xlabel('Día')
ax_z2.set_ylabel('CO₂ (ppm)')
ax_z2.set_title('Evento B — Fallo ventilación (día 5)')
ax_z2.axvline(5, color='k', linestyle='--', label='Fallo')
ax_z2.axhline(1200, color='r', linestyle='--', label='Límite alerta')
ax_z2.legend()
ax_z2.grid(True)

fig2.tight_layout()
fig2_path = os.path.join(script_dir, 'invernadero_zoom_eventos.png')
fig2.savefig(fig2_path, dpi=150)
print(f'Figura guardada: {fig2_path}')
