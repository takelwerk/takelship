import takeltest
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.forgejo
def test_forgejo_tea_config(host):
    port_forgejo_server_http = 53000
    tea_config_takelship_url = 'url: http://localhost:33000'
    tea_config_host_url = f"url: http://localhost:{port_forgejo_server_http}"
    bad_token = 'token: TOKEN'

    tea_config_takelship_file = \
        '/home/podman/.config/tea/config.yml'
    tea_config_host_file = \
        '/home/podman/takelship/compose/services/forgejo-server/config.yml'

    tea_config_takelship = (
        host.file(tea_config_takelship_file).content.decode())
    tea_config_host = (
        host.file(tea_config_host_file).content.decode())

    print(tea_config_takelship)
    print(tea_config_host)

    assert tea_config_takelship_url in tea_config_takelship
    assert tea_config_host_url not in tea_config_takelship
    assert bad_token not in tea_config_takelship

    assert tea_config_host_url in tea_config_host
    assert tea_config_takelship_url not in tea_config_host
    assert bad_token not in tea_config_host
