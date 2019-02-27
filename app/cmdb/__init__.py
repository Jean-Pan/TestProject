from flask import Blueprint

blueprint = Blueprint(
    'asset',
    __name__,
    url_prefix='/asset'
)
