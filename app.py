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

        # FIXME: To eliminate duplicates through crawling artifacts we are going to doctor the results to remove duplicate
        # URLs.  THIS IS NOT A PERMANENT SOLUTION, esp. as we are storing the url reported by the JSON-LD.  Really,
        # we need to store the URL we actually crawl and then make sure it matches the reported URL, etc.
        seen_urls = set()
        doctored_docs = []
        for doc in results['response']['docs']:
            if doc['url'] in seen_urls:
                continue

            seen_urls.add(doc['url'])
            doctored_docs.append(doc)

        results['response']['docs'] = doctored_docs
        results['response']['numFound'] = len(doctored_docs)
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

    # FIXME: Yes I know, not a permanent solution. Biosamples does not have a DataCatalog
    # Probably the eaiest slightly better manual fix is to artificially create one in the Solr index until we have
    # a parallel database for non-solr info
    sites.add('https://www.ebi.ac.uk/biosamples')

    return render_template('about.html', sites=sites)


class SearchForm(FlaskForm):
    q = StringField('q', validators=[DataRequired()])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
