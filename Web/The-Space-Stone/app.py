from flask import Flask, request, render_template, jsonify,redirect,url_for
import pickle
import base64
import random

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
users = ["John", "Scavenger", "Nigru"]
dct = {"Hela": "Holy SHit", "Tobi": "Ask Tony to bring back Rin for me","Dr. Nic West:":"The best surgeon and the best superhero. But you still didn't get the girl.","Thanos":"Wassup bois"}

# Load the pickled data
with open('marvel_data.pkl', 'rb') as file:
    marvel_data = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/space')
def space():
    return render_template('space.html',comments=dct)

@app.route('/get_characters', methods=['POST'])
def get_characters():
    char_name = request.form['char_name']
    characters = marvel_data.get(char_name, [])
    return jsonify(characters)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.json["comment"]

    try:
        comment_bytes = base64.b64decode(comment)
        new_comment = pickle.loads(comment_bytes)

        # Randomly select a user to associate the new comment with
        # dct = {}
        random_user = random.choice(users)
        dct[random_user] = str(new_comment)
        return jsonify({'success': True, 'comments': {random_user:new_comment}})
    
    except Exception as e:
        # dct = {}
        new_comment = str(e)
        random_user = random.choice(users)
        dct[random_user] = new_comment

        return jsonify({'success': True, 'comments': {random_user:new_comment}})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=False)
