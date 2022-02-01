from flask_restful import Resource, reqparse
from models.usuario import UserModel
          
class User(Resource):    
    def get(self, user_id):
        user = UserModel.find_hotel(user_id)
        if (user):
            return user.json()
        else:
            return {'message': 'User not found.'}, 404
     
    def delete(self, user_id):
        user = UserModel.find_hotel(hotel_user_idid)
        if user:
            try:
                user.remove_user()
            except:
                return {'message': 'An internal error ocurred trying to save user.'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404