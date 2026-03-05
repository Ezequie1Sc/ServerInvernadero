from collections import deque
from datetime import datetime, timedelta

ultimos_datos = None
historial_temperatura = deque(maxlen=168)
historial_humedad_ambiente = deque(maxlen=168)
historial_humedad_suelo = deque(maxlen=168)


def guardar_datos(datos):
    global ultimos_datos
    datos['timestamp'] = datetime.now().isoformat()
    ultimos_datos = datos

    historial_temperatura.append({
        'valor': datos['temperatura'],
        'timestamp': datos['timestamp']
    })

    historial_humedad_ambiente.append({
        'valor': datos['humedad_ambiente'],
        'timestamp': datos['timestamp']
    })

    historial_humedad_suelo.append({
        'valor': datos['humedad_suelo'],
        'timestamp': datos['timestamp']
    })

    return datos


def obtener_ultimos_datos():
    return ultimos_datos


def obtener_valor(campo):
    if ultimos_datos and campo in ultimos_datos:
        return {'valor': ultimos_datos[campo]}
    return None


def actualizar_bomba(estado):
    global ultimos_datos
    if ultimos_datos:
        ultimos_datos['bomba_estado'] = estado
    return {'estado': estado}


def obtener_bomba():
    if ultimos_datos and 'bomba_estado' in ultimos_datos:
        return {'estado': ultimos_datos['bomba_estado']}
    return {'estado': False}


def calcular_historial(historial, redondeo=1):
    seven_days_ago = datetime.now() - timedelta(days=7)

    filtrado = [
        entry for entry in historial
        if datetime.fromisoformat(entry['timestamp']) >= seven_days_ago
    ]

    daily_data = {}
    for entry in filtrado:
        date = datetime.fromisoformat(entry['timestamp']).strftime('%Y-%m-%d')
        daily_data.setdefault(date, []).append(entry['valor'])

    resultado = []
    for date, values in sorted(daily_data.items()):
        avg = sum(values) / len(values)
        resultado.append({
            'valor': round(avg, redondeo),
            'timestamp': date
        })

    return resultado


def historial_temperatura_service():
    return calcular_historial(historial_temperatura)


def historial_humedad_ambiente_service():
    return calcular_historial(historial_humedad_ambiente)


def historial_humedad_suelo_service():
    return calcular_historial(historial_humedad_suelo, redondeo=0)