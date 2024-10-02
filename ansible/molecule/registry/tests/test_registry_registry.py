import takeltest
import json

testinfra_hosts = [takeltest.hosts()[0]]


def test_image_takelship_registry(host, testvars):
    image = testvars['takel_ship_registry_ui_image']['name']
    expected_images = [image]
    port = testvars['takel_ship_registry_takelship_registry_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd_curl = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}/v2/_catalog")
    curl_result = host.check_output(cmd_curl)
    registry_images = json.loads(curl_result)['repositories']

    assert expected_images == registry_images


def test_image_registry_server(host, testvars):
    expected_images = ['myregistry']
    image = testvars['takel_ship_registry_server_image']['name']
    tag = testvars['takel_ship_registry_server_image']['tag']
    port = testvars['takel_ship_registry_server_http_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd_tag = f"{cmd} podman tag {image}:{tag} localhost:{port}/myregistry:{tag}"

    assert host.run_expect([0], cmd_tag)
    cmd_push = f"{cmd} podman push localhost:{port}/myregistry:{tag}"

    assert host.run_expect([0], cmd_push)
    cmd_curl_server = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}/v2/_catalog")
    curl_result = host.check_output(cmd_curl_server)
    registry_images = json.loads(curl_result)['repositories']

    assert expected_images == registry_images


def test_image_registry_ui(host, testvars):
    port = testvars['takel_ship_registry_ui_http_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd_curl_server = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}/v2/_catalog")
    curl_result = host.check_output(cmd_curl_server)

    assert 'Quiq Inc.' in curl_result
