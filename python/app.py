from flask import Flask
from flask import request, jsonify
from datetime import datetime

from models.get_image import getImage

app = Flask(__name__)


# api/image?date=YYYY-MM-DD?city=venice
@app.route('/api/image')
def image():
    date = request.args.get('date')
    city = request.args.get('city').lower()

    datetime_object = datetime.strptime(date, '%Y-%m-%d')
    getImage(city, datetime_object)
    return jsonify({'success' : True})


if __name__ == '__main__':
    app.run(debug=False)
