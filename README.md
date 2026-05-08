<p align="center">
  <img src="recursos/img/arm-logo-render.png" alt="Logo grupo de investigación" height="90" />
</p>

# 🤖 GitHub Copilot para Investigadores

> Curso práctico de ~60 minutos para aprender a usar la IA como agente dentro de Visual Studio Code.

---

## 📋 Descripción

Este repositorio contiene todos los materiales del curso **"GitHub Copilot para Investigadores"**: guion del profesor, ejemplos de código MATLAB y Python, infraestructura Docker y recursos de referencia.

El objetivo es que investigadores con conocimientos de MATLAB sean capaces de usar GitHub Copilot como agente dentro de VS Code para automatizar tareas habituales en su flujo de trabajo científico: traducción de código, documentación, control de versiones y reproducibilidad de entornos.

---

## 🎯 Objetivos del curso

Al terminar la sesión, los participantes sabrán:

- Usar **Copilot Chat** y el modo inline (`Ctrl+I`) dentro de VS Code
- Traducir scripts de **MATLAB a Python** con ayuda del agente
- Hacer **commits en GitHub** usando lenguaje natural para los mensajes
- Lanzar un entorno reproducible con `docker compose up`

---

## ⏱ Estructura de la sesión (~60 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| 01 · Contexto y motivación | 10 min | Qué es un agente IA en VS Code, Chat vs Inline |
| 02 · Chat e Inline en VS Code | 10 min | Primeras demos, menú @, compactar historial |
| 03 · MATLAB en VS Code | 10 min | Extensión, F5, traducción a Python |
| 04 · Git y GitHub | 10 min | Commit asistido, push, control de versiones |
| 05 · Docker y reproducibilidad | 10 min | docker compose up, entornos reproducibles |
| 06 · Práctica guiada | 10 min | Caso real: sensores de invernadero |

---

## 🛠 Requisitos previos

Instala todo esto **antes de venir al taller**. Consulta la [guía de instalación detallada](recursos/guia_instalacion.md).

| Herramienta | Enlace |
|-------------|--------|
| Visual Studio Code | [code.visualstudio.com](https://code.visualstudio.com) |
| Cuenta de GitHub (con Copilot activo) | [education.github.com](https://education.github.com) |
| Git | [git-scm.com](https://git-scm.com) |
| Docker Desktop | [docs.docker.com/desktop](https://docs.docker.com/desktop) |
| MATLAB (si lo usas en tu investigación) | Licencia institucional |

**Comprobación rápida antes del taller:**
```bash
git --version
docker --version
docker compose version
```

---

## 📁 Estructura del repositorio

```
.
├── README.md                              # Este archivo
├── guion_profesor.md                      # Guion detallado con tiempos y frases de clase
├── copilot_investigadores_v2.pptx         # Presentación PowerPoint del curso
│
├── Ejercicios/
│   ├── Ejer1/                             # Ejercicio principal — sensores de invernadero
│   │   ├── invernadero.m                  # Script MATLAB: genera 7 días de datos sintéticos
│   │   ├── dataset_invernadero.csv        # Dataset generado por invernadero.m
│   │   ├── docker-compose.yml             # Entorno reproducible (Python 3.11-slim)
│   │   └── requirements.txt              # Dependencias Python con versiones fijadas
│   └── Ejer2/                             # Ejercicio avanzado — identificación de sistemas
│       ├── Identifica_ARX_221.m           # Modelo ARX real: T. interior ← radiación, viento, ventilación
│       ├── 2020_11_15.mat                 # Datos reales de entrenamiento (15-Nov-2020)
│       └── 2020_11_16.mat                 # Datos reales de validación (16-Nov-2020)
│
├── paper/
│   ├── main.tex                           # Template LaTeX Elsevier (elsarticle)
│   ├── main.pdf                           # PDF compilado
│   ├── referencias.bib                    # Bibliografía BibTeX de ejemplo
│   └── figuras/                           # Carpeta para figuras del paper
│
└── recursos/
    ├── prompts_utiles.md                  # Colección de prompts para la sesión práctica
    ├── guia_instalacion.md                # Guía paso a paso de instalación y configuración
    ├── presentacion_curso.html            # Presentación interactiva del curso (HTML)
    └── img/                               # Imágenes y logos
```

---

## 🚀 Cómo usar este repositorio

1. **Clona el repositorio** antes de la sesión:
   ```bash
   git clone https://github.com/ManuelMuRodriguez/Agents-for-researchers.git
   cd Agents-for-researchers
   ```

2. **Abre la carpeta en VS Code:**
   ```bash
   code .
   ```

3. **Abre la presentación** en `recursos/presentacion_curso.html` con tu navegador
   o la versión PowerPoint `copilot_investigadores_v2.pptx`.

4. **Durante la sesión**, sigue el guion en `guion_profesor.md`.

---

## 🧑‍🔬 Ejercicio 1 — Sensores de invernadero

El ejemplo central del curso es `Ejercicios/Ejer1/invernadero.m`: un script MATLAB que genera 7 días de datos sintéticos de sensores de invernadero (temperatura interior/exterior, humedad, CO₂ y viento) con dos eventos de fallo simulados.

Los participantes usan Copilot para:
1. Entender el script con `@workspace`
2. Traducirlo a Python (`invernadero.py`)
3. Ejecutarlo con `docker compose up` desde `Ejercicios/Ejer1/`
4. Añadir nuevas funcionalidades (heatmaps, resumen diario, correlación, dashboard HTML)

---

## 🔬 Ejercicio 2 — Identificación de sistemas (ARX)

`Ejercicios/Ejer2/Identifica_ARX_221.m` trabaja con datos reales de un invernadero (noviembre 2020). Identifica un modelo ARX de orden 221 que predice la **temperatura interior** a partir de radiación solar, apertura de ventilación y velocidad del viento, y lo valida con datos del día siguiente.

Ideal para mostrar cómo Copilot ayuda a entender y traducir código de ingeniería de control avanzado.

---

## 💡 Prompts de ejemplo

```
@workspace explícame qué hace este proyecto y por dónde empieza la ejecución

Traduce este script de MATLAB a Python 3.
Usa numpy para calculos, pandas para CSV y matplotlib para graficas.
Manten la estructura de secciones y comentarios.

Escribe el mensaje de commit para los cambios actuales
```

---

## 🧭 Chat en VS Code: `Compactar` y menú `@`

**Compactar** resume la conversación larga del chat para quitar ruido sin tocar los archivos del proyecto. Útil cuando el historial se hace muy largo y las respuestas pierden calidad.

**Menú `@`** — opciones habituales en este curso:

| Opción | Cuándo usarla |
|--------|--------------|
| `@codebase` / `@workspace` | Entender un proyecto grande completo |
| `@changes` | Revisar qué se ha modificado recientemente |
| `@agent` | Tareas largas de varios pasos automatizados |
| `@terminal` | Interactuar con la terminal desde el chat |

Regla de oro: **primero contexto (`@codebase`), luego cambios**.

---

## 📚 Recursos para seguir

- [Documentación oficial de GitHub Copilot](https://docs.github.com/en/copilot)
- [GitHub Education para investigadores](https://education.github.com)
- [VS Code: guía de Copilot Chat](https://code.visualstudio.com/docs/copilot/overview)
- [Docker para ciencia reproducible](https://docs.docker.com/guides/use-case/jupyter/)
