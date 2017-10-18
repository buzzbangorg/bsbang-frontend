#!/usr/bin/env python3

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import json
import requests

app = Flask(__name__)
app.config.from_pyfile('bsbang.cfg')
app.config['SOLR_SELECT_URL'] = app.config['SOLR_URL'] + '/select'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate():
        # flash('Query for [%s]' % form.q.data)
        params = {'q': form.q.data, 'defType': 'edismax'}
        r = requests.post(app.config['SOLR_SELECT_URL'], data=params)
        results = json.loads(r.text)
    else:
        results = None

    return render_template('index.html', form=form, results=results)


@app.route('/about')
def about():
    params = {'q': 'AT_type:DataCatalog'}
    r = requests.post(app.config['SOLR_SELECT_URL'], data=params)
    results = json.loads(r.text)
    sites = set()
    for result in results['response']['docs']:
        sites.add(result['url'])

    return render_template('about.html', sites=sites)


class SearchForm(FlaskForm):
    q = StringField('q', validators=[DataRequired()])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
