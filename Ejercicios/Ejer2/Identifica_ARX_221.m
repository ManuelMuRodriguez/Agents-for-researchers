%% Identificación y validación de modelo ARX de orden 221
%  Salida:  XTINV    - Temperatura interior del invernadero
%  Entradas: RAD     - Radiación solar
%            UVENT_cen - Apertura de ventilación
%            PVV     - Velocidad del viento
%  Orden ARX: na=2, nb=[2 2 2], nk=[1 1 1]

clear; close all; clc

Ts = 30;   % Tiempo de muestreo (segundos)

%% 1. Cargar datos de entrenamiento (2020_11_15)
load('2020_11_15.mat')

y_train  = XTINV;
u_train  = [PRAD, UVENT_cen, PVV];

N_train  = length(y_train);
T_train  = (0:N_train-1)' * Ts;   % vector de tiempos (segundos)

% Eliminar medias
y_mean_train = mean(y_train);
u_mean_train = mean(u_train);
y_train_dm   = y_train - y_mean_train;
u_train_dm   = u_train - u_mean_train;

%% 2. Crear objeto iddata para identificación
datos_train = iddata(y_train_dm, u_train_dm, Ts, ...
    'OutputName',  'Temp. Interior', ...
    'OutputUnit',  'ºC', ...
    'InputName',   {'Radiación Solar', 'Apertura Ventilación', 'Vel. Viento'}, ...
    'InputUnit',   {'W/m²', '%', 'm/s'});

%% 3. Identificar modelo ARX 221
%  na=2 (polos), nb=[2 2 2] (ceros+1 por entrada), nk=[1 1 1] (retardo)
na = 2;
nb = [2 2 2];
nk = [1 1 1];

modelo_arx = arx(datos_train, [na nb nk]);

disp('=== Modelo ARX identificado ===')
present(modelo_arx)

%% 4. Cargar datos de validación (2020_11_16)
clear XTINV PRAD UVENT_cen PVV

load('2020_11_16.mat')

y_val  = XTINV;
u_val  = [PRAD, UVENT_cen, PVV];

N_val  = length(y_val);
T_val  = (0:N_val-1)' * Ts;   % vector de tiempos (segundos)

% Eliminar medias
y_mean_val = mean(y_val);
u_mean_val = mean(u_val);
y_val_dm   = y_val - y_mean_val;
u_val_dm   = u_val - u_mean_val;

datos_val = iddata(y_val_dm, u_val_dm, Ts, ...
    'OutputName',  'Temp. Interior', ...
    'OutputUnit',  'ºC', ...
    'InputName',   {'Radiación Solar', 'Apertura Ventilación', 'Vel. Viento'}, ...
    'InputUnit',   {'W/m²', '%', 'm/s'});

%% 5. Validación: comparación salida real vs predicha
figure('Name', 'Validación modelo ARX 221', 'NumberTitle', 'off')
compare(datos_val, modelo_arx)
title('Validación ARX 221 — 2020-11-16')
grid on

%% 6. Análisis de residuos
figure('Name', 'Análisis de residuos', 'NumberTitle', 'off')
resid(datos_val, modelo_arx)

%% 7. Predicción un paso adelante y simulación libre
[y_pred, fit_pred, ic] = compare(datos_val, modelo_arx, 1);   % 1 paso
[y_sim,  fit_sim,  ~]  = compare(datos_val, modelo_arx, Inf); % simulación libre

fprintf('\n=== Bondad del ajuste (Fit %%) ===\n')
fprintf('  Predicción 1 paso : %.2f %%\n', fit_pred)
fprintf('  Simulación libre  : %.2f %%\n', fit_sim)

%% 8. Representación temporal (se suma la media para mostrar ºC reales)
figure('Name', 'Comparación temporal', 'NumberTitle', 'off')
subplot(2,1,1)
plot(T_val, y_val, 'b', 'DisplayName', 'Real'); hold on
plot(y_pred.SamplingInstants, y_pred.OutputData + y_mean_val, 'r--', ...
    'DisplayName', 'ARX (pred. 1 paso)')
grid on; legend; ylabel('Temperatura (ºC)')
title(sprintf('Predicción 1 paso adelante  —  Fit = %.2f %%', fit_pred))

subplot(2,1,2)
plot(T_val, y_val, 'b', 'DisplayName', 'Real'); hold on
plot(y_sim.SamplingInstants, y_sim.OutputData + y_mean_val, 'r--', ...
    'DisplayName', 'ARX (simulación libre)')
grid on; legend; ylabel('Temperatura (ºC)'); xlabel('Tiempo (s)')
title(sprintf('Simulación libre  —  Fit = %.2f %%', fit_sim))
