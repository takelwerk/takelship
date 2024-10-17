import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_compose_projects_compose_files(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['file'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    projects_dir = testvars['takel_ship_compose_projects_dir']
    docker_compose_yml = testvars['takel_ship_compose_docker_compose_yml']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/{projects_dir}/"
            f"{project['name']}/{docker_compose_yml}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_projects_copy_image_files(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    # we assume that file is executable
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    projects_dir = testvars['takel_ship_compose_projects_dir']
    copy_image = testvars['takel_ship_compose_copy_image']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        if project['name'] == 'registry':
            continue

        file = host.file(
            f"{home_dir}/{dist_dir}/"
            f"{compose_dir}/{projects_dir}/"
            f"{project['name']}/{copy_image}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_projects_run_docker_files(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    # we assume that file is executable
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    projects_dir = testvars['takel_ship_compose_projects_dir']
    run_docker = testvars['takel_ship_compose_run_docker']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        file = host.file(
            f"{home_dir}/{dist_dir}/"
            f"{compose_dir}/{projects_dir}/"
            f"{project['name']}/{run_docker}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_projects_run_podman_files(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    # we assume that file is executable
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    projects_dir = testvars['takel_ship_compose_projects_dir']
    run_podman = testvars['takel_ship_compose_run_podman']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        file = host.file(
            f"{home_dir}/{dist_dir}/"
            f"{compose_dir}/{projects_dir}/"
            f"{project['name']}/{run_podman}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode


def test_takel_ship_compose_projects_copy_project_files(
        host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    # we assume that file is executable
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    copy_project = testvars['takel_ship_compose_copy_project']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        file = host.file(
            f"{home_dir}/{dist_dir}/"
            f"{copy_project}.{project['name']}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode
