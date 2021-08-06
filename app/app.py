from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # new
from flask_migrate import Migrate
from werkzeug.utils import import_string

app = Flask(__name__)
cfg = import_string("app.config.ProductionConfig")()
app.config.from_object(cfg)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# from view.views import get_bills_blueprint
from app.view.views import get_bills_blueprint

app.register_blueprint(get_bills_blueprint, url_prefix='/bills')

from app.view.views import create_bills_blueprint

app.register_blueprint(create_bills_blueprint, url_prefix='/create-bill')

from app.view.views import update_bill_blueprint

app.register_blueprint(update_bill_blueprint, url_prefix='/update-bill')

from app.view.views import delete_bill_blueprint

app.register_blueprint(delete_bill_blueprint, url_prefix='/delete-bill')

if __name__ == '__main__':
    app.run()
