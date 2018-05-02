import os
from flask import Flask
from {{cookiecutter.package_name}} import log_config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
log_config.set_logging(os.path.join(BASE_DIR, 'logs'))

app = Flask('{{cookiecutter.package_name}}')
app.config.from_object('{{cookiecutter.package_name}}.default_settings')

import dotenv

dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

import {{cookiecutter.package_name}}.views  # Must be loaded at last
