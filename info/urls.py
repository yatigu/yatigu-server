from flask import Blueprint
from .views import Stations, Tickets


app = Blueprint('info', __name__)

station_view = Stations.as_view('stations_view')
tickets_view = Tickets.as_view('tickets_view')
app.add_url_rule('/stations/', view_func=station_view)
app.add_url_rule('/tickets/', view_func=tickets_view)
