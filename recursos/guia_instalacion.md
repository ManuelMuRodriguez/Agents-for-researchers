# Guia de instalacion y configuracion previa al taller

Sigue los pasos en orden. Al final de cada sección hay una comprobación rápida para confirmar que todo funciona.

---

## 1. Visual Studio Code

### Instalación

1. Ve a [https://code.visualstudio.com](https://code.visualstudio.com)
2. Descarga el instalador para tu sistema operativo (Windows, macOS o Linux)
3. Ejecuta el instalador y acepta las opciones por defecto

### Comprobación

Abre VS Code. Debe arrancar sin errores y mostrar la pantalla de bienvenida.

---

## 2. Cuenta en GitHub

### Si no tienes cuenta

1. Ve a [https://github.com](https://github.com) y haz clic en **Sign up**
2. Elige un nombre de usuario, correo y contraseña
3. Verifica tu correo electrónico

### Acceso gratuito para investigadores y estudiantes

Si tienes correo institucional (universidad o centro de investigación):

1. Ve a [https://education.github.com](https://education.github.com)
2. Haz clic en **Get benefits** → **Students** o **Researchers**
3. Introduce tu correo institucional y sigue el proceso de verificación
4. Una vez aprobado, tendrás acceso gratuito a GitHub Copilot

### Comprobación

Inicia sesión en [github.com](https://github.com). Debes ver tu perfil sin problemas.

---

## 3. Git

### macOS

Abre una terminal y ejecuta:

```bash
git --version
```

Si no está instalado, macOS te ofrecerá instalarlo automáticamente. También puedes instalar las **Xcode Command Line Tools**:

```bash
xcode-select --install
```

Alternativa con Homebrew:

```bash
brew install git
```

### Windows

Descarga el instalador desde [https://git-scm.com/download/win](https://git-scm.com/download/win) y ejecutalo con las opciones por defecto.

### Linux (Debian/Ubuntu)

```bash
sudo apt update && sudo apt install git
```

### Configuración obligatoria tras instalar

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
```

### Comprobación

```bash
git --version
git config --global user.name
git config --global user.email
```

Los tres comandos deben devolver valores sin errores.

---

## 4. Docker Desktop

### Instalación

1. Ve a [https://docs.docker.com/desktop](https://docs.docker.com/desktop)
2. Selecciona tu sistema operativo y descarga el instalador
3. Ejecuta el instalador y sigue los pasos (puede pedir reiniciar el equipo)
4. Abre Docker Desktop y espera a que el icono de la ballena aparezca estable en la barra del sistema

> **Windows:** Docker Desktop requiere WSL 2. El instalador lo configura automáticamente, pero necesitas que la virtualización esté activada en la BIOS.

> **macOS Apple Silicon (M1/M2/M3):** descarga la versión para **Apple Silicon**, no la de Intel.

### Comprobación

```bash
docker --version
docker compose version
```

Ambos deben mostrar un número de versión. Si Docker Desktop no está arrancado, el segundo comando fallará — asegúrate de que la aplicación está abierta.

---

## 5. MATLAB (solo si lo usas en tu investigación)

### Requisitos

- Licencia de MATLAB activa (individual, institucional o campus)
- MATLAB R2022b o posterior recomendado

### Instalación

1. Ve a [https://mathworks.com/downloads](https://mathworks.com/downloads)
2. Inicia sesión con tu cuenta de MathWorks (vinculada a tu licencia)
3. Descarga e instala MATLAB para tu sistema operativo
4. Durante la instalación selecciona al menos los toolboxes: **Signal Processing Toolbox** y **Statistics and Machine Learning Toolbox** (usados en los ejemplos del taller)

### Comprobación

Abre MATLAB. Ejecuta en la ventana de comandos:

```matlab
version
```

Debe mostrar la versión instalada sin errores.

---

## Comprobación global el día antes del taller

Abre una terminal y ejecuta los siguientes comandos uno a uno:

```bash
git --version
docker --version
docker compose version
code --version
```

Todos deben devolver un número de versión. Si alguno falla, revisa la sección correspondiente o escribe antes del taller.
