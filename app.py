from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')  # 定義 /aboutme 路由
def aboutme():
    return render_template('aboutme.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/ucan')
def ucan():
    return render_template('ucan.html')

if __name__ == '__main__':
    app.run(debug=True)

