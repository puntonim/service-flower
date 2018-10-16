# -*- coding: utf-8 -*-
import requests
import urllib3

from service_flower.conf import settings

from . import models, states

# Suppress warnings related to the invalid SSL certificate for Flower API.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FlowerClient(object):
    REQUESTS_BASE_KWARGS = dict(
        verify=False,
        auth=(settings.HTTP_AUTH_USERNAME, settings.HTTP_AUTH_PASSWORD),
        timeout=settings.REQUEST_TIMEOUT,
    )

    def get_tasks(self, taskname='', state=None, limit=25):
        """
        Get all tasks filtering by taskname and/or state.
        $ curl -u username:password -k "https://inspire-prod-worker3-task1.cern.ch/api/tasks?taskname=inspirehep.modules.orcid.tasks.orcid_push&limit=10"
        """  # noqa: E501
        endpoint = 'tasks'
        query = 'taskname={}'.format(taskname) if taskname else ''
        query += '&limit={}'.format(limit) if limit else ''

        if state and state not in states.ALL_STATES:
            raise ValueError('Allowed states: {}'.format(states.ALL_STATES))
        query += '&state={}'.format(state) if state else ''

        url = '{}/{}?{}'.format(settings.BASE_URL, endpoint, query)

        response = requests.get(url, **self.REQUESTS_BASE_KWARGS)
        return models.GetTasksResponse(response)

    def get_task_info(self, task_id):
        """
        Get a task info.
        $ curl -u username:password -k "https://inspire-prod-worker3-task1.cern.ch/api/task/info/7d4d92db-39d0-4918-bd86-7ec243ba008d"
        """  # noqa: E501
        endpoint = 'task/info'
        url = '{}/{}/{}'.format(settings.BASE_URL, endpoint, task_id)

        response = requests.get(url, **self.REQUESTS_BASE_KWARGS)
        return models.GetTaskInfoResponse(response)

    def get_workers(self, workername=None, status_only=False):
        """
        Get workers info:
        $ curl -u username:password -k "https://inspire-prod-worker3-task1.cern.ch/api/workers?workername=celery@inspire-qa-worker3-task5.cern.ch"
        """  # noqa: E501
        endpoint = 'workers'
        query = 'workername={}'.format(workername) if workername else ''
        query += '&status=true' if status_only else ''

        url = '{}/{}?{}'.format(settings.BASE_URL, endpoint, query)

        response = requests.get(url, **self.REQUESTS_BASE_KWARGS)
        return models.GetWorkersResponse(response)
