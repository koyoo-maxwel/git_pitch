from flask import Flask


# initializing our application
app = Flask(__name__)
from app import views