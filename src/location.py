from raw import nws_rest_api

class Location:
  def __init__(self, latitude=None, longitude=None, wfo=None, grid_x=None, grid_y=None):
    # lat/long
    if latitude is not None or longitude is not None:
      if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        raise AttributeError('Latitude and longitude must be numbers')
    self.latitude = latitude
    self.longitude = longitude

    # gridpoint
    if wfo is not None or grid_x is not None or grid_y is not None:
      if not isinstance(wfo, str) or wfo == '':
        raise AttributeError('wfo must be a string')
      if not isinstance(grid_x, int) or not isinstance(grid_y, int):
        raise AttributeError('grid_x and grid_y must be integers')
    self.wfo = wfo
    self.grid_x = grid_x
    self.grid_y = grid_y

    # derived
    self.zone_id = None
    self.station_id = None

    if not self.has_latlong() and not self.has_gridpoint():
      raise AttributeError('Must provide either latitude/longitude or wfo/grid_x/grid_y')

  def has_latlong(self):
    return self.latitude is not None and self.longitude is not None

  def has_gridpoint(self):
    return self.wfo is not None and self.grid_x is not None and self.grid_y is not None

  def get_latlong(self):
    if not self.has_latlong():
      if not self.has_gridpoint():
        raise Exception('Unexpected logic error')
      self.call_gridpoint_to_latlong()
    return self.latitude, self.longitude

  def get_gridpoint(self):
    if not self.has_gridpoint():
      if not self.has_latlong():
        raise Exception('Unexpected logic error')
      self.call_point()
    return self.wfo, self.grid_x, self.grid_y

  def get_zone_id(self):
    if self.zone_id is None:
      self.call_zone()
    return self.zone_id

  def get_station_id(self):
    if self.station_id is None:
      self.call_gridpoint_stations()
    return self.station_id

  def get_office_id(self):
    wfo, _1, _2 = self.get_gridpoint()
    return wfo

  def call_point(self):
    latitude, longitude = self.get_latlong()
    point_obj = nws_rest_api.point(f'{latitude},{longitude}')
    self.wfo = point_obj.properties['gridId']
    self.grid_x = point_obj.properties['gridX']
    self.grid_y = point_obj.properties['gridY']

  def call_gridpoint_to_latlong(self):
    # smallish return data with gridpoint geometry
    forecast = nws_rest_api.gridpoint_forecast(*self.get_gridpoint())
    coords = forecast.geometry['coordinates'][0]
    self.latitude = sum([coord[1] for coord in coords]) / len(coords)
    self.longitude = sum([coord[0] for coord in coords]) / len(coords)

  def call_gridpoint_stations(self):
    stations = nws_rest_api.gridpoint_stations(*self.get_gridpoint())
    closest_dist = float('inf')
    closest_station = None
    latitude, longitude = self.get_latlong()
    for station in stations.features:
      # cartesion distance should be good enough, no need for geodesics
      station_latitude = station.geometry['coordinates'][1]
      station_longitude = station.geometry['coordinates'][0]

      dist = ((latitude - station_latitude)**2 + (longitude - station_longitude)**2)**.5
      if dist < closest_dist:
        closest_dist = dist
        closest_station = station

    self.station_id = closest_station.properties['stationIdentifier']

  def call_zone(self):
    latitude, longitude = self.get_latlong()
    # note, include_geometry not currently working
    zone_list = nws_rest_api.zone_list_type(
        type='forecast', point=f'{latitude},{longitude}', include_geometry='false').features
    if len(zone_list) == 0:
      raise Exception(f'Did not find any zones that cover {latitude},{longitude}')
    if len(zone_list) == 1:
      self.zone_id = zone_list[0].properties['id']
      return
    station_id = self.get_station_id()
    for zone in zone_list:
      for station_url in zone.properties['observationStations']:
        if station_url.endswith(f'/{station_id}'):
          self.zone_id = zone.properties['id']
          return
    # can't pick, so just go with the first one
    self.zone_id = zones[0].properties['id']


    


def location_by_latlong(latitude, longitude):
  return Location(latitude=latitude, longitude=longitude)


def location_by_gridpoint(wfo, grid_x, grid_y):
  return Location(wfo=wfo, grid_x=grid_x, grid_y=grid_y)
