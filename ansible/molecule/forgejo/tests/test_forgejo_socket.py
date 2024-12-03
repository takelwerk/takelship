import takeltest
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.forgejo
def test_forgejo_podman_socket_file(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    podman_socket = testvars['takel_ship_dind_podman_socket']
    file = host.file(podman_socket['file'])
    socket = host.socket(podman_socket['socket'])

    assert file.exists
    assert file.is_socket
    assert file.user == user
    assert file.group == group
    assert file.mode == 0o666

    assert socket.is_listening


@pytest.mark.forgejo
def test_forgejo_podman_socket_query(host, testvars):
    podman_socket = testvars['takel_ship_dind_podman_socket']
    socket_file = podman_socket['file']
    curl_cmd = (f"curl "
                f"--unix-socket {socket_file} "
                f"http://latest/containers/json")
    curl_result = host.check_output(curl_cmd)

    assert 'forgejo' in curl_result
