from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "system": "LifeSigns Healthcare API",
        "status": "secure",
        "version": "1.0",
        "hipaa_compliant": True
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/patients')
def patients():
    return jsonify({
        "message": "Patient data endpoint",
        "data": []
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)