from flask import Blueprint
from .views import Station
app = Blueprint('info', __name__)

station_view = Station.as_view('info_view')
app.add_url_rule('/stations/', view_func=station_view)