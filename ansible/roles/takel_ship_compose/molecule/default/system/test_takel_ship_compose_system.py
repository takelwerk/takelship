import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_compose_system_dry_run_compose(host, testvars):
    home_dir = testvars['takel_ship_compose_home_dir']
    data_dir = testvars['takel_ship_compose_dist_dir']
    compose_dir = testvars['takel_ship_compose_compose_dir']
    services_dir = testvars['takel_ship_compose_services_dir']
    services = testvars['takel_ship_compose_services']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    for service in services:
        service_dir = (f"{home_dir}/{data_dir}/"
                       f"{compose_dir}/{services_dir}/{service['name']}")
        podup = (f"{cmd} --workdir {service_dir} "
                 f"podman compose --dry-run up")
        print(podup)
        exit_status = host.run_test(podup).exit_status

        assert 0 == exit_status
