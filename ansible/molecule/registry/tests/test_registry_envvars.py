import takeltest
import json

testinfra_hosts = [takeltest.hosts()[0]]


def test_registry_envvars_service_disabled(host):
    cmd_podman = f"pod podman ps -a -q -f name='docker-dind'"

    assert '' == host.check_output(cmd_podman)
