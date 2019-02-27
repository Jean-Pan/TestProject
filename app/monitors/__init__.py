from flask import Blueprint

blueprint = Blueprint(
    'monitor_blueprint',
    __name__,
    url_prefix='/monitors',
)
