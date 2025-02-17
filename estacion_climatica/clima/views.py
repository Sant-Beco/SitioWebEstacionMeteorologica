import pandas as pd
import plotly.express as px
import plotly.io as pio
from django.shortcuts import render
from .models import DatosClimaticos
from django.http import JsonResponse

def graficos(request):
    year = request.GET.get("year")
    month = request.GET.get("month")

    # Obtener los años únicos de los datos
    años_únicos = DatosClimaticos.objects.dates('fecha', 'year').values_list('fecha__year', flat=True).distinct()

    # Validar que year y month sean números antes de filtrar
    filtros = {}
    if year and year.isdigit():
        year = int(year)
        if year > 0:  # Asegurarse de que el año sea válido
            filtros["fecha__year"] = year
    if month and month.isdigit():
        month = int(month)
        if 1 <= month <= 12:  # Asegurarse de que el mes sea válido
            filtros["fecha__month"] = month

    # Obtener los meses únicos para el año seleccionado
    meses_únicos = []
    if year:
        meses_únicos = DatosClimaticos.objects.filter(fecha__year=year).dates('fecha', 'month').values_list('fecha__month', flat=True).distinct()

    # Obtener los datos de la base de datos
    datos = DatosClimaticos.objects.filter(**filtros).values("fecha", "temperatura", "humedad", "luz", "presion")

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(list(datos))

    # Si no hay datos, mostrar un mensaje
    if df.empty:
        return render(request, "clima/graficos.html", {"mensaje": "No hay datos para este período."})

    # Convertir la columna de fecha a datetime (si no está en ese formato)
    try:
        df["fecha"] = pd.to_datetime(df["fecha"])
    except Exception as e:
        return render(request, "clima/graficos.html", {"mensaje": f"Error al procesar fechas: {e}"})

    # Agrupar por día y calcular promedios
    df["dia"] = df["fecha"].dt.date
    df_daily = df.groupby("dia").mean().reset_index().fillna(0)

    # Formatear los valores a 2 decimales
    df_daily["temperatura"] = df_daily["temperatura"].round(2)
    df_daily["humedad"] = df_daily["humedad"].round(2)
    df_daily["luz"] = df_daily["luz"].round(2)
    df_daily["presion"] = df_daily["presion"].round(2)

    # Crear gráficos con Plotly (con escalas de colores condicionales)

    # Gráfica de Temperatura
    fig_temp = px.scatter(
        df_daily, x="dia", y="temperatura", 
        title="Promedio Diario de Temperatura (°C)",
        labels={"dia": "Fecha", "temperatura": "Temperatura (°C)"},
        color="temperatura",  # Escala de colores basada en la temperatura
        color_continuous_scale=["#1E90FF", "#FF4500"],  # Azul para frío, rojo para calor
    )
    fig_temp.update_traces(marker=dict(size=10, line=dict(width=2, color="DarkSlateGrey")), mode="markers+lines")

    # Gráfica de Humedad
    fig_hum = px.scatter(
        df_daily, x="dia", y="humedad", 
        title="Promedio Diario de Humedad (%)",
        labels={"dia": "Fecha", "humedad": "Humedad (%)"},
        color="humedad",  # Escala de colores basada en la humedad
        color_continuous_scale=["#90EE90", "#006400"],  # Verde claro para baja humedad, verde oscuro para alta humedad
    )
    fig_hum.update_traces(marker=dict(size=10, line=dict(width=2, color="DarkSlateGrey")), mode="markers+lines")

    # Gráfica de Luz
    fig_luz = px.scatter(
        df_daily, x="dia", y="luz", 
        title="Promedio Diario de Luz",
        labels={"dia": "Fecha", "luz": "Luz"},
        color="luz",  # Escala de colores basada en la luz
        color_continuous_scale=["#FFD700", "#FF8C00"],  # Amarillo para poca luz, naranja para mucha luz
    )
    fig_luz.update_traces(marker=dict(size=10, line=dict(width=2, color="DarkSlateGrey")), mode="markers+lines")

    # Gráfica de Presión Atmosférica
    fig_presion = px.scatter(
        df_daily, x="dia", y="presion", 
        title="Promedio Diario de Presión Atmosférica",
        labels={"dia": "Fecha", "presion": "Presión"},
        color="presion",  # Escala de colores basada en la presión
        color_continuous_scale=["#9370DB", "#4B0082"],  # Morado claro para baja presión, morado oscuro para alta presión
    )
    fig_presion.update_traces(marker=dict(size=10, line=dict(width=2, color="DarkSlateGrey")), mode="markers+lines")

    # Convertir gráficos a HTML
    graficos_html = {
        "temperatura": pio.to_html(fig_temp, full_html=False),
        "humedad": pio.to_html(fig_hum, full_html=False),
        "luz": pio.to_html(fig_luz, full_html=False),
        "presion": pio.to_html(fig_presion, full_html=False),
    }

    return render(request, "clima/graficos.html", {
        **graficos_html,
        "year_selected": year,
        "month_selected": month,
        "años_únicos": años_únicos,  # Pasar los años únicos al template
        "meses_únicos": meses_únicos,  # Pasar los meses únicos al template
    })


def obtener_meses(request):
    year = request.GET.get("year")
    if year and year.isdigit():
        year = int(year)
        meses = DatosClimaticos.objects.filter(fecha__year=year).dates('fecha', 'month').values_list('fecha__month', flat=True).distinct()
        return JsonResponse({"meses": list(meses)})
    return JsonResponse({"meses": []})