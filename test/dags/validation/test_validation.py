from collections.abc import Callable

import pytest

LOAD_SECOND_THRESHOLD = 2


def test_import_dags(dagbag):
    assert len(dagbag.import_errors) == 0


def test_alert_email_present(dagbag):
    for dag_id, dag in dagbag.dags.items():
        emails = dag.default_args.get('email', [])
        assert len(emails) > 0


@pytest.mark.skip("This is a good idea to have a callback as alerting!")
def test_alert_email_present(dagbag):
    for dag_id, dag in dagbag.dags.items():
        on_failure_callback = dag.default_args.get('on_failure_callback', False)
        assert isinstance(on_failure_callback, Callable)
