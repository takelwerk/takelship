import takeltest
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.forgejo
def test_forgejo_ship_ports(host, testvars):
    port_forgejo_server_ssh = 50022
    port_forgejo_server_http = 53000
    port_portainer_server_http = 59000
    port_takelship_registry_http = 52375

    env_port_forgejo_server_ssh = \
        f"\nTAKELSHIP_FORGEJO_SERVER_HTTP_33000={port_forgejo_server_http}\n"
    env_forgejo_server_http = \
        f"\nTAKELSHIP_FORGEJO_SERVER_SSH=30022{port_forgejo_server_ssh}\n"
    env_portainer_server_http = \
        f"\nTAKELSHIP_PORTAINER_SERVER_HTTP_39000={port_portainer_server_http}\n"
    env_takelship_registry_http = \
        f"\nTAKELSHIP_REGISTRY_HTTP_5555={port_takelship_registry_http}\n"

    env_docker_forgejo_server_file = \
        '/home/podman/data/services/forgejo-server/env-docker'
    env_docker_portainer_server_file = \
        '/home/podman/data/services/portainer-server/env-docker'
    env_docker_takelship_registry_file = \
        '/home/podman/data/services/takelship-registry/env-docker'

    env_docker_forgejo_server = host(env_docker_forgejo_server_file).content
    env_docker_portainer_server = host(env_docker_portainer_server_file).content
    env_docker_takelship_registry = host(env_docker_takelship_registry_file).content

    assert env_port_forgejo_server_ssh in env_docker_forgejo_server
    assert env_forgejo_server_http in env_docker_forgejo_server_file
    assert env_portainer_server_http in env_docker_portainer_server
    assert env_takelship_registry_http in env_docker_takelship_registry
