from flask import Flask
from config import Config
from .forms import ContactForm

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
