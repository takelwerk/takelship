import takeltest
import pytest
import json
from time import sleep

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.dump
def test_dump_project_dir(host, testvars):
    assert True
