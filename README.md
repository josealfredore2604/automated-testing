# Proyecto de Automatización de Pruebas

Este proyecto contiene una aplicación web construida con FastAPI y un conjunto de pruebas automatizadas que utilizan Cypress, Playwright y Selenium. El objetivo es demostrar diferentes enfoques de automatización end-to-end y la aplicación de Page Object Model (POM) en Playwright.

---

## Contenido del proyecto

### 1. Aplicación FastAPI

La aplicación ubicada en `src/main.py` expone un pequeño sistema de autenticación y gestión de tareas. Incluye:

* Página de inicio de sesión.
* Validación de credenciales.
* Dashboard con tareas en memoria.
* Creación de tareas con prioridad.
* Cierre de sesión.

La aplicación usa almacenamiento temporal en una lista (`DB_TAREAS`) y no utiliza base de datos.

### 2. Pruebas con Cypress

Las pruebas ubicadas en `cypress/e2e/spec.cy.js` realizan:

* Inicio de sesión.
* Navegación al dashboard.
* Creación de una tarea.
* Verificación de contenido en la lista de tareas.

Para ejecutar Cypress:

```
npx cypress open
```

o en modo headless:

```
npx cypress run
```

### 3. Pruebas con Playwright (POM)

En `tests/e2e_playwright/` se encuentra un ejemplo de diseño Page Object Model incluyendo:

* `LoginPage`
* `DashboardPage`
* Pruebas E2E con validaciones automáticas

Para ejecutar Playwright:

```
pytest tests/e2e_playwright
```

Antes de la primera ejecución es necesario instalar los navegadores:

```
playwright install
```

### 4. Pruebas con Selenium

El archivo `tests/legacy/test_selenium.py` contiene:

* Flujo completo: login, creación de tarea y logout.
* Prueba de error en inicio de sesión.

Para ejecutarlo:

```
pytest tests/legacy
```

Es necesario tener el driver de Chrome configurado y accesible en el sistema.

---

## Requisitos

### Dependencias de Python

Administradas por `pyproject.toml` (FastAPI, Playwright, Selenium, pytest).

Instalación:

```
pip install -r requirements.txt
```

o si estás usando uv:

```
uv sync
```

### Dependencias de Node

Requeridas para Cypress:

```
npm install
```

---

## Ejecutar la aplicación FastAPI

Desde la carpeta del proyecto:

```
uvicorn src.main:app --reload --port 8000
```

La aplicación quedará disponible en:

```
http://127.0.0.1:8000
```

---

## Estructura del proyecto

```
src/
  main.py              # Aplicación FastAPI

tests/
  e2e_playwright/
    pages/             # Page Objects
    test_main_flow.py  # Pruebas con Playwright
  legacy/              # Pruebas con Selenium
  ...

cypress/
  e2e/                 # Pruebas Cypress
  fixtures/
  support/

package.json
pyproject.toml
README.md
```

---

## Objetivo del proyecto

El objetivo principal es mostrar cómo realizar pruebas automatizadas con distintos frameworks y técnicas modernas siguiendo buenas prácticas como Page Object Model, flujos E2E completos y validaciones de interfaz.