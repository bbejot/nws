# coding: utf-8

"""
    weather.gov API

    weather.gov API  # noqa: E501

    OpenAPI spec version: 1.8.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Observation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'JsonLdContext',
        'geometry': 'GeometryString',
        'id': 'str',
        'type': 'str',
        'elevation': 'QuantitativeValue',
        'station': 'str',
        'timestamp': 'datetime',
        'raw_message': 'str',
        'text_description': 'str',
        'icon': 'str',
        'present_weather': 'list[MetarPhenomenon]',
        'temperature': 'QuantitativeValue',
        'dewpoint': 'QuantitativeValue',
        'wind_direction': 'QuantitativeValue',
        'wind_speed': 'QuantitativeValue',
        'wind_gust': 'QuantitativeValue',
        'barometric_pressure': 'QuantitativeValue',
        'sea_level_pressure': 'QuantitativeValue',
        'visibility': 'QuantitativeValue',
        'max_temperature_last24_hours': 'QuantitativeValue',
        'min_temperature_last24_hours': 'QuantitativeValue',
        'precipitation_last_hour': 'QuantitativeValue',
        'precipitation_last3_hours': 'QuantitativeValue',
        'precipitation_last6_hours': 'QuantitativeValue',
        'relative_humidity': 'QuantitativeValue',
        'wind_chill': 'QuantitativeValue',
        'heat_index': 'QuantitativeValue',
        'cloud_layers': 'list[ObservationCloudLayers]'
    }

    attribute_map = {
        'context': '@context',
        'geometry': 'geometry',
        'id': '@id',
        'type': '@type',
        'elevation': 'elevation',
        'station': 'station',
        'timestamp': 'timestamp',
        'raw_message': 'rawMessage',
        'text_description': 'textDescription',
        'icon': 'icon',
        'present_weather': 'presentWeather',
        'temperature': 'temperature',
        'dewpoint': 'dewpoint',
        'wind_direction': 'windDirection',
        'wind_speed': 'windSpeed',
        'wind_gust': 'windGust',
        'barometric_pressure': 'barometricPressure',
        'sea_level_pressure': 'seaLevelPressure',
        'visibility': 'visibility',
        'max_temperature_last24_hours': 'maxTemperatureLast24Hours',
        'min_temperature_last24_hours': 'minTemperatureLast24Hours',
        'precipitation_last_hour': 'precipitationLastHour',
        'precipitation_last3_hours': 'precipitationLast3Hours',
        'precipitation_last6_hours': 'precipitationLast6Hours',
        'relative_humidity': 'relativeHumidity',
        'wind_chill': 'windChill',
        'heat_index': 'heatIndex',
        'cloud_layers': 'cloudLayers'
    }

    def __init__(self, context=None, geometry=None, id=None, type=None, elevation=None, station=None, timestamp=None, raw_message=None, text_description=None, icon=None, present_weather=None, temperature=None, dewpoint=None, wind_direction=None, wind_speed=None, wind_gust=None, barometric_pressure=None, sea_level_pressure=None, visibility=None, max_temperature_last24_hours=None, min_temperature_last24_hours=None, precipitation_last_hour=None, precipitation_last3_hours=None, precipitation_last6_hours=None, relative_humidity=None, wind_chill=None, heat_index=None, cloud_layers=None):  # noqa: E501
        """Observation - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._geometry = None
        self._id = None
        self._type = None
        self._elevation = None
        self._station = None
        self._timestamp = None
        self._raw_message = None
        self._text_description = None
        self._icon = None
        self._present_weather = None
        self._temperature = None
        self._dewpoint = None
        self._wind_direction = None
        self._wind_speed = None
        self._wind_gust = None
        self._barometric_pressure = None
        self._sea_level_pressure = None
        self._visibility = None
        self._max_temperature_last24_hours = None
        self._min_temperature_last24_hours = None
        self._precipitation_last_hour = None
        self._precipitation_last3_hours = None
        self._precipitation_last6_hours = None
        self._relative_humidity = None
        self._wind_chill = None
        self._heat_index = None
        self._cloud_layers = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if geometry is not None:
            self.geometry = geometry
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if elevation is not None:
            self.elevation = elevation
        if station is not None:
            self.station = station
        if timestamp is not None:
            self.timestamp = timestamp
        if raw_message is not None:
            self.raw_message = raw_message
        if text_description is not None:
            self.text_description = text_description
        if icon is not None:
            self.icon = icon
        if present_weather is not None:
            self.present_weather = present_weather
        if temperature is not None:
            self.temperature = temperature
        if dewpoint is not None:
            self.dewpoint = dewpoint
        if wind_direction is not None:
            self.wind_direction = wind_direction
        if wind_speed is not None:
            self.wind_speed = wind_speed
        if wind_gust is not None:
            self.wind_gust = wind_gust
        if barometric_pressure is not None:
            self.barometric_pressure = barometric_pressure
        if sea_level_pressure is not None:
            self.sea_level_pressure = sea_level_pressure
        if visibility is not None:
            self.visibility = visibility
        if max_temperature_last24_hours is not None:
            self.max_temperature_last24_hours = max_temperature_last24_hours
        if min_temperature_last24_hours is not None:
            self.min_temperature_last24_hours = min_temperature_last24_hours
        if precipitation_last_hour is not None:
            self.precipitation_last_hour = precipitation_last_hour
        if precipitation_last3_hours is not None:
            self.precipitation_last3_hours = precipitation_last3_hours
        if precipitation_last6_hours is not None:
            self.precipitation_last6_hours = precipitation_last6_hours
        if relative_humidity is not None:
            self.relative_humidity = relative_humidity
        if wind_chill is not None:
            self.wind_chill = wind_chill
        if heat_index is not None:
            self.heat_index = heat_index
        if cloud_layers is not None:
            self.cloud_layers = cloud_layers

    @property
    def context(self):
        """Gets the context of this Observation.  # noqa: E501


        :return: The context of this Observation.  # noqa: E501
        :rtype: JsonLdContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this Observation.


        :param context: The context of this Observation.  # noqa: E501
        :type: JsonLdContext
        """

        self._context = context

    @property
    def geometry(self):
        """Gets the geometry of this Observation.  # noqa: E501


        :return: The geometry of this Observation.  # noqa: E501
        :rtype: GeometryString
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this Observation.


        :param geometry: The geometry of this Observation.  # noqa: E501
        :type: GeometryString
        """

        self._geometry = geometry

    @property
    def id(self):
        """Gets the id of this Observation.  # noqa: E501


        :return: The id of this Observation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Observation.


        :param id: The id of this Observation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Observation.  # noqa: E501


        :return: The type of this Observation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Observation.


        :param type: The type of this Observation.  # noqa: E501
        :type: str
        """
        allowed_values = ["wx:ObservationStation"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def elevation(self):
        """Gets the elevation of this Observation.  # noqa: E501


        :return: The elevation of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this Observation.


        :param elevation: The elevation of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._elevation = elevation

    @property
    def station(self):
        """Gets the station of this Observation.  # noqa: E501


        :return: The station of this Observation.  # noqa: E501
        :rtype: str
        """
        return self._station

    @station.setter
    def station(self, station):
        """Sets the station of this Observation.


        :param station: The station of this Observation.  # noqa: E501
        :type: str
        """

        self._station = station

    @property
    def timestamp(self):
        """Gets the timestamp of this Observation.  # noqa: E501


        :return: The timestamp of this Observation.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Observation.


        :param timestamp: The timestamp of this Observation.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def raw_message(self):
        """Gets the raw_message of this Observation.  # noqa: E501


        :return: The raw_message of this Observation.  # noqa: E501
        :rtype: str
        """
        return self._raw_message

    @raw_message.setter
    def raw_message(self, raw_message):
        """Sets the raw_message of this Observation.


        :param raw_message: The raw_message of this Observation.  # noqa: E501
        :type: str
        """

        self._raw_message = raw_message

    @property
    def text_description(self):
        """Gets the text_description of this Observation.  # noqa: E501


        :return: The text_description of this Observation.  # noqa: E501
        :rtype: str
        """
        return self._text_description

    @text_description.setter
    def text_description(self, text_description):
        """Sets the text_description of this Observation.


        :param text_description: The text_description of this Observation.  # noqa: E501
        :type: str
        """

        self._text_description = text_description

    @property
    def icon(self):
        """Gets the icon of this Observation.  # noqa: E501


        :return: The icon of this Observation.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Observation.


        :param icon: The icon of this Observation.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def present_weather(self):
        """Gets the present_weather of this Observation.  # noqa: E501


        :return: The present_weather of this Observation.  # noqa: E501
        :rtype: list[MetarPhenomenon]
        """
        return self._present_weather

    @present_weather.setter
    def present_weather(self, present_weather):
        """Sets the present_weather of this Observation.


        :param present_weather: The present_weather of this Observation.  # noqa: E501
        :type: list[MetarPhenomenon]
        """

        self._present_weather = present_weather

    @property
    def temperature(self):
        """Gets the temperature of this Observation.  # noqa: E501


        :return: The temperature of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this Observation.


        :param temperature: The temperature of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._temperature = temperature

    @property
    def dewpoint(self):
        """Gets the dewpoint of this Observation.  # noqa: E501


        :return: The dewpoint of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._dewpoint

    @dewpoint.setter
    def dewpoint(self, dewpoint):
        """Sets the dewpoint of this Observation.


        :param dewpoint: The dewpoint of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._dewpoint = dewpoint

    @property
    def wind_direction(self):
        """Gets the wind_direction of this Observation.  # noqa: E501


        :return: The wind_direction of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, wind_direction):
        """Sets the wind_direction of this Observation.


        :param wind_direction: The wind_direction of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._wind_direction = wind_direction

    @property
    def wind_speed(self):
        """Gets the wind_speed of this Observation.  # noqa: E501


        :return: The wind_speed of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed):
        """Sets the wind_speed of this Observation.


        :param wind_speed: The wind_speed of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._wind_speed = wind_speed

    @property
    def wind_gust(self):
        """Gets the wind_gust of this Observation.  # noqa: E501


        :return: The wind_gust of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._wind_gust

    @wind_gust.setter
    def wind_gust(self, wind_gust):
        """Sets the wind_gust of this Observation.


        :param wind_gust: The wind_gust of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._wind_gust = wind_gust

    @property
    def barometric_pressure(self):
        """Gets the barometric_pressure of this Observation.  # noqa: E501


        :return: The barometric_pressure of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._barometric_pressure

    @barometric_pressure.setter
    def barometric_pressure(self, barometric_pressure):
        """Sets the barometric_pressure of this Observation.


        :param barometric_pressure: The barometric_pressure of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._barometric_pressure = barometric_pressure

    @property
    def sea_level_pressure(self):
        """Gets the sea_level_pressure of this Observation.  # noqa: E501


        :return: The sea_level_pressure of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._sea_level_pressure

    @sea_level_pressure.setter
    def sea_level_pressure(self, sea_level_pressure):
        """Sets the sea_level_pressure of this Observation.


        :param sea_level_pressure: The sea_level_pressure of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._sea_level_pressure = sea_level_pressure

    @property
    def visibility(self):
        """Gets the visibility of this Observation.  # noqa: E501


        :return: The visibility of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Observation.


        :param visibility: The visibility of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._visibility = visibility

    @property
    def max_temperature_last24_hours(self):
        """Gets the max_temperature_last24_hours of this Observation.  # noqa: E501


        :return: The max_temperature_last24_hours of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._max_temperature_last24_hours

    @max_temperature_last24_hours.setter
    def max_temperature_last24_hours(self, max_temperature_last24_hours):
        """Sets the max_temperature_last24_hours of this Observation.


        :param max_temperature_last24_hours: The max_temperature_last24_hours of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._max_temperature_last24_hours = max_temperature_last24_hours

    @property
    def min_temperature_last24_hours(self):
        """Gets the min_temperature_last24_hours of this Observation.  # noqa: E501


        :return: The min_temperature_last24_hours of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._min_temperature_last24_hours

    @min_temperature_last24_hours.setter
    def min_temperature_last24_hours(self, min_temperature_last24_hours):
        """Sets the min_temperature_last24_hours of this Observation.


        :param min_temperature_last24_hours: The min_temperature_last24_hours of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._min_temperature_last24_hours = min_temperature_last24_hours

    @property
    def precipitation_last_hour(self):
        """Gets the precipitation_last_hour of this Observation.  # noqa: E501


        :return: The precipitation_last_hour of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._precipitation_last_hour

    @precipitation_last_hour.setter
    def precipitation_last_hour(self, precipitation_last_hour):
        """Sets the precipitation_last_hour of this Observation.


        :param precipitation_last_hour: The precipitation_last_hour of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._precipitation_last_hour = precipitation_last_hour

    @property
    def precipitation_last3_hours(self):
        """Gets the precipitation_last3_hours of this Observation.  # noqa: E501


        :return: The precipitation_last3_hours of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._precipitation_last3_hours

    @precipitation_last3_hours.setter
    def precipitation_last3_hours(self, precipitation_last3_hours):
        """Sets the precipitation_last3_hours of this Observation.


        :param precipitation_last3_hours: The precipitation_last3_hours of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._precipitation_last3_hours = precipitation_last3_hours

    @property
    def precipitation_last6_hours(self):
        """Gets the precipitation_last6_hours of this Observation.  # noqa: E501


        :return: The precipitation_last6_hours of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._precipitation_last6_hours

    @precipitation_last6_hours.setter
    def precipitation_last6_hours(self, precipitation_last6_hours):
        """Sets the precipitation_last6_hours of this Observation.


        :param precipitation_last6_hours: The precipitation_last6_hours of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._precipitation_last6_hours = precipitation_last6_hours

    @property
    def relative_humidity(self):
        """Gets the relative_humidity of this Observation.  # noqa: E501


        :return: The relative_humidity of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._relative_humidity

    @relative_humidity.setter
    def relative_humidity(self, relative_humidity):
        """Sets the relative_humidity of this Observation.


        :param relative_humidity: The relative_humidity of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._relative_humidity = relative_humidity

    @property
    def wind_chill(self):
        """Gets the wind_chill of this Observation.  # noqa: E501


        :return: The wind_chill of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._wind_chill

    @wind_chill.setter
    def wind_chill(self, wind_chill):
        """Sets the wind_chill of this Observation.


        :param wind_chill: The wind_chill of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._wind_chill = wind_chill

    @property
    def heat_index(self):
        """Gets the heat_index of this Observation.  # noqa: E501


        :return: The heat_index of this Observation.  # noqa: E501
        :rtype: QuantitativeValue
        """
        return self._heat_index

    @heat_index.setter
    def heat_index(self, heat_index):
        """Sets the heat_index of this Observation.


        :param heat_index: The heat_index of this Observation.  # noqa: E501
        :type: QuantitativeValue
        """

        self._heat_index = heat_index

    @property
    def cloud_layers(self):
        """Gets the cloud_layers of this Observation.  # noqa: E501


        :return: The cloud_layers of this Observation.  # noqa: E501
        :rtype: list[ObservationCloudLayers]
        """
        return self._cloud_layers

    @cloud_layers.setter
    def cloud_layers(self, cloud_layers):
        """Sets the cloud_layers of this Observation.


        :param cloud_layers: The cloud_layers of this Observation.  # noqa: E501
        :type: list[ObservationCloudLayers]
        """

        self._cloud_layers = cloud_layers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Observation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Observation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other