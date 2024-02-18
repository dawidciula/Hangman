from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

correctWord = ['W', 'I', 'S', 'I', 'E', 'L', 'E', 'C']

class usedLetters(db.Model):
    letter = db.Column(db.String(1), nullable = False, primary_key = True)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        letter = request.form['letter']
        for guessedLetter in correctWord:
           if guessedLetter == letter:
                pass
        else:
            return 'Błędna litera'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)