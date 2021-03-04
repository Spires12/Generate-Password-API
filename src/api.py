from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get():
    return jsonify(message="API Generator Password")


if __name__ == '__main__':
  app.run(debug=True)
