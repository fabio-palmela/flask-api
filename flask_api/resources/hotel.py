from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id': 1,
        'nome': 'Alpha', 
        'diaria': 430.02,
        'cidade': 'São Paulo',
        'estrelas': 4
    }, 
    {
        'hotel_id': 2,
        'nome': 'Omega', 
        'diaria': 40.02,
        'cidade': 'Contagem',
        'estrelas': 1
    },
    {
        'hotel_id': 3,
        'nome': 'Beta', 
        'diaria': 1430.02,
        'cidade': 'São Bernardo',
        'estrelas': 5
    }
]

class Hoteis(Resource):
    def get(self):
        hoteis = HotelModel.find_hoteis()
        if (hoteis):
            return hoteis.json()
        else:
            return {'message': 'Hotel not found.'}, 404
        return hoteis[1]
          
class Hotel(Resource):
    #add_arguments aceita apenas argumentos necessários eliminando outros enviados na requisição
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome') 
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if (hotel):
            return hotel.json()
        else:
            return {'message': 'Hotel not found.'}, 404
     
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        
        novo_hotel = HotelModel(hotel_id, **dados)
        novo_hotel.save_hotel()
        return novo_hotel.json(), 201       
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()
     
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.remove_hotel()
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404