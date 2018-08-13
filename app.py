#!/usr/bin/env python3

import json
import requests
from flask_wtf import FlaskForm
from wtforms import StringField
from flask import Flask, render_template, url_for
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_pyfile('bsbang.cfg')
app.config['SOLR_SELECT_URL'] = app.config['SOLR_URL'] + '/select'
app.config['SOLR_SPELL_URL'] = app.config['SOLR_URL'] + '/spell'


def get_items(data, startarg, rows=10):
    params = {'q': data, 'defType': 'edismax', 'start': startarg, 'rows': rows}
    r = requests.post(app.config['SOLR_SELECT_URL'], data=params)
    results = json.loads(r.text)
    return results


def get_spellcheck(data):
    params = {'q': data}
    r = requests.post(app.config['SOLR_SPELL_URL'], data=params)
    results = json.loads(r.text)
    return results


def revamped_response(old_response):
    new_docs = list()
    for doc in old_response["response"]["docs"]:
        new_doc = dict()
        for key, val in doc.items():
            new_doc[key.split(".")[-1]] = val
        new_docs.append(new_doc)
    return new_docs


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate():
        results = get_spellcheck(form.q.data)
        if(results["response"]["numFound"] != 0):
            results = get_items(form.q.data, startarg=0)
            results["response"]["docs"] = revamped_response(results)
            total_items = results["response"]["numFound"]
            return render_template('results.html', results=results, n_items=total_items, itemno=0)
        else:
            return render_template('index.html', results=results["spellcheck"]["suggestions"][-1], form=form)

    else:
        return render_template('index.html', form=form)


@app.route('/next_results&query=<query>&start=<start>', methods=['GET', 'POST'])
def next_results(query, start):
    no = int(start) + int(10)
    results = get_items(query, startarg=no)
    if(len(results["response"]["docs"]) == 0):
        no = int(start)
        results = get_items(query, startarg=no)
    results["response"]["docs"] = revamped_response(results)
    total_items = results["response"]["numFound"]
    return render_template('results.html', results=results, n_items=total_items, itemno=no)


@app.route('/prev_results&query=<query>&start=<start>', methods=['GET', 'POST'])
def prev_results(query, start):
    if(int(start) == 0):
        no = int(start)
        results = get_items(query, startarg=no)
    else:
        no = int(start) - int(10)
        results = get_items(query, startarg=no)
    results["response"]["docs"] = revamped_response(results)
    total_items = results["response"]["numFound"]
    return render_template('results.html', results=results, n_items=total_items, itemno=no)


@app.route('/about')
def about():
    params = {'q': 'AT_type:DataCatalog'}
    r = requests.post(app.config['SOLR_SELECT_URL'], data=params)
    results = json.loads(r.text)
    sites = set()
    for result in results['response']['docs']:
        sites.add(result)

    # FIXME: Yes I know, not a permanent solution. Biosamples does not have a DataCatalog
    # Probably the eaiest slightly better manual fix is to artificially create one in the Solr index until we have
    # a parallel database for non-solr info
    # justincc 2018-02-14 disable again, we ain't crawling biosamples atm
    # sites.add('https://www.ebi.ac.uk/biosamples')

    return render_template('about.html', sites=sites)


class SearchForm(FlaskForm):
    q = StringField('q', validators=[DataRequired()])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
