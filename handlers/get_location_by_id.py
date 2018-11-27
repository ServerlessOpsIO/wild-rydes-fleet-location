'''Get location of device'''

import json
import logging
import os


log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))  # type: ignore
_logger = logging.getLogger(__name__)

# Dummy table
LOCATION_TABLE = {
    '212dee58-f26a-11e8-b171-8c859074f8c7': {'Latitude': 42.348053, 'Longitude': -71.084883},
    '21fc3d3a-f26a-11e8-9109-8c859074f8c7': {'Latitude': 42.364848, 'Longitude': -71.019217},
    '2279df58-f26a-11e8-9b3b-8c859074f8c7': {'Latitude': 42.300698, 'Longitude': -71.113918},
}


def _get_fleet_member_location_by_id(device_id: str) -> dict:
    '''Return a tuple of latitude and logitude'''
    location = LOCATION_TABLE.get(device_id)
    if not location:
        location = {'Latitude': None, 'Longitude': None}
    return location


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event received: {}'.format(json.dumps(event)))

    device_id = event.get('pathParameters').get('id')

    location = _get_fleet_member_location_by_id(device_id)

    resp_body = {
        'Location': location
    }

    resp = {
        'body': json.dumps(resp_body)
    }
    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp

