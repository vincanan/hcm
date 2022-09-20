# 패키지
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

# mongodb 주소 바꿔야 함
client = MongoClient('mongodb+srv://gmo:gmo@gmo.fmwwa2z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbgmo

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def home():
    return render_template('main.html')

# 포스팅
@app.route('/api/reviewspost', methods=['POST'])
def posting():
    title_receive = request.form["title_give"]
    url_receive = request.form["url_give"]
    keywords_receive = request.form["keywords_give"]

    doc = {
        'title':title_receive,
        'url':url_receive,
        'keywords':keywords_receive
    }
    db.reviews.insert_one(doc)

    return jsonify({'msg':'등록 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)