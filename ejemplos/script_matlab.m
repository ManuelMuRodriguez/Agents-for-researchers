% =========================================================
% Análisis de señal de vibración de un motor
% Simula la lectura de un acelerómetro, filtra el ruido
% y calcula métricas estadísticas básicas.
% =========================================================

%% Parámetros de la señal
fs = 1000;          % Frecuencia de muestreo (Hz)
t_total = 2;        % Duración de la medición (segundos)
t = 0:1/fs:t_total; % Vector de tiempo

freq_motor = 50;    % Frecuencia fundamental del motor (Hz)
amplitud   = 2.5;   % Amplitud de la vibración (m/s²)

%% Generación de señal sintética (motor + ruido de sensor)
ruido     = 0.4 * randn(size(t));
vibracion = amplitud * sin(2*pi*freq_motor*t) + ...
            0.8 * sin(2*pi*2*freq_motor*t) + ...  % 2º armónico
            ruido;

%% Filtrado por media móvil (ventana de 10 muestras)
ventana          = 10;
vibracion_suave  = movmean(vibracion, ventana);

%% Métricas estadísticas
media   = mean(vibracion);
desv    = std(vibracion);
pico    = max(abs(vibracion));
rms     = rms(vibracion);

fprintf('--- Métricas de la señal ---\n');
fprintf('Media      : %.4f m/s²\n', media);
fprintf('Desv. típ. : %.4f m/s²\n', desv);
fprintf('Pico       : %.4f m/s²\n', pico);
fprintf('RMS        : %.4f m/s²\n', rms);

%% Representación gráfica
figure('Name', 'Análisis de vibración');

subplot(2,1,1);
plot(t, vibracion, 'Color', [0.6 0.6 0.6], 'LineWidth', 0.8);
hold on;
plot(t, vibracion_suave, 'b', 'LineWidth', 1.8);
xlabel('Tiempo (s)');
ylabel('Aceleración (m/s²)');
title('Señal de vibración — cruda vs filtrada');
legend('Señal cruda', 'Media móvil');
grid on;

subplot(2,1,2);
N   = length(vibracion);
f   = (0:N-1) * (fs/N);
Y   = abs(fft(vibracion)) / N;
plot(f(1:N/2), 2*Y(1:N/2), 'r', 'LineWidth', 1.2);
xlabel('Frecuencia (Hz)');
ylabel('Amplitud');
title('Espectro de frecuencias (FFT)');
xlim([0 200]);
grid on;
