from flask_restx import fields
from extensions import api

ns = api.namespace('riego', description='Operaciones de riego')

datos_model = api.model('Datos', {
    'temperatura': fields.Float(description='Temperatura en °C'),
    'humedad_ambiente': fields.Float(description='Humedad ambiente en %'),
    'humedad_suelo': fields.Integer(description='Humedad del suelo (valor ADC)'),
    'bomba_estado': fields.Boolean(description='Estado de la bomba'),
    'timestamp': fields.String(description='Fecha y hora')
})

historial_model = api.model('Historial', {
    'valor': fields.Float(description='Valor del sensor'),
    'timestamp': fields.String(description='Fecha')
})

bomba_model = api.model('Bomba', {
    'estado': fields.Boolean(required=True, description='Estado de la bomba')
})

valor_model = api.model('Valor', {
    'valor': fields.Float(description='Valor del sensor')
})