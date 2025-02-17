🌱 MicroEstación Meteorológica ⛅

Descripción

Un sistema de monitoreo climático diseñado para caficultores y pequeñas fincas 🌿☕. Este proyecto permite visualizar el histórico de datos meteorológicos obtenidos de una micro estación, ayudando a la toma de decisiones en el cultivo.

🚀 Características

✅ Visualización de datos climáticos históricos 📊

✅ Despliegue local para cada finca 🏡

✅ Interfaz intuitiva y ligera 🎨

✅ Fácil de instalar y utilizar ⚡

🔧 Tecnologías

Backend: Django 🐍

Frontend: HTML, CSS, JavaScript 🌐

Base de datos: SQLite 📁

📌 Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

Clona el repositorio:

git clone https://github.com/Sant-Beco/SitioWebEstacionMeteorologica.git
cd SitioWebEstacionMeteorologica

Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows

Instala las dependencias:

pip install -r requirements.txt

Aplica migraciones y ejecuta el servidor:

python manage.py migrate
python manage.py runserver

Accede a la aplicación:

Abre tu navegador y ve a: http://127.0.0.1:8000

📁 Estructura del Proyecto

SitioWebEstacionMeteorologica/
│── estacion_climatica/
│   │── clima/                 # Aplicación principal
│   │── estacion_climatica/     # Configuración de Django
│   │── static/                 # Archivos estáticos (CSS, JS, imágenes)
│   │── templates/              # Plantillas HTML
│   │── db.sqlite3              # Base de datos SQLite
│   │── manage.py               # Script principal de Django
│   │── venv/                   # Entorno virtual (opcional)

🎨 Capturas de Pantalla

Agrega aquí imágenes o capturas de pantalla del sistema en funcionamiento.

📜 Licencia

Este proyecto está bajo la Licencia Apache 2.0. Consulta el archivo LICENSE para más información.

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

Haz un fork del repositorio

Crea una nueva rama (git checkout -b feature-nueva-funcionalidad)

Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad')

Sube tus cambios (git push origin feature-nueva-funcionalidad)

Abre un Pull Request

📧 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en escribirme a sanprogramador8@gmail.com.

🚜🌍 Hagamos la agricultura más inteligente juntos.
