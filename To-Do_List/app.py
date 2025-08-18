from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') # Procura automaticamente por uma pasta 'templates'

@app.route('/users/<username>')
def users(username):
    return render_template('users.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)