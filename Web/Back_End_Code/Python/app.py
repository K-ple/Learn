from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data_from_client = request.json.get('data')
    # 여기서 Python 코드로 데이터 처리를 수행합니다.
    # 필요한 결과를 변수에 저장합니다.
    result = "Hello, " + data_from_client + "!"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
