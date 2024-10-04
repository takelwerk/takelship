import takeltest
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.forgejo
def test_forgejo_podman_socket(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    podman_socket = testvars['takel_ship_podman_socket']
    socket = host.socket(podman_socket['socket'])
    file = host.file(podman_socket['path'])

    assert file.exists
    assert file.is_socket
    assert file.user == user
    assert file.group == group
    assert file.mode == 0o600

    assert socket.is_listening
