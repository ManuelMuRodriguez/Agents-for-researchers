% =========================================================
% Monitorización de sensores de invernadero
% Dataset sintético de 7 días (muestras cada 15 min)
% Variables: temperatura, humedad, CO2 y viento (interior/exterior)
% Incluye dos eventos: fallo de calefacción y fallo de ventilación
%
% Ejecutar completo: F5  (no "Run Section")
% =========================================================

rng(7);  % Semilla fija → resultados reproducibles

% --- 1. Vector de tiempo ---
dt      = 15 / (60*24);          % 15 min expresados en días
t_dias  = (0 : dt : 7-dt)';      % 7 días
N       = length(t_dias);
t_horas = t_dias * 24;           % Para cálculos de ciclos diarios

% Función de ciclo diario (seno con pico a la hora "pico")
ciclo = @(pico) sin(2*pi*(t_horas - pico) / 24);

% --- 2. Temperatura (°C) ---
T_ext = 15 + 8*ciclo(14) + 1.5*randn(N,1);            % Exterior: ciclo diario ±8°C
T_int = 22 + 1.2*ciclo(16) + 0.3*(T_ext-15) + 0.4*randn(N,1); % Interior: controlada ~22°C

% --- 3. Humedad relativa (%) ---
H_ext = 60 - 15*ciclo(14) + 5*randn(N,1);             % Exterior: más alta de noche
H_int = 70 -  5*ciclo(16) + 2*randn(N,1);             % Interior: controlada ~70%
H_ext = max(20, min(100, H_ext));
H_int = max(40, min(95,  H_int));

% --- 4. CO2 interior (ppm) ---
% Cae de día (fotosíntesis) y sube de noche (respiración)
luz     = max(0, ciclo(13));
CO2_int = 800 - 320*luz + 50*randn(N,1);
CO2_int = max(400, CO2_int);

% --- 5. Viento exterior (m/s) ---
viento = abs(3 + 2*randn(N,1));
% Racha de viento el día 2 (3 horas)
i_racha = round(2*24*4) : round(2*24*4 + 3*4);
viento(i_racha) = viento(i_racha) + 8*rand(numel(i_racha),1);

% --- 6. Eventos anómalos ---
% Evento A: fallo de calefacción en día 3 (2 horas) → bajada brusca T_int
i_fallo = round(3*24*4) : round(3*24*4 + 2*4);
T_int(i_fallo) = T_int(i_fallo) - 6*linspace(1,0,numel(i_fallo))';

% Evento B: fallo de ventilación en día 5 (3 horas) → pico de CO2
i_vent = round(5*24*4) : round(5*24*4 + 3*4);
CO2_int(i_vent) = CO2_int(i_vent) + 700*linspace(0,1,numel(i_vent))';

% --- 7. Guardar dataset en CSV ---
T_tabla = table(t_dias, T_ext, T_int, H_ext, H_int, CO2_int, viento, ...
    'VariableNames', {'dia','T_ext_C','T_int_C','H_ext_pct','H_int_pct','CO2_ppm','viento_ms'});
writetable(T_tabla, 'dataset_invernadero.csv');
fprintf('Dataset guardado: dataset_invernadero.csv (%d filas)\n', N);

% --- 8. Figura principal: 7 días completos ---
fig1 = figure('Name','Invernadero — visión general','Position',[50 50 1200 800]);

ax_T = subplot(4,1,1);
plot(t_dias, T_ext, 'Color',[0.6 0.6 0.6],'LineWidth',0.8); hold on;
plot(t_dias, T_int, 'r','LineWidth',1.5);
ylabel('T (°C)'); title('Temperatura interior vs exterior');
legend('Exterior','Interior','Location','northwest'); grid on;

ax_H = subplot(4,1,2);
plot(t_dias, H_ext, 'Color',[0.6 0.6 0.6],'LineWidth',0.8); hold on;
plot(t_dias, H_int, 'b','LineWidth',1.5);
ylabel('HR (%)'); title('Humedad relativa');
legend('Exterior','Interior','Location','northwest'); grid on;

ax_C = subplot(4,1,3);
plot(t_dias, CO2_int, 'Color',[0.2 0.6 0.2],'LineWidth',1.2);
ylabel('CO₂ (ppm)'); title('CO₂ interior');
yline(1200,'r--','Límite alerta','LabelHorizontalAlignment','left'); grid on;

ax_V = subplot(4,1,4);
plot(t_dias, viento, 'Color',[0.4 0.4 0.8],'LineWidth',1.0);
ylabel('Viento (m/s)'); xlabel('Día'); title('Viento exterior');
grid on;

linkaxes([ax_T, ax_H, ax_C, ax_V], 'x');
xticks(0:7); xticklabels({'Lun','Mar','Mié','Jue','Vie','Sáb','Dom','Lun'});

% --- 9. Figura de zoom: eventos anómalos ---
fig2 = figure('Name','Zoom — eventos anómalos','Position',[100 100 1100 500]);

% Zoom fallo calefacción (día 3, ventana ±6 horas)
ax_z1 = subplot(1,2,1);
plot(t_dias, T_int, 'r','LineWidth',1.4);
xlim([3 - 0.25, 3 + 0.35]);
xlabel('Día'); ylabel('T interior (°C)');
title('Evento A — Fallo calefacción (día 3)');
xline(3,'k--','Fallo','LabelVerticalAlignment','bottom'); grid on;

% Zoom fallo ventilación (día 5, ventana ±6 horas)
ax_z2 = subplot(1,2,2);
plot(t_dias, CO2_int, 'Color',[0.2 0.6 0.2],'LineWidth',1.4);
xlim([5 - 0.25, 5 + 0.40]);
xlabel('Día'); ylabel('CO₂ (ppm)');
title('Evento B — Fallo ventilación (día 5)');
xline(5,'k--','Fallo','LabelVerticalAlignment','bottom');
yline(1200,'r--','Límite alerta'); grid on;
