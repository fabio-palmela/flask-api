from flask_restful import Resource, reqparse

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

class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }


class Hoteis(Resource):
     def get(self):
         return hoteis
          
class Hotel(Resource):
    #add_arguments aceita apenas argumentos necessários eliminando outros enviados na requisição
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome') 
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def find_hotel(hotel_id):
        todos_hoteis = Hoteis.get(Hoteis);
        hotel_id = int(hotel_id)
        for hotel in todos_hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel;
        return None;
    
    def gera_novo_hotel():
        novo_id = max(item['hotel_id'] for item in hoteis)
        dados = Hotel.argumentos.parse_args()
        objHotel = HotelModel(novo_id + 1, **dados)
        hoteis.append(objHotel.json())
        
    def update_hotel(hotel, hotel_id):
        dados = Hotel.argumentos.parse_args()
        objHotel = HotelModel(hotel_id, **dados)
        hotel.update(objHotel.json())
    
    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if (hotel):
            return hotel
        else:
            return {'message': 'Hotel not found.'}, 404
     
    def put(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if (hotel):
            Hotel.update_hotel(hotel, hotel_id)
            return Hotel.get(Hotel, hotel_id), 200
        else:
            Hotel.gera_novo_hotel()
            return Hotel.get(Hotel, hotel_id), 201            
    
    def post(self, hotel_id):
        #add_arguments aceita apenas argumentos necessários eliminando outros enviados na requisição
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome') 
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        
        dados = argumentos.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }
        
        hoteis.append(novo_hotel)
        return novo_hotel, 200
     
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if int(hotel['hotel_id']) != int(hotel_id)]
        return {'message': 'Hotel deleted.'}