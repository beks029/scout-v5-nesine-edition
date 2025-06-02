from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>🎉 Scout v5.0 Çalışıyor!</h1><p>Dashboard geliyor...</p>"

@app.route('/api/test')
def test():
    return jsonify({"message": "Scout v5.0 API çalışıyor!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
