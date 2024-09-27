import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_services_system_dry_run_compose(host, testvars):
    home_dir = testvars['takel_ship_services_home_dir']
    data_dir = testvars['takel_ship_services_dist_dir']
    compose_dir = testvars['takel_ship_services_compose_dir']
    services = testvars['takel_ship_services_services']
    cmd = testvars['takel_ship_scripts_script_cmd']['name']
    for service in services:
        service_dir = (f"{home_dir}/{data_dir}/"
                       f"{compose_dir}/{service['name']}")
        podup = (f"{cmd} --workdir {service_dir} "
                 f"podman compose --dry-run up")
        print(podup)
        exit_status = host.run_test(podup).exit_status

        assert 0 == exit_status
