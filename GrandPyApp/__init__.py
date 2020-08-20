from flask import Flask

from .views import app
from . import models

# connect SQLAchemy to app
models.db.init_app(app)