from flask import Flask,render_template,jsonify
import pandas as pd


app = Flask(__name__)

df = pd.read_csv("dictionary.csv")
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<word>')
def search_word(word):

    definition = df.loc[df['word']==word]["definition"].squeeze()
    word_dict = {
        "definition" : definition,
        "word":word
    }
    return word_dict


if __name__ == "__main__":
    app.run(debug=True)