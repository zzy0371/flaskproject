from flask import Flask
import os
from views.user import userbp
from views.main import mainbp

app = Flask(__name__)
app.register_blueprint(mainbp)
app.register_blueprint(userbp)

app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(debug=True)