import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_compose_compose_projects_compose_files(host, testvars):
    user = testvars['takel_ship_compose_user']['owner']
    group = testvars['takel_ship_compose_user']['group']
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    service_filename = testvars['takel_ship_compose_service_filename']
    service_fileext = testvars['takel_ship_compose_service_fileext']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/"
            f"{service_filename}-{project['name']}.{service_fileext}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == 0o644


def test_takel_ship_compose_compose_projects_bash_files(host, testvars):
    user = testvars['takel_ship_compose_user']['owner']
    group = testvars['takel_ship_compose_user']['group']
    home_dir = testvars['takel_ship_compose_home_dir']
    dist_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    projects = testvars['takel_ship_compose_projects']
    for project in projects:
        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/run.{project['name']}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == 0o755
