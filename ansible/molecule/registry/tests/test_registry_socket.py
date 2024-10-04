import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_registry_podman_socket(host, testvars):
    podman_socket = testvars['takel_ship_podman_socket']
    file = host.file(podman_socket['path'])

    assert not file.exists
