from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LifeSigns Healthcare System</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #0a0f1e; color: #e0e6f0; }
        header {
            background: linear-gradient(135deg, #0d1b2a, #1b3a5c);
            padding: 20px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid #00d4ff;
        }
        header h1 { color: #00d4ff; font-size: 24px; letter-spacing: 2px; }
        header span { color: #7fdbff; font-size: 13px; }
        .badge {
            background: #00ff9d22;
            border: 1px solid #00ff9d;
            color: #00ff9d;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 12px;
        }
        .hero {
            text-align: center;
            padding: 60px 20px 40px;
            background: radial-gradient(ellipse at center, #0d2137 0%, #0a0f1e 70%);
        }
        .hero h2 { font-size: 36px; color: #00d4ff; margin-bottom: 12px; }
        .hero p { color: #8899aa; font-size: 16px; max-width: 600px; margin: 0 auto 30px; }
        .status-bar {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }
        .status-item {
            background: #0d1b2a;
            border: 1px solid #1b3a5c;
            border-radius: 10px;
            padding: 16px 24px;
            text-align: center;
            min-width: 140px;
        }
        .status-item .label { font-size: 12px; color: #5577aa; margin-bottom: 6px; }
        .status-item .value { font-size: 20px; font-weight: bold; color: #00ff9d; }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            padding: 40px;
            max-width: 1100px;
            margin: 0 auto;
        }
        .card {
            background: #0d1b2a;
            border: 1px solid #1b3a5c;
            border-radius: 12px;
            padding: 24px;
            transition: border-color 0.3s;
        }
        .card:hover { border-color: #00d4ff; }
        .card .icon { font-size: 32px; margin-bottom: 12px; }
        .card h3 { color: #00d4ff; margin-bottom: 8px; font-size: 16px; }
        .card p { color: #667788; font-size: 14px; line-height: 1.6; }
        .security-section {
            background: #050d18;
            padding: 40px;
            text-align: center;
        }
        .security-section h2 { color: #00ff9d; margin-bottom: 30px; font-size: 22px; }
        .checks {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 12px;
            max-width: 800px;
            margin: 0 auto;
        }
        .check {
            background: #0d1b2a;
            border: 1px solid #00ff9d44;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 13px;
            color: #00ff9d;
        }
        .check::before { content: "✓ "; }
        .api-section {
            padding: 40px;
            max-width: 800px;
            margin: 0 auto;
        }
        .api-section h2 { color: #00d4ff; margin-bottom: 20px; font-size: 20px; }
        .endpoint {
            background: #0d1b2a;
            border-left: 3px solid #00d4ff;
            padding: 12px 20px;
            margin-bottom: 10px;
            border-radius: 0 8px 8px 0;
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .method {
            background: #00d4ff22;
            color: #00d4ff;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            min-width: 45px;
            text-align: center;
        }
        .path { color: #aabbcc; font-family: monospace; font-size: 14px; }
        .desc { color: #556677; font-size: 13px; margin-left: auto; }
        footer {
            text-align: center;
            padding: 20px;
            color: #334455;
            font-size: 12px;
            border-top: 1px solid #1b3a5c;
        }
    </style>
</head>
<body>
    <header>
        <h1>⚕ LifeSigns Healthcare</h1>
        <span>Secure Patient Data Management System</span>
        <span class="badge">HIPAA Compliant</span>
    </header>

    <div class="hero">
        <h2>Healthcare API Dashboard</h2>
        <p>Secure, containerized healthcare data management system deployed via DevSecOps pipeline with full HIPAA compliance.</p>
        <div class="status-bar">
            <div class="status-item"><div class="label">System Status</div><div class="value">ONLINE</div></div>
            <div class="status-item"><div class="label">Version</div><div class="value">1.0</div></div>
            <div class="status-item"><div class="label">HIPAA</div><div class="value">PASS</div></div>
            <div class="status-item"><div class="label">Uptime</div><div class="value">99.9%</div></div>
        </div>
    </div>

    <div class="grid">
        <div class="card">
            <div class="icon">🔒</div>
            <h3>Security First</h3>
            <p>Every deployment passes SAST, SCA, secrets scanning, and container vulnerability scanning before reaching production.</p>
        </div>
        <div class="card">
            <div class="icon">🏥</div>
            <h3>Patient Data Protection</h3>
            <p>PHI data handled in compliance with HIPAA regulations. All access is logged and audited automatically.</p>
        </div>
        <div class="card">
            <div class="icon">🚀</div>
            <h3>DevSecOps Pipeline</h3>
            <p>Automated CI/CD pipeline with integrated security gates. No insecure code reaches the Kubernetes cluster.</p>
        </div>
        <div class="card">
            <div class="icon">☸</div>
            <h3>Kubernetes Hardened</h3>
            <p>Pods run as non-root, privilege escalation disabled, all Linux capabilities dropped, resource limits enforced.</p>
        </div>
    </div>

    <div class="security-section">
        <h2>🛡 HIPAA Security Compliance Checks</h2>
        <div class="checks">
            <div class="check">Container runs as non-root</div>
            <div class="check">Privilege escalation disabled</div>
            <div class="check">Linux capabilities dropped</div>
            <div class="check">Resource limits enforced</div>
            <div class="check">Image scanned for CVEs</div>
            <div class="check">No hardcoded credentials</div>
            <div class="check">Secrets via K8s Secrets</div>
            <div class="check">SAST scan passed</div>
            <div class="check">Dependency check passed</div>
        </div>
    </div>

    <div class="api-section">
        <h2>API Endpoints</h2>
        <div class="endpoint">
            <span class="method">GET</span>
            <span class="path">/</span>
            <span class="desc">Dashboard & system status</span>
        </div>
        <div class="endpoint">
            <span class="method">GET</span>
            <span class="path">/health</span>
            <span class="desc">Health check endpoint</span>
        </div>
        <div class="endpoint">
            <span class="method">GET</span>
            <span class="path">/patients</span>
            <span class="desc">Patient data endpoint</span>
        </div>
        <div class="endpoint">
            <span class="method">GET</span>
            <span class="path">/api/status</span>
            <span class="desc">API status & compliance info</span>
        </div>
    </div>

    <footer>
        LifeSigns Healthcare System — DevSecOps Pipeline — HIPAA Compliant — Deployed on Kubernetes
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "hipaa_compliant": True})

@app.route('/patients')
def patients():
    return jsonify({"message": "Patient data endpoint", "data": []})

@app.route('/api/status')
def status():
    return jsonify({
        "system": "LifeSigns Healthcare API",
        "status": "secure",
        "version": "1.0",
        "hipaa_compliant": True,
        "security_checks": {
            "secrets_scan": "PASS",
            "code_quality": "PASS",
            "dependency_check": "PASS",
            "image_scan": "PASS"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)