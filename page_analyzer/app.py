import os

import requests
from dotenv import load_dotenv
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from .data_base import UrlRepository
from .normalize_url import normalize_url, validate_url
from .parser import get_data

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DATABASE_URL'] = DATABASE_URL


repo = UrlRepository(DATABASE_URL)


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/urls')
def urls_create():
    url = request.form.get('url', '').strip()
    errors = validate_url(url)
    if errors:
        flash(errors, 'danger')
        return render_template('index.html', url=url), 422
    
    url = normalize_url(url)
    found_url = repo.get_url_by_name(url)

    if found_url:
        flash('Страница уже существует', 'info')
        return redirect(url_for('url', id=found_url.id))
    else:
        id = repo.add_url(url)
        flash('Страница успешно добавлена', 'success')
        return redirect(url_for('url', id=id.id))
    

@app.get('/urls')
def urls():
    urls = repo.get_all_urls()
    return render_template('urls.html', urls=urls)


@app.get('/urls/<int:id>')
def url(id):
    url = repo.get_url_by_id(id)
    if not url:
        return abort(404)
    
    url_checks = repo.get_url_checks_by_id(id)
    return render_template(
        'url.html',
        url=url,
        url_checks=url_checks
    )


@app.post('/urls/<int:id>/checks')
def url_checks(id):
    url = repo.get_url_by_id(id)
    
    try:
        response = requests.get(url.name, timeout=3)
        response.raise_for_status()
        
        data = get_data(response.text) 
        data['url_id'] = id
        data['status_code'] = response.status_code

        repo.add_url_checks(data)
        flash('Страница успешно проверена', 'success')
    
    except Exception:
        flash('Произошла ошибка при проверке', 'danger')
    
    finally:

        return redirect(url_for('url', id=id))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()