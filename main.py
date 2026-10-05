from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Lista de idiomas soportados
IDIOMAS = ['es', 'en', 'ru']


# 1. Ruta raíz
@app.route('/')
def route():
    return redirect(url_for('home', lang='es'))


# 2. Rutas dinámicas por idioma
@app.route('/<lang>/')
def home(lang):
    if lang not in IDIOMAS: return redirect(url_for('home', lang='es'))
    return render_template(f'{lang}/index.html', lang=lang)


@app.route('/<lang>/implantes')
def implantes(lang):
    if lang not in IDIOMAS: return redirect(url_for('implantes', lang='es'))
    return render_template(f'{lang}/implantes.html', lang=lang)


@app.route('/<lang>/ortodoncia')
def ortodoncia(lang):
    if lang not in IDIOMAS: return redirect(url_for('ortodoncia', lang='es'))
    return render_template(f'{lang}/ortodoncia.html', lang=lang)


@app.route('/<lang>/periodoncia')
def periodoncia(lang):
    if lang not in IDIOMAS: return redirect(url_for('periodoncia', lang='es'))
    return render_template(f'{lang}/periodoncia.html', lang=lang)


@app.route('/<lang>/equipo')
def equipo(lang):
    if lang not in IDIOMAS: return redirect(url_for('equipo', lang='es'))
    return render_template(f'{lang}/equipo.html', lang=lang)


@app.route('/<lang>/contacto')
def contacto(lang):
    if lang not in IDIOMAS: return redirect(url_for('contacto', lang='es'))
    return render_template(f'{lang}/contacto.html', lang=lang)



if __name__ == '__main__':
    app.run(debug=False)
