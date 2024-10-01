import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_compose_compose_dirs_service_dir(host, testvars):
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


def test_takel_ship_compose_compose_dirs_projects_dir(host, testvars):
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


def test_takel_ship_compose_compose_dirs_service_dirs(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        service_dir = (f"{home_dir}/{data_dir}/"
                       f"{compose_dir}/{service['name']}")
        dir = host.file(service_dir)

        assert dir.exists
        assert dir.is_directory
        assert dir.user == user
        assert dir.group == group
        assert dir.mode == mode


def test_takel_ship_compose_compose_dirs_volumes(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services = testvars['takel_ship_compose_services']
    for service in services:
        if 'volumes' not in service:
            continue

        for volume in service['volumes']:
            volume_dir = \
                (f"{home_dir}/{data_dir}/{compose_dir}/"
                 f"{service['name']}/{volume['name']}")
            dir = host.file(volume_dir)

            assert dir.exists
            assert dir.is_directory
            assert dir.user == user
            assert dir.group == group
            assert dir.mode == mode
