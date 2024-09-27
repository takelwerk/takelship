import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_pod_services_compose_services_compose_files(
        host, testvars):
    user = testvars['takel_pod_services_user']['owner']
    group = testvars['takel_pod_services_user']['group']
    home_dir = testvars['takel_pod_services_home_dir']
    dist_dir = testvars['takel_pod_services_dist_dir']
    compose_dir = testvars['takel_pod_services_compose_dir']
    service_filename = testvars['takel_pod_services_service_filename']
    service_fileext = testvars['takel_pod_services_service_fileext']
    services = testvars['takel_pod_services_services']
    for service in services:
        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/"
            f"{service['name']}/{service_filename}.{service_fileext}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == 0o644


def test_takel_pod_services_compose_services_compose_include_files(
        host, testvars):
    user = testvars['takel_pod_services_user']['owner']
    group = testvars['takel_pod_services_user']['group']
    home_dir = testvars['takel_pod_services_home_dir']
    dist_dir = testvars['takel_pod_services_dist_dir']
    compose_dir = testvars['takel_pod_services_compose_dir']
    service_include_filename = (
        testvars)['takel_pod_services_service_include_filename']
    service_fileext = testvars['takel_pod_services_service_fileext']
    services = testvars['takel_pod_services_services']
    for service in services:
        file = host.file(
            f"{home_dir}/{dist_dir}/{compose_dir}/"
            f"{service['name']}/{service_include_filename}.{service_fileext}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == 0o644
