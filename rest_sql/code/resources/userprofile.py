from flask_restful import Resource, reqparse
from models.user_profile import UserProfile
from models.user import UserModel
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class UserProfileResouce(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('address',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('phone',
                        type=str,
                        help="This field cannot be blank."
                        )
    parser.add_argument('avatar',
                        type=str,
                        help="This field cannot be blank."
                        )
    parser.add_argument('user_id',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserProfileResouce.parser.parse_args()
        if (UserModel.find_by_id(data['user_id'])) is None:
            return {'message': 'User cannot created !'}, 401
        userProfile = UserProfile(
            data['address'], data['phone'], data['avatar'], data['user_id'])
        if (userProfile.check_exists_user_id(data['user_id'])):
          return {'message': 'Cannot create new user profile'}, 400
        try:
          userProfile.save_to_database()
        except Exception as e:
          return {"message": "An error occurred inserting the item.", "error": MyEncoder().encode(e)}, 500

        return {"message": "User pofile created successfully.", "data": userProfile.json()}, 201
