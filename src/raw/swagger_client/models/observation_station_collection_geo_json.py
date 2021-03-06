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
from swagger_client.models.geo_json_feature_collection import GeoJsonFeatureCollection  # noqa: F401,E501

class ObservationStationCollectionGeoJson(GeoJsonFeatureCollection):
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
        'features': 'list[ObservationStationCollectionGeoJsonFeatures]',
        'observation_stations': 'list[str]'
    }
    if hasattr(GeoJsonFeatureCollection, "swagger_types"):
        swagger_types.update(GeoJsonFeatureCollection.swagger_types)

    attribute_map = {
        'features': 'features',
        'observation_stations': 'observationStations'
    }
    if hasattr(GeoJsonFeatureCollection, "attribute_map"):
        attribute_map.update(GeoJsonFeatureCollection.attribute_map)

    def __init__(self, features=None, observation_stations=None, *args, **kwargs):  # noqa: E501
        """ObservationStationCollectionGeoJson - a model defined in Swagger"""  # noqa: E501
        self._features = None
        self._observation_stations = None
        self.discriminator = None
        if features is not None:
            self.features = features
        if observation_stations is not None:
            self.observation_stations = observation_stations
        GeoJsonFeatureCollection.__init__(self, *args, features=features, **kwargs)

    @property
    def features(self):
        """Gets the features of this ObservationStationCollectionGeoJson.  # noqa: E501


        :return: The features of this ObservationStationCollectionGeoJson.  # noqa: E501
        :rtype: list[ObservationStationCollectionGeoJsonFeatures]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ObservationStationCollectionGeoJson.


        :param features: The features of this ObservationStationCollectionGeoJson.  # noqa: E501
        :type: list[ObservationStationCollectionGeoJsonFeatures]
        """

        self._features = features

    @property
    def observation_stations(self):
        """Gets the observation_stations of this ObservationStationCollectionGeoJson.  # noqa: E501


        :return: The observation_stations of this ObservationStationCollectionGeoJson.  # noqa: E501
        :rtype: list[str]
        """
        return self._observation_stations

    @observation_stations.setter
    def observation_stations(self, observation_stations):
        """Sets the observation_stations of this ObservationStationCollectionGeoJson.


        :param observation_stations: The observation_stations of this ObservationStationCollectionGeoJson.  # noqa: E501
        :type: list[str]
        """

        self._observation_stations = observation_stations

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
        if issubclass(ObservationStationCollectionGeoJson, dict):
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
        if not isinstance(other, ObservationStationCollectionGeoJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
