from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ

# Некоторые пользователи для примера
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

# Генерируем фиктивные данные для демонстрации
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Признаки (например, время)
y = np.array([2, 4, 5, 4, 5])  # Целевая переменная (например, количество продаж)

# Настройка Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user = User()
        user.id = user_id
        return user


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id in users and users[user_id]['password'] == password:
            user = User()
            user.id = user_id
            login_user(user)
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/analytics')
@login_required
def analytics():
    # Создаем и обучаем модель линейной регрессии
    model = LinearRegression()
    model.fit(X, y)

    # Получаем предсказания модели
    predictions = model.predict(X)

    # Передаем данные в шаблон и рендерим страницу аналитики
    return render_template('analytics.html', X=X, y=y, predictions=predictions)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        if user_id not in users:
            users[user_id] = {'password': password}
            return redirect(url_for('login'))
        else:
            return 'User already exists'
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
