# -*- coding: utf-8 -*-
from requests.models import Response

from service_flower import models


class TestBaseFlowerClientResponse(object):
    def test_response(self):
        data = {'color': 'red', 'age': 25}
        mock_response = Response()
        mock_response.status_code = 200
        mock_response.json = lambda: data

        response = models.BaseFlowerClientResponse(mock_response)
        assert response['color'] == data['color']
        assert response['age'] == data['age']
        assert response.raw_response == mock_response
        assert response.status_code == 200
        assert response.ok
