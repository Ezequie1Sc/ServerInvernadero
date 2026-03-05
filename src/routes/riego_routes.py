from flask_restx import Resource
from models.riego_models import ns, datos_model, historial_model, bomba_model, valor_model
from services import riego_service as service


@ns.route('/datos')
class Datos(Resource):

    @ns.expect(datos_model)
    @ns.marshal_with(datos_model)
    def post(self):
        datos = service.guardar_datos(ns.payload)
        return datos, 201

    @ns.marshal_with(datos_model)
    def get(self):
        datos = service.obtener_ultimos_datos()
        if not datos:
            ns.abort(404, "No hay datos disponibles")
        return datos


@ns.route('/temperatura')
class Temperatura(Resource):

    @ns.marshal_with(valor_model)
    def get(self):
        valor = service.obtener_valor('temperatura')
        if not valor:
            ns.abort(404, "No hay datos disponibles")
        return valor


@ns.route('/humedad_ambiente')
class HumedadAmbiente(Resource):

    @ns.marshal_with(valor_model)
    def get(self):
        valor = service.obtener_valor('humedad_ambiente')
        if not valor:
            ns.abort(404, "No hay datos disponibles")
        return valor


@ns.route('/humedad_suelo')
class HumedadSuelo(Resource):

    @ns.marshal_with(valor_model)
    def get(self):
        valor = service.obtener_valor('humedad_suelo')
        if not valor:
            ns.abort(404, "No hay datos disponibles")
        return valor


@ns.route('/bomba')
class Bomba(Resource):

    @ns.expect(bomba_model)
    @ns.marshal_with(bomba_model)
    def post(self):
        estado = ns.payload['estado']
        return service.actualizar_bomba(estado)

    @ns.marshal_with(bomba_model)
    def get(self):
        return service.obtener_bomba()


@ns.route('/historial/temperatura')
class HistTemp(Resource):

    @ns.marshal_list_with(historial_model)
    def get(self):
        return service.historial_temperatura_service()


@ns.route('/historial/humedad_ambiente')
class HistHumAmb(Resource):

    @ns.marshal_list_with(historial_model)
    def get(self):
        return service.historial_humedad_ambiente_service()


@ns.route('/historial/humedad_suelo')
class HistHumSuelo(Resource):

    @ns.marshal_list_with(historial_model)
    def get(self):
        return service.historial_humedad_suelo_service()