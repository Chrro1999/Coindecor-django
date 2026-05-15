# Coindecor - Frontend (React + Vite)

Este es el catálogo interactivo de **Coindecor**. Una aplicación moderna, elegante y rápida construida con **React** para visualizar productos de decoración y hogar con un sistema de reservas vía WhatsApp.

---

## ✨ Características Principales

* **Visualización Premium:** Interfaz limpia con tipografía refinada y diseño minimalista.
* **Carrusel Dinámico:** Galería de imágenes integrada en modales para cada producto.
* **Zoom de Alta Precisión:** Sistema de lupa personalizado para ver detalles de los productos.
* **Adaptabilidad:** Diseño 100% responsivo para móviles, tablets y escritorio.
* **Integración con Backend:** Consumo de datos en tiempo real desde una API Django.

---

## 🛠️ Tecnologías Utilizadas

* **React 19:** Biblioteca principal para la interfaz de usuario.
* **Vite:** Herramienta de construcción y servidor de desarrollo ultra rápido.
* **Tailwind CSS:** Framework de estilos para un diseño moderno y ágil.
* **Lucide React / Heroicons:** Para la iconografía del sitio.

---

## ⚙️ Configuración Local

Sigue estos pasos para poner en marcha el proyecto en tu máquina local:

### 1. Instalación de dependencias
Entra a la carpeta del proyecto y ejecuta:
```bash
npm install

2. Configuración de API (CORS)
    Asegúrate de que tu servidor backend (Django) esté corriendo en http://127.0.0.1:8000.

    Nota: El archivo ModalProducto.jsx está configurado para transformar las URLs relativas del backend en URLs absolutas automáticamente.

3. Iniciar el servidor de desarrollo
    npm run dev
    La aplicación estará disponible en: http://localhost:5173/

Estructura del Proyecto
    /src/components/: Contiene los componentes reutilizables como el ModalProducto.jsx.

    /src/assets/: Imágenes locales, logos y recursos estáticos.

    /src/App.jsx: Punto de entrada principal donde se gestiona el estado de los productos.

    tailwind.config.js: Configuración personalizada de fuentes y colores para la marca.