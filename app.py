from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['SOLR_SELECT_URL'] = app.config['SOLR_URL'] + '/select'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate():
        # flash('Query for [%s]' % form.q.data)
        params = {'q': form.q.data, 'defType': 'edismax'}
        r = requests.post(app.config['SOLR_SELECT_URL'], data=params)
        flash('Results [%s]' % r.text)

    return render_template('index.html', form=form)


class SearchForm(FlaskForm):
    q = StringField('q', validators=[DataRequired()])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
