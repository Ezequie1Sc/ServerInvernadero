from flask_restx import Api
from flask_cors import CORS

api = Api(
    version='1.0',
    title='API Sistema de Riego',
    description='API para monitoreo y control de un sistema de riego'
)

cors = CORS()