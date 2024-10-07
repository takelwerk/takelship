import takeltest
import json

testinfra_hosts = [takeltest.hosts()[0]]


def test_registry_takelship_registry(host, testvars):
    image_socat = testvars['takel_ship_dind_docker_image']['name']
    image_ui = testvars['takel_ship_registry_ui_image']['name']
    expected_images = [image_socat, image_ui]
    port = testvars['takel_ship_registry_takelship_registry_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd_curl = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}/v2/_catalog")
    curl_result = host.check_output(cmd_curl)
    registry_images = json.loads(curl_result)['repositories']

    assert expected_images == registry_images


def test_registry_registry_server(host, testvars):
    expected_images = ['myregistry']
    image = testvars['takel_ship_registry_server_image']['name']
    tag = testvars['takel_ship_registry_server_image']['tag']
    port = testvars['takel_ship_registry_server_http_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd_tag = (f"{cmd} podman tag "
               f"{image}:{tag} localhost:{port}/myregistry:{tag}")

    assert host.run_expect([0], cmd_tag)
    cmd_push = (f"{cmd} podman push "
                f"localhost:{port}/myregistry:{tag}")

    assert host.run_expect([0], cmd_push)
    cmd_curl_server = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}/v2/_catalog")
    curl_result = host.check_output(cmd_curl_server)
    registry_images = json.loads(curl_result)['repositories']

    assert expected_images == registry_images


def test_registry_registry_ui(host, testvars):
    port = testvars['takel_ship_registry_ui_http_port']['port']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd_curl_server = (
        f"{cmd} curl "
        "--insecure "
        f"http://localhost:{port}/v2/_catalog")
    curl_result = host.check_output(cmd_curl_server)

    assert 'Quiq Inc.' in curl_result
