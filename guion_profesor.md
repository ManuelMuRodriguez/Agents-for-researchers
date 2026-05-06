# Guion del Profesor — GitHub Copilot para Investigadores

> **Uso interno — no distribuir a los participantes**
> Sesión de 45 minutos · Nivel: usuarios de MATLAB/R con algo de código

---

## Antes de empezar (llegada al aula)

- [ ] Abre VS Code con la carpeta del proyecto clonada
- [ ] Ten abierto `script_matlab.m` en un tab y `docker-compose.yml` en otro
- [ ] Panel de Copilot Chat visible en la barra lateral
- [ ] Resolución del proyector comprobada
- [ ] Apaga Slack/notificaciones del ordenador

---

## Bloque 01 · Intro y contexto `[0:00 – 7:00]`

**Objetivo:** Que entiendan qué es un agente IA y cómo cambia su flujo de trabajo.

### Qué decir

> *"Todos usáis herramientas para escribir código: MATLAB, R, scripts de bash. Hoy vamos a añadir un compañero de trabajo que entiende lo que estáis haciendo y puede ayudaros a escribir, traducir, documentar y depurar código usando lenguaje normal."*

- Copilot **no es un buscador**: conoce el contexto de tus ficheros
- Dos modos: **Chat lateral** (para tareas grandes) y **Inline `Ctrl+I`** (para editar directamente)
- Hoy vamos a hacer exactamente lo que haréis en vuestro laboratorio

### Pregunta para el grupo

> *"¿Cuántos tenéis algún script de MATLAB o R que lleváis años sin tocar porque 'funciona y no lo toques'? Pues hoy vamos a hacer que Copilot lo entienda por vosotros."*

---

## Bloque 02 · Primeras demos con Copilot Chat `[7:00 – 17:00]`

**Objetivo:** Que vean el Chat y el Inline en acción antes de tocarlos ellos.

### Demo 1 — Abrir Copilot Chat y hacer una pregunta (2 min)

1. Abre el panel lateral de Copilot Chat
2. Escribe: `@workspace explícame qué hace este proyecto`
3. Muestra la respuesta y señala que **conoce todos los ficheros**

### Demo 2 — Inline con `Ctrl+I` (3 min)

1. Abre `script_matlab.m`
2. Selecciona una función entera
3. Pulsa `Ctrl+I` y escribe: `añade un comentario explicando qué hace cada paso`
4. Acepta con un clic — muestra el botón de aceptar/rechazar

### Demo 3 — Explicar un script entero (5 min)

1. Con `script_matlab.m` abierto, en el Chat escribe:
   `Explícame este script línea a línea como si yo no supiera MATLAB`
2. Deja que responda y lee un fragmento en voz alta

> ⚠️ **Consejo:** Si la respuesta tarda, aprovecha para preguntar al grupo qué esperan que diga.

---

## Bloque 03 · Casos de uso reales `[17:00 – 29:00]`

**Objetivo:** Ver tres tareas reales que podrían hacer hoy mismo en su investigación.

### Caso A — Traducir MATLAB a Python `[17:00 – 22:00]` ⭐ DEMO PRINCIPAL

1. Abre `script_matlab.m`
2. En el Chat escribe:
   ```
   Traduce este script de MATLAB a Python 3.
   Mantén los mismos comentarios y la misma lógica.
   ```
3. Copia el resultado en un nuevo archivo `script_python.py`
4. Señala que **Copilot ha mantenido los comentarios y la estructura**

> 💡 **Frase de impacto:** *"Esto que acaba de hacer en 30 segundos, a mí me habría costado media mañana buscando equivalencias en Stack Overflow."*

### Caso B — Primer commit con Git `[22:00 – 25:00]`

1. Abre la terminal en VS Code
2. Escribe en el Chat: `escribe un mensaje de commit para los cambios que acabamos de hacer`
3. Copia el mensaje y haz el commit:
   ```bash
   git add script_python.py
   git commit -m "[mensaje que generó Copilot]"
   ```

> 💡 **Nota:** No hace falta hacer push en directo. Solo enseña el commit local.

### Caso C — Generar un Dockerfile `[25:00 – 29:00]`

1. En el Chat escribe:
   ```
   Genera un Dockerfile para ejecutar script_python.py
   con Python 3.11 y las librerías que necesite
   ```
2. Crea el archivo con la respuesta
3. Muestra el `docker-compose.yml` de ejemplo ya preparado

---

## Bloque 04 · Práctica guiada `[29:00 – 45:00]`

**Objetivo:** Que ellos usen Copilot con sus propios ficheros o con los ejemplos del repo.

### Instrucciones para el grupo

> *"Ahora sois vosotros. Tenéis 16 minutos para probar al menos UNA de estas tres tareas. Si habéis traído un script propio, usadlo. Si no, usad los ejemplos de la carpeta."*

### Tareas sugeridas (en la pantalla)

1. Pide a Copilot que explique `script_matlab.m`
2. Tradúcelo a Python
3. Pide un Dockerfile para tu script

### Tu rol durante este bloque

- Pasea por la sala y ayuda a quien se atasque
- Si ves un error interesante, muéstralo en el proyector
- A los 5 minutos, pregunta en voz alta: *"¿Quién ha conseguido traducir el script? ¿Alguna sorpresa?"*

### Cierre `[43:00 – 45:00]`

> *"Lo que habéis hecho hoy — traducir código, documentar, crear un entorno reproducible — es exactamente lo que podéis hacer mañana en vuestro laboratorio. Copilot no sustituye vuestro conocimiento científico, pero sí os ahorra la parte mecánica."*

- Señala el README del repo con los recursos
- Recuerda el programa GitHub Education si no tienen Copilot activo
- Deja 2 minutos para preguntas

---

## Preguntas frecuentes

**"¿Es seguro subir mi código a Copilot?"**
> Anthropic y GitHub tienen políticas claras de privacidad. Para datos sensibles, existe GitHub Copilot for Business con garantías adicionales. Para código de investigación sin datos personales, el uso estándar es seguro.

**"¿Puede equivocarse?"**
> Sí, siempre. Copilot es un asistente, no un oráculo. Siempre hay que revisar el código que genera. Úsalo como un borrador inteligente, no como código de producción sin revisar.

**"¿Funciona con R?"**
> Sí. Prueba: `Traduce este script de R a Python` o `Explícame qué hace esta función de R`.

---

*Guion preparado para la Sesión 1 · Actualizado mayo 2026*
