from flask import Flask, request, redirect, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(os.path.join(BASE_DIR, 'messages.txt'), 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {name} ({email}): {message}\n")

    return redirect('/thank-you.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
