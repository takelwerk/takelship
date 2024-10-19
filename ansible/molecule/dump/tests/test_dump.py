import takeltest
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.dump
def test_dump_project_dir(host, testvars):
    assert True
