from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_pyfile('config.cfg')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate():
        flash('Query for [%s]' % form.q.data)
        return redirect('/')

    return render_template('index.html', form=form)


class SearchForm(FlaskForm):
    q = StringField('q', validators=[DataRequired()])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
