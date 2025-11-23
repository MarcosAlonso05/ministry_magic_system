# Ministry Magic System
proyecto implementa un sistema avanzado de gestión de hechizos y eventos mágicos para el Ministerio de Magia, desarrollado en Python utilizando FastAPI.

## Requisitos y Dependencias
Para la correcta ejecución del sistema, es necesario instalar las siguientes librerías de Python:
-fastapi: Framework para la API.
-uvicorn: Servidor ASGI.
-psutil: Para monitorización de hardware (CPU/RAM).
-prometheus-client: Para métricas de rendimiento.
-matplotlib: Para la generación de gráficos en el dashboard.
-httpx: Cliente HTTP asíncrono (usado para simulaciones).

Puedes instalarlas todas ejecutando el siguiente comando en tu terminal:
```
pip install fastapi uvicorn psutil prometheus-client matplotlib httpx
```

## Ejecución

Para iniciar el servidor, asegúrate de estar en la carpeta raíz del proyecto y ejecuta:
```
uvicorn app.main:app --reload
```

## Rutas del Sistema

- Simulador de Batalla (Frontend):
```http://127.0.0.1:8000/static/index.html```
Interfaz gráfica completa para crear magos, seleccionar personajes y luchar.

- Dashboard de Métricas:
```http://127.0.0.1:8000/dashboard/stats```
Visualización en tiempo real del rendimiento del sistema y estadísticas de hechizos.

- Documentación de la API (Swagger):
```http://127.0.0.1:8000/docs```
Documentación interactiva automática de todos los endpoints.

### Credenciales Admin
Contraseña: 1234

## Enlace al repositorio

```
https://github.com/MarcosAlonso05/ministry_magic_system
```
