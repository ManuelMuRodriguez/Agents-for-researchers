# 🤖 GitHub Copilot para Investigadores

> Curso práctico de 45 minutos para aprender a usar la IA como agente dentro de Visual Studio Code.

---

## 📋 Descripción

Este repositorio contiene todos los materiales del curso **"GitHub Copilot para Investigadores"**: guion del profesor, guía del estudiante, ejemplos de código y recursos de referencia.

El objetivo es que investigadores con conocimientos básicos de MATLAB o R sean capaces de usar GitHub Copilot como agente dentro de VS Code para automatizar tareas habituales en su flujo de trabajo científico.

---

## 🎯 Objetivos del curso

Al terminar la sesión, los participantes sabrán:

- Usar **Copilot Chat** y el modo inline (`Ctrl+I`) dentro de VS Code
- Traducir scripts de **MATLAB a Python** con ayuda del agente
- Hacer su primer **commit en GitHub** usando lenguaje natural
- Generar un **Dockerfile** y lanzar un entorno reproducible con `docker-compose`

---

## ⏱ Estructura de la sesión (45 min)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| 01 · Intro y contexto | 7 min | ¿Qué es un agente IA en VS Code? Chat vs Inline |
| 02 · Copilot Chat | 10 min | Primeras demos: abrir Chat, Ctrl+I, explicar un script |
| 03 · Casos de uso | 12 min | MATLAB→Python · Git · Docker |
| 04 · Práctica guiada | 16 min | Los participantes en el teclado, el profesor guía |

---

## 🛠 Requisitos previos

Instala todo esto **antes de venir al curso**. No habrá tiempo para instalaciones durante la sesión.

| Herramienta | Versión mínima | Enlace |
|-------------|---------------|--------|
| Visual Studio Code | 1.85+ | [Descargar](https://code.visualstudio.com) |
| GitHub Copilot (extensión) | última | Buscar en el marketplace de VS Code |
| Git | 2.40+ | [Descargar](https://git-scm.com) |
| Docker Desktop | 4.25+ | [Descargar](https://www.docker.com/products/docker-desktop) |

> **Nota:** Para usar GitHub Copilot necesitas una cuenta de GitHub con Copilot activo (gratuito para investigadores a través del programa GitHub Education).

---

## 📁 Estructura del repositorio

```
.
├── README.md                  # Este archivo
├── guion_profesor.md          # Guion detallado con tiempos y consejos
├── ejemplos/
│   ├── script_matlab.m        # Script de ejemplo para traducir
│   ├── script_python.py       # Resultado esperado tras traducción
│   └── docker-compose.yml     # Ejemplo de entorno reproducible
└── recursos/
    └── prompts_utiles.md      # Colección de prompts para investigadores
```

---

## 🚀 Cómo usar este repositorio

1. **Clona el repositorio** antes de la sesión:
   ```bash
   git clone https://github.com/TU_USUARIO/copilot-para-investigadores.git
   cd copilot-para-investigadores
   ```

2. **Abre la carpeta en VS Code:**
   ```bash
   code .
   ```

3. **Durante la sesión**, sigue el guion en `guion_profesor.md` o la guía en pantalla.

---

## 💡 Prompts de ejemplo

Aquí tienes algunos prompts de arranque para usar durante la sesión:

```
"Traduce este script de MATLAB a Python manteniendo los mismos comentarios"
"Explícame qué hace esta función línea a línea"
"Genera un Dockerfile para ejecutar este script de Python"
"Escribe el mensaje de commit para estos cambios"
"Crea un docker-compose.yml que incluya Python 3.11 y Jupyter"
```

---

## 🧭 Chat en VS Code: `Compactar` y menú `@`

### ¿Qué significa `Compactar`?

- Resume la conversación larga para conservar lo importante y reducir ruido.
- Mejora la velocidad y la calidad cuando el chat ya tiene mucho historial.
- No borra ni modifica archivos del proyecto: solo compacta el contexto del chat.

### ¿Qué es el menú `@`?

Cuando escribes `@` en Copilot Chat, eliges una fuente de contexto o una capacidad concreta.
Las opciones exactas dependen de las herramientas activas en tu VS Code.

Opciones habituales en este curso:

- `@workspace` o `@codebase`: analiza todo el proyecto.
- `@changes`: se centra en los cambios de Git (diffs).
- `@agent`: delega una tarea larga a un subagente.
- `@configurePythonEnvironment`: ayuda a configurar el entorno Python.
- `@configureNotebook`: prepara kernels de notebook.

Opciones avanzadas (si hay herramientas conectadas):

- `@browser`, `@clickElement`: automatización básica del navegador.
- `@collection-schema`, `@collection-indexes`, `@aggregate`: consultas y análisis de MongoDB.

Regla rápida para clase:

- Usa `@codebase` para entender un proyecto grande.
- Usa `@changes` para revisar qué se ha modificado.
- Usa `@agent` cuando la tarea tenga varios pasos.

---

## 📚 Recursos para seguir

- [Documentación oficial de GitHub Copilot](https://docs.github.com/en/copilot)
- [GitHub Education para investigadores](https://education.github.com)
- [VS Code: guía de Copilot Chat](https://code.visualstudio.com/docs/copilot/overview)
- [Docker para ciencia reproducible](https://docs.docker.com/guides/use-case/jupyter/)

---

## 📄 Licencia

Este material está disponible bajo licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Puedes usarlo, adaptarlo y redistribuirlo citando la fuente.

---

*Curso preparado para investigadores · Sesión 1 de N*
