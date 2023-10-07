from flask import Flask, render_template, request, jsonify
import t2
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send-location', methods=['POST'])
def receive_location():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']

    # 在這裡處理經緯度資訊，你可以儲存在資料庫中，或進行其他操作
    current_address = t2.get_current_location_address(latitude,longitude)
    if current_address:
        print(type(current_address))
        print(f'當前位置：{current_address}')
    else:
        print('無法獲取當前位置信息')
    return jsonify({'message': '位置資訊已接收'})



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=443,ssl_context=(r'C:\self_signed_certificate\server.crt',r'C:\self_signed_certificate\server.key'))