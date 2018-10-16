# -*- coding: utf-8 -*-


class BaseFlowerClientResponse(dict):
    exceptions = []

    def __init__(self, response):
        self.raw_response = response
        try:
            data = response.json()
        except ValueError:
            data = dict(content=response.content)
        super(BaseFlowerClientResponse, self).__init__(data)

    @property
    def ok(self):
        return self.raw_response.ok

    @property
    def status_code(self):
        return self.raw_response.status_code

    @property
    def request(self):
        return self.raw_response.request

    def raise_for_result(self):
        """
        Raise one of the known exceptions (in self.exceptions) depending on the
        matching criteria; or raise requests.exceptions.HTTPError.
        In case of no errors no exception is raised.
        """
        for exception_class in self.exceptions:
            if exception_class.match(self):
                exception_object = exception_class(str(self))
                exception_object.raw_response = self.raw_response
                raise exception_object
        # Can raise requests.exceptions.HTTPError.
        return self.raw_response.raise_for_status()


class GetTasksResponse(BaseFlowerClientResponse):
    """
    A dict-like object as:
    {
      "fa929218-b49d-44e9-a5a3-8a94c8e0ca29": {
        "root_id": "fa929218-b49d-44e9-a5a3-8a94c8e0ca29",
        "result": "None",
        "children": [],
        "uuid": "fa929218-b49d-44e9-a5a3-8a94c8e0ca29",
        "clock": 167456,
        "exchange": null,
        "routing_key": null,
        "failed": null,
        "state": "SUCCESS",
        "client": null,
        "parent_id": null,
        "kwargs": "{'orcid': '0000-0002-0942-XXXX', 'oauth_token': 'mytoken', 'rec_id': 1678462}",
        "sent": null,
        "expires": null,
        "parent": null,
        "retries": 0,
        "started": 1531213555.923144,
        "timestamp": 1531213557.500176,
        "args": "()",
        "rejected": null,
        "name": "inspirehep.modules.orcid.tasks.orcid_push",
        "received": 1531213263.680338,
        "exception": null,
        "revoked": null,
        "succeeded": 1531213557.500176,
        "traceback": null,
        "eta": null,
        "retried": null,
        "runtime": 1.5760211059823632,
        "root": "fa929218-b49d-44e9-a5a3-8a94c8e0ca29"
      },
      ...
    }
    """  # noqa: E501
    pass


class GetTaskInfoResponse(BaseFlowerClientResponse):
    """
    A dict-like object as:
    {
      "root_id": "b4931472-3150-49a2-b33a-ea97d15190dd",
      "result": null,
      "children": [],
      "uuid": "7d4d92db-39d0-4918-bd86-7ec243ba008d",
      "clock": 7258101,
      "exchange": null,
      "routing_key": null,
      "failed": null,
      "state": "STARTED",
      "client": null,
      "parent_id": "b4931472-3150-49a2-b33a-ea97d15190dd",
      "kwargs": "{'orcid': '0000-0002-2064-XXXX', 'oauth_token': 'mytoken', 'rec_id': 1261966}",
      "sent": null,
      "expires": null,
      "parent": "b4931472-3150-49a2-b33a-ea97d15190dd",
      "retries": 0,
      "started": 1531321917.734636,
      "timestamp": 1531321917.734636,
      "args": "()",
      "worker": "celery@inspire-prod-worker3-task5.cern.ch",
      "rejected": null,
      "name": "inspirehep.modules.orcid.tasks.orcid_push",
      "received": 1531321484.761342,
      "exception": null,
      "revoked": null,
      "succeeded": null,
      "traceback": null,
      "eta": null,
      "retried": null,
      "runtime": null,
      "root": "b4931472-3150-49a2-b33a-ea97d15190dd"
    }
    """  # noqa: E501
    pass


class GetWorkersResponse(BaseFlowerClientResponse):
    """
    {
      "celery@inspire-prod-worker3-task5.cern.ch":{
        "scheduled":[],
        "stats":{
          "clock":"115676",
          "pid":2316,
          "broker":{
            "transport_options":{},
            "failover_strategy":"round-robin",
            "login_method":"AMQPLAIN",
            "hostname":"inspire-prod-broker1.cern.ch",
            "userid":"inspire",
            "insist":false,
            "connect_timeout":4,
            "ssl":false,
            "virtual_host":"inspire",
            "heartbeat":120.0,
            "uri_prefix":null,
            "port":5672,
            "transport":"amqp",
            "alternates":[]
          },
          "prefetch_count":8,
          "total":{
            "invenio_workflows.tasks.resume":12,
            "inspirehep.modules.records.tasks.index_modified_citations_from_record":169,
            "inspire_crawler.tasks.schedule_crawl":3,
            "inspirehep.modules.migrator.tasks.continuous_migration":16,
            "inspirehep.modules.orcid.tasks.orcid_push":1102
          },
          "rusage":{
            "majflt":91,
            "nsignals":0,
            "minflt":120613,
            "maxrss":194228,
            "inblock":96392,
            "nswap":0,
            "idrss":0,
            "msgrcv":0,
            "ixrss":0,
            "isrss":0,
            "nvcsw":117884,
            "stime":7.173639,
            "oublock":104,
            "msgsnd":0,
            "nivcsw":667,
            "utime":62.23651
          },
          "pool":{
            "processes":[
              2467,
              2469
            ],
            "max-concurrency":2,
            "timeouts":[
              0,
              0
            ],
            "writes":{
              "all":"59.29%, 40.71%",
              "avg":"50.00%",
              "inqueues":{
                "active":0,
                "total":2
              },
              "strategy":"fair",
              "raw":"772, 530",
              "total":1302
            },
            "put-guarded-by-semaphore":false,
            "max-tasks-per-child":"N/A"
          }
        },
        "revoked":[],
        "timestamp":1539692391.175565,
        "registered":[
          "inspire_crawler.tasks.schedule_crawl",
          "inspire_crawler.tasks.submit_results",
          "inspirehep.modules.hal.tasks.hal_push",
          "inspirehep.modules.orcid.tasks.orcid_push",
          "invenio_workflows.tasks.start",
          "invenio_workflows_ui.tasks.batch_reindex",
          "invenio_workflows_ui.tasks.resolve_actions"
          ...
        ],
        "active":[],
        "conf":{
          "ADMIN_TEMPLATE_MODE":"bootstrap3",
          ...
        },
        "active_queues":[
          {
            "no_declare":null,
            "exclusive":false,
            "max_priority":null,
            "exchange":{
              "no_declare":false,
              "name":"orcid_push",
              "durable":true,
              "delivery_mode":null,
              "passive":false,
              "arguments":null,
              "type":"direct",
              "auto_delete":false
            },
            "auto_delete":false,
            "expires":null,
            "routing_key":"orcid_push",
            "no_ack":false,
            "alias":null,
            "message_ttl":null,
            "max_length":null,
            "max_length_bytes":null,
            "binding_arguments":null,
            "queue_arguments":null,
            "bindings":[],
            "consumer_arguments":null,
            "durable":true,
            "name":"orcid_push"
          },
          ...
        ],
        "reserved":[]
      },
      ...
    }
    """  # noqa: E501
    def get_active_queues_names(self, workername):
        return [queue['name'] for queue in self[workername]['active_queues']]
