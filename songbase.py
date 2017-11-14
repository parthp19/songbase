from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dashfjkdfasasldjfklasjfuoeasm'

@app.route('/')
def home():
    # return '<h1>hello world!!!!</h1>'
    return render_template('index.html')


@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    if request.method == 'GET':
        first_name = request.args.get('first_name')  # this is for GET
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            return render_template('form-demo.html', first_name=session.get('first_name'))

    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        return redirect(url_for('form_demo'))

@app.route('/songs')
def get_all_songs():
    songs = [
        'song 1',
        'song 2',
        'song 3'
    ]
    return render_template('songs.html', songs=songs)

@app.route('/user/<string:name>')
def get_user(name):
    # return '<h1>Hello %s your age is %d</h1>' % (name,3)
    return render_template('user.html',user_name=name)

if __name__ =='__main__':
    app.run()
