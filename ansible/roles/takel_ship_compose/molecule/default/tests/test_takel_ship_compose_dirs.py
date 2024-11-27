import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_compose_compose_dir(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    dir = host.file(f"{home_dir}/{data_dir}/{compose_dir}")

    assert dir.exists
    assert dir.is_directory
    assert dir.user == user
    assert dir.group == group
    assert dir.mode == mode


def test_takel_ship_compose_services_dir(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    dir = host.file(f"{home_dir}/{data_dir}/{compose_dir}/{services_dir}")

    assert dir.exists
    assert dir.is_directory
    assert dir.user == user
    assert dir.group == group
    assert dir.mode == mode


def test_takel_ship_compose_base_projects_dir(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    projects_dir = testvars['takel_ship_compose_projects_dir']
    dir = host.file(f"{home_dir}/{data_dir}/{projects_dir}")

    assert dir.exists
    assert dir.is_directory
    assert dir.user == user
    assert dir.group == group
    assert dir.mode == mode


def test_takel_ship_compose_compose_projects_dir(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    projects_dir = testvars['takel_ship_compose_projects_dir']
    dir = host.file(f"{home_dir}/{data_dir}/{compose_dir}/{projects_dir}")

    assert dir.exists
    assert dir.is_directory
    assert dir.user == user
    assert dir.group == group
    assert dir.mode == mode


def test_takel_ship_compose_services_dirs(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        service_dir = (f"{home_dir}/{data_dir}/"
                       f"{compose_dir}/{services_dir}/{service['name']}")
        dir = host.file(service_dir)

        assert dir.exists
        assert dir.is_directory
        assert dir.user == user
        assert dir.group == group
        assert dir.mode == mode


def test_takel_ship_compose_preinstall_dirs(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    preinstall_dir = testvars['takel_ship_compose_preinstall_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        service_dir = (f"{home_dir}/{data_dir}/"
                       f"{compose_dir}/{services_dir}/"
                       f"{service['name']}/{preinstall_dir}")
        dir = host.file(service_dir)

        assert dir.exists
        assert dir.is_directory
        assert dir.user == user
        assert dir.group == group
        assert dir.mode == mode


def test_takel_ship_compose_postinstall_dirs(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    postinstall_dir = testvars['takel_ship_compose_postinstall_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        service_dir = (f"{home_dir}/{data_dir}/"
                       f"{compose_dir}/{services_dir}/"
                       f"{service['name']}/{postinstall_dir}")
        dir = host.file(service_dir)

        assert dir.exists
        assert dir.is_directory
        assert dir.user == user
        assert dir.group == group
        assert dir.mode == mode


def test_takel_ship_compose_projects_dirs(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    projects_dir = testvars['takel_ship_compose_projects_dir']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        project_dir = (f"{home_dir}/{data_dir}/"
                       f"{compose_dir}/{projects_dir}/{project['name']}")
        dir = host.file(project_dir)

        assert dir.exists
        assert dir.is_directory
        assert dir.user == user
        assert dir.group == group
        assert dir.mode == mode
