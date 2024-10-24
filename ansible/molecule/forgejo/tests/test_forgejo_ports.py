import takeltest
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.forgejo
def test_forgejo_ship_ports(host, testvars):
    port_forgejo_server_ssh = 50022
    port_forgejo_server_http = 53000
    port_takelship_registry_http = 52375
    port_aptproxy_server_http = 53142

    env_port_forgejo_server_http = \
        f"\nTAKELSHIP_FORGEJO_SERVER_HTTP_33000=" \
        f"{port_forgejo_server_http}\n"
    env_port_forgejo_server_ssh = \
        f"\nTAKELSHIP_FORGEJO_SERVER_SSH_30022=" \
        f"{port_forgejo_server_ssh}\n"
    env_port_takelship_registry_http = \
        f"\nTAKELSHIP_TAKELSHIP_REGISTRY_HTTP_5555=" \
        f"{port_takelship_registry_http}\n"
    env_port_aptproxy_server_http = \
        f"\nTAKELSHIP_APTPROXY_SERVER_HTTP_33142=" \
        f"{port_aptproxy_server_http}\n"

    env_docker_forgejo_server_file = \
        '/home/podman/takelship/compose/services/forgejo-server/env-docker'
    env_docker_aptproxy_server_file = \
        '/home/podman/takelship/compose/services/aptproxy-server/env-docker'
    env_docker_takelship_registry_file = \
        '/home/podman/takelship/compose/services/takelship-registry/env-docker'

    env_docker_forgejo_server = (
        host.file(env_docker_forgejo_server_file).content.decode())
    env_docker_aptproxy_server = (
        host.file(env_docker_aptproxy_server_file).content.decode())
    env_docker_takelship_registry = (
        host.file(env_docker_takelship_registry_file).content.decode())

    assert env_port_forgejo_server_ssh in env_docker_forgejo_server
    assert env_port_forgejo_server_http in env_docker_forgejo_server
    assert env_port_aptproxy_server_http in env_docker_aptproxy_server
    assert env_port_takelship_registry_http in env_docker_takelship_registry
