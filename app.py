from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'GET':
        if ['weight', 'height', 'waist', 'sex'] in request.form:
            return render_template('resp.html')


if __name__ == '__main__':
    app.run(debug=True)

