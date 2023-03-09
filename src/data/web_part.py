from flask import Flask
from flask import render_template, request, redirect, abort, jsonify, make_response
import pandas as pd
from pathlib import Path
from forms.rating import RatingForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

PROJECT_DIR = str(Path(__file__).parent.parent.parent)


@app.route('/', methods=['GET', 'POST'])
def rating():
    domens = ['.com', '.site', '.рф', '.net', '.org', '.aero', '.biz', '.coop', '.info', '.ru']
    valid_domen = 0
    form = RatingForm()
    if form.validate_on_submit():
        site = form.site.data.lower()
        if 'http' in site:
            site = site[site.index('/') + 2:]
        if site.count('/') != 0:
            site = site[:site.index('/')]
        for i in domens:
            if i in site[-5:]:
                valid_domen = 1
        if valid_domen == 0:
            return render_template('register.html', form=form,
                                   message='Сайт введен в некоректном формате. Пожалуйста, введите корректный домен.',
                                   color=0)
        df = pd.read_csv(PROJECT_DIR + '/rating.csv', encoding='windows-1251')
        for i in df[:].values:
            data = i[0].split('&')
            if data[0] == site:
                if int(data[1][:-1]) >= 80:
                    color = 1
                elif int(data[1][:-1]) >= 30:
                    color = 2
                else:
                    color = 3
                return render_template('register.html', form=form,
                                       rating1='Рейтиг безопастности сайта ', rating2=data[0], rating3=data[1],
                                       color=color)
        return render_template('register.html', form=form,
                               message='К сожалению, этого сайта пока нет в нашей базе данных. Мы исправим это в самом ближайшем будущем!',
                               color=0)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
