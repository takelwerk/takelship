import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_compose_compose_services_compose_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['file'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    service_filename = testvars['takel_ship_compose_service_filename']
    service_fileext = testvars['takel_ship_compose_service_fileext']
    services = testvars['takel_ship_compose_services']
    for service in services:
        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/"
            f"{service['name']}/{service_filename}.{service_fileext}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_compose_services_env_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['file'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'env' not in service:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/"
            f"{service['name']}/env")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_compose_services_copy_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'env' not in service:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/"
            f"{service['name']}/copy-image")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_compose_services_run_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'env' not in service:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/"
            f"{service['name']}/run-docker")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode
