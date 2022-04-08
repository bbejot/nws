__all__ = ['swagger_client', 'nws_rest_api']

import os, sys
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR)
import swagger_client
del sys.path[0]

nws_rest_api = swagger_client.DefaultApi()
