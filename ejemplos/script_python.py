# =========================================================
# Análisis de señal de vibración de un motor
# Simula la lectura de un acelerómetro, filtra el ruido
# y calcula métricas estadísticas básicas.
# =========================================================

import numpy as np
import matplotlib.pyplot as plt

# %% Parámetros de la señal
fs = 1000           # Frecuencia de muestreo (Hz)
t_total = 2         # Duración de la medición (segundos)
t = np.arange(0, t_total, 1 / fs)  # Vector de tiempo

freq_motor = 50     # Frecuencia fundamental del motor (Hz)
amplitud = 2.5      # Amplitud de la vibración (m/s²)

# %% Generación de señal sintética (motor + ruido de sensor)
rng = np.random.default_rng(seed=42)
ruido = 0.4 * rng.standard_normal(len(t))
vibracion = (
    amplitud * np.sin(2 * np.pi * freq_motor * t)
    + 0.8 * np.sin(2 * np.pi * 2 * freq_motor * t)  # 2º armónico
    + ruido
)

# %% Filtrado por media móvil (ventana de 10 muestras)
ventana = 10
vibracion_suave = np.convolve(vibracion, np.ones(ventana) / ventana, mode="same")

# %% Métricas estadísticas
media = np.mean(vibracion)
desv = np.std(vibracion)
pico = np.max(np.abs(vibracion))
rms = np.sqrt(np.mean(vibracion**2))

print("--- Métricas de la señal ---")
print(f"Media      : {media:.4f} m/s²")
print(f"Desv. típ. : {desv:.4f} m/s²")
print(f"Pico       : {pico:.4f} m/s²")
print(f"RMS        : {rms:.4f} m/s²")

# %% Representación gráfica
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
fig.suptitle("Análisis de vibración")

# Señal cruda vs filtrada
ax1.plot(t, vibracion, color="0.6", linewidth=0.8, label="Señal cruda")
ax1.plot(t, vibracion_suave, color="blue", linewidth=1.8, label="Media móvil")
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Aceleración (m/s²)")
ax1.set_title("Señal de vibración — cruda vs filtrada")
ax1.legend()
ax1.grid(True)

# Espectro de frecuencias (FFT)
N = len(vibracion)
f = np.arange(N) * (fs / N)
Y = np.abs(np.fft.fft(vibracion)) / N

ax2.plot(f[: N // 2], 2 * Y[: N // 2], color="red", linewidth=1.2)
ax2.set_xlabel("Frecuencia (Hz)")
ax2.set_ylabel("Amplitud")
ax2.set_title("Espectro de frecuencias (FFT)")
ax2.set_xlim(0, 200)
ax2.grid(True)

plt.tight_layout()
plt.show()
