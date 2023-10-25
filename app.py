
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Bird

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://myname:ZSekcuQffPNf3nmkJCGSWPB7zRGLCFzp@dpg-cksivgprfc9c738fhhl0-a.oregon-postgres.render.com/bird_app_oca3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Birds(Resource):
    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

api.add_resource(Birds, "/birds")

class BirdByID(Resource):
    def get(self, id):
        bird = Bird.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(bird), 200)
    
api.add_resource(BirdByID, "/birds/<int:id>")    

if __name__ == "__main__":
    app.run


