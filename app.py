import io
import base64
# import
from PIL import Image
from flask import Flask
from flask import render_template, request, jsonify, send_file, send_from_directory

from models.get_image import getImage_

app = Flask(__name__)




@app.route("/")
def index():
    return "<h1 style='text-align:center;'>Nimbus</h1>"

@app.route("/api/v1/image")
def getImage():
    source = request.args.get('source', default = 'nasa', type = str)
    getImage_(source)
    # if source.lower() == 'esa':
    #     return send_file('data/esa_tsm.png', mimetype='image/gif')
    # elif source.lower() == 'jaxa':
    #
    # elif source.lower() == 'nasa':
    #     return 'NASA not ready yet'
    # else:
    #     return 'Specify a data source'
    # return send_file('data/jaxa_tsm.png', mimetype='image/gif')
    return 'test'

if __name__ == '__main__':
    app.run(debug=False)
