[![Build Status](https://travis-ci.org/puntonim/service-flower.svg?branch=master)](https://travis-ci.org/puntonim/service-flower)

# Flower service client

This package is service client for Flower API used to monitor Celery.

## Client usage

```python
# Configure settings.
import service_flower.conf
d = dict(
    BASE_URL='https://inspire-qa-worker3-task1.cern.ch/api',
    REQUEST_TIMEOUT=30,
    HTTP_AUTH_USERNAME='user',
    HTTP_AUTH_PASSWORD='pass',
)
service_flower.conf.settings.configure(**d)

# Use the client.
from service_flower.client import FlowerClient
client = FlowerClient()
response = client.get_workers(workername='celery@inspire-qa-worker3-task5.cern.ch')
response.raise_for_result()
queues = response.get_active_queues_names('celery@inspire-qa-worker3-task5.cern.ch')
```

## Development

```bash
# Create a venv and install the requirements:
$ make venv

# Run isort and lint:
$ make isort
$ make lint

# Run all the tests:
$ make test  # tox against Python27 and Python36.
$ tox -e py27  # tox against a specific Python version.
$ pytest  # pytest against the active venv.

# Run a specific test:
$ make test/tests/test_client.py  # tox against Python27 and Python36.
$ tox -e py27 -- tests/test_client.py  # tox against a specific Python version.
$ pytest tests/test_client.py  # pytest against the active venv.
```

To publish on PyPi, first set the PyPi credentials:

```bash
# Edit .pypirc:
$ cat $HOME/.pypirc
[pypi]
username: myuser
password: mypass
```

```bash
# Edit the version in `setup_gen.py`.
# ... version=pep440_version('1.1.1'),
# Then generate setup.py with:
$ make setup.py
# Commit, tag, push:
$ git commit -m '1.1.1 release'
$ git tag 1.1.1
$ git push origin master --tags

# Finally publish:
$ make publish
```
