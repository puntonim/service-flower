# -*- coding: utf-8 -*-
import pytest
from requests import HTTPError

from service_flower import states
from service_flower.client import FlowerClient

# How to import mock PY3 and PY3 compatible:
# from six import MovedModule, add_move  # isort:skip
# add_move(MovedModule('mock', 'mock', 'unittest.mock'))
# from six.moves import mock  # noqa:E402 isort:skip


class TestGetTasks(object):
    def setup(self):
        self.client = FlowerClient()

    def test_happy_flow(self):
        response = self.client.get_tasks(limit=2)
        response.raise_for_result()
        assert response.ok
        assert len(response) == 2
        assert response['508fe6e2-ac99-4096-ad8d-d572574418de']['name'] == \
            'inspirehep.modules.migrator.tasks.migrate_recids_from_mirror'

    def test_taskname(self):
        taskname = 'inspirehep.modules.migrator.tasks.continuous_migration'
        response = self.client.get_tasks(taskname=taskname)
        response.raise_for_result()
        for task in response.values():
            assert task['name'] == taskname

    def test_state(self):
        state = states.RECEIVED
        response = self.client.get_tasks(state=state)
        response.raise_for_result()
        for task in response.values():
            assert task['state'] == state

    def test_assert_500(self):
        response = self.client.get_tasks()
        with pytest.raises(HTTPError):
            response.raise_for_result()
        assert not response.ok


class TestGetTaskInfo(object):
    def setup(self):
        self.client = FlowerClient()

    def test_happy_flow(self):
        task_id = '42c661b6-90e1-4087-8ba6-21a040d56c41'
        response = self.client.get_task_info(task_id)
        response.raise_for_result()
        assert response.ok
        assert response['worker'] == 'celery@inspire-qa-worker3-task6.cern.ch'
        assert response['state'] == 'RECEIVED'


class TestGetWorkers(object):
    def setup(self):
        self.client = FlowerClient()

    def test_happy_flow(self):
        response = self.client.get_workers(
            workername='celery@inspire-qa-worker3-task5.cern.ch',)
        response.raise_for_result()
        assert response.ok
        assert response.get_active_queues_names('celery@inspire-qa-worker3-task5.cern.ch') == [
            'celery', 'harvests', 'migrator', 'orcid_push', 'orcid_push_legacy_tokens']
