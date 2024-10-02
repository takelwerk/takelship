import takeltest
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.forgejo
def test_forgejo_server_setup_page(host, testvars):
    port = testvars['takel_ship_forgejo_server_http_port']['port']
    cmd_curl_server = (
        "cmd curl "
        "--insecure "
        f"http://localhost:{port}")
    curl_result = host.check_output(cmd_curl_server)
    expected = 'Installation - Forgejo: Beyond coding. We forge.'

    assert expected in curl_result
