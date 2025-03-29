from flask import Flask, render_template
from controller.database import db 
from controller.models import *

app = Flask(__name__, template_folder ='views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.quizmaster'
db.init_app(app)





from controller.routes import *

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
