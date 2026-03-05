# 🌱 API Sistema de Riego Automatizado

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Flask-RESTX](https://img.shields.io/badge/Flask--RESTX-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Arquitectura](https://img.shields.io/badge/Arquitectura-MVC- purple)

API RESTful profesional para el monitoreo y control de un sistema de riego automatizado. Desarrollada con Flask y Flask-RESTX siguiendo una arquitectura por capas (MVC) para garantizar escalabilidad y mantenibilidad.

## 📋 Características

- **Monitoreo en tiempo real** de sensores:
  - 🌡️ Temperatura ambiente
  - 💧 Humedad ambiente
  - 🌱 Humedad del suelo

- **Control de actuadores**:
  - 💦 Bomba de agua (encendido/apagado)

- **Historial de datos**:
  - Almacenamiento de los últimos 7 días
  - Promedios diarios para visualización en gráficas

- **Arquitectura profesional**:
  - Separación en capas (Models, Routes, Services)
  - Documentación automática con Swagger UI
  - Manejo centralizado de extensiones

## 🛠️ Stack Tecnológico

![Tecnologías](https://skillicons.dev/icons?i=python,flask,git,github,vscode)

### Backend
| Tecnología | Versión | Uso |
|------------|---------|-----|
| **Python** | 3.8+ | Lenguaje de programación base |
| **Flask** | 2.0+ | Framework web principal |
| **Flask-RESTX** | 1.0+ | API RESTful con Swagger automático |
| **Flask-CORS** | 3.0+ | Habilitar CORS para Flutter/Web |
| **Python-dotenv** | 0.19+ | Gestión de variables de entorno |

## 📁 Estructura del Proyecto (MVC)
sistema-riego-api/
├── 📂 src/
│ ├── 📂 models/ # Capa de Modelos
│ │ └── riego_models.py # Modelos de datos (sensores, bomba)
│ │
│ ├── 📂 routes/ # Capa de Controladores/Rutas
│ │ └── riego_routes.py # Endpoints de la API
│ │
│ └── 📂 services/ # Capa de Servicios/Lógica de negocio
│ └── riego_service.py # Lógica de almacenamiento y procesamiento
│
├── 📂 pycache/ # Archivos compilados de Python
│
├── app.py # Punto de entrada de la aplicación
├── config.py # Configuraciones y variables de entorno
├── extensions.py # Inicialización de extensiones Flask
