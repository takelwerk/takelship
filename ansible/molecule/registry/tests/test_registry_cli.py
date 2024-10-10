import takeltest
import yaml

testinfra_hosts = [takeltest.hosts()[0]]


def test_registry_cli_no_argument(testvars, docker_client):
    image_user = testvars['project']['local_user']
    image_repo = f"{testvars['project']['name']}-project"
    image = f"{image_user}/{image_repo}:latest"
    result = docker_client.containers.run(
        image, "").decode("utf-8")

    assert "[takelship] This is a takelwerk takelship container" in result
    assert "[takelship] No project selected. Available projects:" in result
    assert "docker run --rm --interactive --tty --name takelship" in result


def test_registry_cli_update(testvars, docker_client):
    image_user = testvars['project']['local_user']
    image_repo = f"{testvars['project']['name']}-project"
    image = f"{image_user}/{image_repo}:latest"
    result = docker_client.containers.run(
        image, "dump").decode("utf-8")

    assert "[takelship] This is a takelwerk takelship container" in result
    assert "[takelship] Preparing podman container environment" in result
    assert "[takelship] Updating data directory" in result


def test_registry_cli_info(testvars, docker_client):
    image_user = testvars['project']['local_user']
    image_repo = f"{testvars['project']['name']}-project"
    image = f"{image_user}/{image_repo}:latest"
    result = docker_client.containers.run(
        image, "info").decode("utf-8")
    takelshipinfo = yaml.safe_load(result)
    assert 'name' in takelshipinfo


def test_registry_cli_root(host, docker_client):
    hostname = host.check_output('hostname')
    container = docker_client.containers.get(hostname)
    result = container.exec_run("whoami").output.decode("utf-8").strip()

    assert 'root' == result


def test_registry_cli_pod(host, docker_client):
    hostname = host.check_output('hostname')
    container = docker_client.containers.get(hostname)
    result = container.exec_run("pod whoami").output.decode("utf-8").strip()

    assert 'podman' == result
