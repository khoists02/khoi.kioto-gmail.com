from flask import Flask
from db import db
from flask_restful import Api
from resources.user import UserRegister
from resources.userprofile import UserProfileResouce

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'lekhoi07121993'

api = Api(app)

@app.before_first_request # when first request to sever the database will start create tables from that.
def create_tables():
    db.create_all()


# jwt = JWT(app, authenticate, identity)  # /auth

# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList, '/stores')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserProfileResouce, '/user-profile')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)