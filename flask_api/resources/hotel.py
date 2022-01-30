from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

    def get_hoteis_por_cidade(self):
        dados = Hotel.argumentos.parse_args()
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.filter_by(cidade=dados['Sabará']).all()]}
          
class Hotel(Resource):
    #add_arguments aceita apenas argumentos necessários eliminando outros enviados na requisição
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.") 
    argumentos.add_argument('estrelas', type=float, help="The field 'estrelas' must be of type float")
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
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return novo_hotel.json(), 201       
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel.json()
     
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.remove_hotel()
            except:
                return {'message': 'An internal error ocurred trying to save hotel.'}, 500
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404