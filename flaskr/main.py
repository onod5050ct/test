from flaskr import app
from flask import render_template
from flask import Response
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
id_list = {
    "user001": "1234",
    "USER002": "4567"
}

@auth.get_password
def get_pw(id):
    return id_list.get(id)

@app.route('/')
@auth.login_required
def index():
    book = [
        {'title': 'はらぺこあおむし',
        'price': 1200,
        'arrival_day': '2020/7/12'},
        {'title': 'ぐりとぐら',
        'price': 990,
        'arrival_day': '2020/7/13'},
    ]
    return book, 404
    # return render_template(
    #    'index.html',
    #    book=book
    # )