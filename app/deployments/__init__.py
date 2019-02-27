from flask import Blueprint

blueprint = Blueprint(
    'deployment_blueprint',
    __name__,
    url_prefix='/deployment',
)
