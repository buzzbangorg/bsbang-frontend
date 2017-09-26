from flask import Flask, render_template
from wtforms import Form, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    return render_template('index.html', form=form)


class SearchForm(Form):
    q = StringField('q', validators=[DataRequired()])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
