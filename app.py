from flask import Flask, render_template

app = Flask(__name__)


@app.route('/clothes/')
def index():
    context = {
        'title': 'Одежда'
    }
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {
        'title': 'Обувь'
    }
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {
        'title': 'Куртка'
    }
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
