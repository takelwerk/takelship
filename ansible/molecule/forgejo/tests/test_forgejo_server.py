import takeltest
import pytest
import json
from time import sleep

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.forgejo
def test_forgejo_server_setup_page(host, testvars):
    port = testvars['takel_ship_forgejo_server_http_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd_curl_server = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}")

    for _ in range(30):
        curl_run = host.run(cmd_curl_server)
        if curl_run.exit_status == 0:
            break
        sleep(1)

    curl_result = host.check_output(cmd_curl_server)
    expected = 'Forgejo: Beyond coding. We forge.'
    unexpected = 'Installation'

    assert expected in curl_result
    assert unexpected not in curl_result


@pytest.mark.forgejo
def test_forgejo_server_api_query(host, testvars):
    port = testvars['takel_ship_forgejo_server_http_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']

    for _ in range(30):
        cmd_curl_server = (
            f"{cmd} curl "
            "--insecure "
            f"http://localhost:{port}/api/v1/version")
        curl_run = host.run(cmd_curl_server)
        if curl_run.exit_status == 0:
            break
        sleep(1)

    cmd_curl_server = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}/api/v1/version")
    curl_result = host.check_output(cmd_curl_server)
    result = json.loads(curl_result)

    assert 'version' in result
