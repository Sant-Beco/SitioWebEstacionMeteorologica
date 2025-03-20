@echo off
cd /d C:\Users\Usuario\Documents\Arduino\estacionClimaticaIoTProjectActual\GraficosDelHistoricoSitioWeb\estacion_climatica
set PYTHONPATH=%CD%
C:\Users\Usuario\Documents\Arduino\estacionClimaticaIoTProjectActual\GraficosDelHistoricoSitioWeb\venv\Scripts\python.exe -m waitress --listen=127.0.0.1:8000 estacion_climatica.wsgi:application

