from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/times-table')
def times_table():
    data = []
    for i in range(1, 13):
        row = [{'value': i * j} for j in range(1, 13)]
        data.append(row)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)