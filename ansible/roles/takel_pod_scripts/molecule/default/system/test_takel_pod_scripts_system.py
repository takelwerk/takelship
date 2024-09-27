import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_pod_scripts_system_cmd(host, testvars):
    owner = testvars['takel_pod_services_user']['owner']
    cmd = testvars['takel_pod_scripts_script_cmd']['name']
    command = f"{cmd} whoami"
    user = host.check_output(command)

    assert owner == user


def test_takel_pod_scripts_system_commands(host, testvars):
    command = 'commands'
    cmd = testvars['takel_pod_scripts_script_cmd']['name']
    output = host.check_output(command)

    assert cmd in output
