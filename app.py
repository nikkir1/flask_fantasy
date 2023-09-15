from flask import Flask, render_template, abort, redirect, url_for

app = Flask(__name__)

ids_with_images = {
    '111': '../static/111.png',
    '11': '../static/11.jpg',
    '12': '../static/12.jpg',
    '13': '../static/13.png',
    '15': '../static/15.png',
    '21': '../static/21.png',
    '22': '../static/22.png',
    '23': '../static/23.png',
    '42': '../static/42.png',
    '73': '../static/73.png',
    '85': '../static/85.png',
    '91': '../static/91.png',
    '72': '../static/72.png',
    '53': '../static/53.png',
}

hidden_id = '787'

@app.route('/')
def home():
    return render_template('home.html', ids_with_images=ids_with_images, hidden_id=hidden_id)

@app.route('/object/id=<string:id>')
def object(id):
    if id in ids_with_images or id == hidden_id:
        image_path = ids_with_images.get(id, '787.png')  # use 'hidden.png' for hidden_id
        return render_template('object.html', id=id, image_path=image_path)
    else:
        return redirect(url_for('home'))  # redirect to home page for non-existing id

if __name__ == '__main__':
    app.run(debug=True)
