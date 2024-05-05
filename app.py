from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from sklearn.linear_model import LinearRegression
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ
# Получаем абсолютный путь к корневой директории проекта
basedir = os.path.abspath(os.path.dirname(__file__))

# Настройки базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)


# Класс модели пользователя
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)


# Настройка Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Пользователь уже существует.', 'error')
            return redirect(url_for('registration'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация успешна', 'success')
        return redirect(url_for('login'))

    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Неверные данные для входа')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    username = current_user.username if current_user.is_authenticated else None
    return render_template('home.html', username=username)


@app.route('/analytics')
@login_required
def analytics():
    # Создаем и обучаем модель линейной регрессии
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Признаки (например, время)
    y = np.array([2, 4, 5, 4, 5])  # Целевая переменная (например, количество продаж)
    model = LinearRegression()
    model.fit(X, y)

    # Получаем предсказания модели
    predictions = model.predict(X)

    # Передаем данные в шаблон и рендерим страницу аналитики
    return render_template('analytics.html', X=X, y=y, predictions=predictions)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)