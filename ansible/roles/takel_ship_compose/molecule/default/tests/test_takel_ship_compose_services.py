import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_compose_services_compose_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['file'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    docker_compose_yml = testvars['takel_ship_compose_docker_compose_yml']
    services = testvars['takel_ship_compose_services']
    for service in services:
        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{docker_compose_yml}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_env_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['file'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    env = testvars['takel_ship_compose_env_docker']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'env' not in service:
            continue
        if 'docker' not in service['profiles']:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{env}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_run_docker_down_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    run_docker_down = testvars['takel_ship_compose_run_docker_down']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'docker' not in service['profiles']:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{run_docker_down}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_run_docker_up_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    run_docker_up = testvars['takel_ship_compose_run_docker_up']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'docker' not in service['profiles']:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{run_docker_up}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_run_podman_down_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    run_podman_down = testvars['takel_ship_compose_run_podman_down']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'podman' not in service['profiles']:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{run_podman_down}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_run_podman_up_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    run_podman_up = testvars['takel_ship_compose_run_podman_up']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'podman' not in service['profiles']:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{run_podman_up}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_run_postinstall_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    run_postinstall = testvars['takel_ship_compose_run_postinstall']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'postinstall' not in service:
            continue
        if 'podman' not in service['profiles']:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{run_postinstall}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_run_preinstall_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    run_preinstall = testvars['takel_ship_compose_run_preinstall']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'preinstall' not in service:
            continue
        if 'podman' not in service['profiles']:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{run_preinstall}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_services_dockerfile_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['file'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    dockerfile = testvars['takel_ship_compose_dockerfile']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'dockerfile' not in service:
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{services_dir}/"
            f"{service['name']}/{dockerfile}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode
