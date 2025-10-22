from flask import request, redirect
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

notes = {
}

@app.route('/programmer-diary')
def programmer_diary():
    return render_template('notes.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
        title = request.form['title']
        text = request.form['text']
        notes[title] = text
        return redirect('programmer_diary')

if __name__ == '__main__':
    app.run(debug=True)