from flask import Flask, request, redirect, send_from_directory
from datetime import datetime

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # 打印到控制台
    print(f"New message from {name} ({email}): {message}")

    # 生成时间戳
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 保存到文件（每条信息一行）
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {name} ({email}): {message}\n")

    return redirect('/thank-you.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
