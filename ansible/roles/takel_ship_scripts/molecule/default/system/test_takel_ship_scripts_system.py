import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_scripts_system_cmd(host, testvars):
    owner = testvars['takel_ship_podman_user']['owner']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    command = f"{cmd} whoami"
    user = host.check_output(command)

    assert owner == user


def test_takel_ship_scripts_system_commands(host, testvars):
    cli = testvars['takel_ship_scripts_script_cli']['name']
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    output = host.check_output(cli)

    assert cmd in output
