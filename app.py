from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        if 'weight' in request.form and 'height' in request.form \
                and 'hip_girth' in request.form and 'sex' in request.form:
            return render_template('resp.html',
                                   imt=(int(request.form['weight']) /
                                       (int(request.form['height'])/100) ** 2),
                                   hip_girth_to_height=int(request.form['hip_girth']) /
                                                       int(request.form['height']) * 100,
                                   sex=request.form['sex'])
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
