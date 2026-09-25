import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-placeholder')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Card(db.Model):
    """Database model for storing journal/portfolio entries."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Card {self.id}>'


class User(db.Model):
    """Database model for user authentication."""
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password: str) -> None:
        """Hashes raw password for secure database storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifies raw password against stored database hash."""
        return check_password_hash(self.password_hash, password)


# Auto-create SQLite database tables on initial run
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def login():
    """Handles user sign-in and credentials verification."""
    error = None
    if request.method == 'POST':
        login_input = request.form.get('email')
        password_input = request.form.get('password')

        user = User.query.filter_by(login=login_input).first()

        if user and user.check_password(password_input):
            return redirect(url_for('index'))
        else:
            error = 'Invalid email or password.'

    return render_template('login.html', error=error)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    """Handles new user registration and secure password hashing."""
    error = None
    if request.method == 'POST':
        login_input = request.form.get('email')
        password_input = request.form.get('password')

        existing_user = User.query.filter_by(login=login_input).first()
        if existing_user:
            error = 'Account with this email already exists.'
            return render_template('registration.html', error=error)

        new_user = User(login=login_input)
        new_user.set_password(password_input)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('registration.html', error=error)


@app.route('/index')
def index():
    """Displays user dashboard with all journal entries."""
    cards = Card.query.order_by(Card.id.desc()).all()
    return render_template('index.html', cards=cards)


@app.route('/card/<int:id>')
def card(id: int):
    """Displays detailed page for a specific journal entry."""
    card_item = Card.query.get_or_404(id)
    return render_template('card.html', card=card_item)


@app.route('/create', methods=['GET', 'POST'])
def create():
    """Renders creation form and handles new entry submission."""
    if request.method == 'POST':
        title = request.form.get('title')
        subtitle = request.form.get('subtitle')
        text = request.form.get('text')

        new_card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(new_card)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
