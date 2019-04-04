from flask_restful import Resource

class Home(Resource):

    def get():
        return render_template('index.html')
