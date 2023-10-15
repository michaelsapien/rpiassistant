from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class home(Resource):
    def get(self):
        return jsonify(
            {
                'Message': 'flaskserver is running',
                'description': 'check api documentation for details',
                'status': 200
            }
        )

api.add_resource(home, '/')

if __name__ == "__main__":
	app.run(debug=True)