from typing_extensions import Required
from flask_restful import Resource, reqparse

serializador =reqparse.RequestParser(bundle_errors=True)
serializador.add_argument(
    'actividadNombre',
    required=True,
    location='json',
    message='Falta la actividadNombre',
    type=str
)
class ActividadesController(Resource):
    def get(self):
        return {
            "message": None,
            "content":[{
                "actividadId": 1,
                "actividadNombre":"Ir a la playa",
            },
            {
                "actividadId": 2,
                "actividadNombre":"Cocinar",
            },
            {
                "actividadId": 3,
                "actividadNombre":"Ir al cumpleaños de mi abuela",
            }]
        }, 201

    def post(self):
        # logica para registrar la actividad en la bd
        return {
            "message": "actividad creada exitosamente",
            "content": ""
        }