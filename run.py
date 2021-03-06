import os
from flask import Flask
from whitenoise import WhiteNoise

app = Flask(__name__)
wnapp = WhiteNoise(app, root='./public/', index_file=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)