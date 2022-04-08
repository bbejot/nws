#!/usr/bin/env python3

from raw import nws_rest_api
from location import Location, location_by_gridpoint, location_by_latlong


def get_alerts(location: Location):
  latitude, longitude = location.get_latlong()
  alerts = nws_rest_api.alerts_active(status=['actual'], point=f'{latitude},{longitude}', limit=2)
  return [feature.properties for feature in alerts.features]


def get_hourly_forecast(location: Location):
  forecast_obj = nws_rest_api.gridpoint_forecast_hourly(*location.get_gridpoint())
  return forecast_obj.properties['periods']


def get_forecast(location: Location):
  forecast_obj = nws_rest_api.gridpoint_forecast(*location.get_gridpoint())
  return forecast_obj.properties['periods']


def f_to_c(temp):
  return (temp - 32) * 5 / 9


def c_to_f(temp):
  return temp * 9 / 5 + 32


def temp_with_unit(temp, cur_unit, desired_unit):
  if cur_unit not in ('F', 'C') or desired_unit not in ('F', 'C'):
    raise AttributeError('unit must be either F or C')

  if cur_unit == 'F':
    if desired_unit == 'F':
      return temp
    else:
      return f_to_c(temp)
  else:
    if desired_unit == 'F':
      return c_to_f(temp)
    else:
      return temp
  

def get_high_low(location: Location, unit='F'):
  if unit not in ('F', 'C'):
    raise AttributeError('unit must be either F or C')

  forecast = get_forecast(location)
  high = None
  low = None
  for period in forecast:
    if period['name'] not in ('Today', 'Tonight'):
      continue
    temp = temp_with_unit(period['temperature'], period['temperatureUnit'][-1].upper(), unit)
    if period['name'] == 'Today':
      high = temp
    elif period['name'] == 'Tonight':
      low = temp
    else:
      continue

  return high, low


def get_product(type: str, location: Location, limit=1):
  products = nws_rest_api.products_type_location(type, location.get_office_id())
  product_ids = [ref.id for ref in products.graph[:limit]]
  return [nws_rest_api.product(id) for id in product_ids]


def list_product_types():
  return nws_rest_api.product_types().graph


def get_headlines(location: Location):
  headlines = nws_rest_api.office_headlines(location.get_office_id())
  return headlines.graph


def get_zone_forecast(location: Location):
  forecast = nws_rest_api.zone_forecast(type='forecast', zone_id=location.get_zone_id())
  return forecast.properties['periods']


def get_observation(location: Location):
  observation = nws_rest_api.station_observation_latest(station_id=location.get_station_id())
  return observation.properties


def get_current_temp(location: Location, unit='F'):
  if unit not in ('F', 'C'):
    raise AttributeError('unit must be either F or C')
  observation = get_observation(location)

  temp = observation['temperature']['value']

  cur_unit = observation['temperature']['unitCode'][-1].upper()
  return temp_with_unit(temp, cur_unit, unit)
