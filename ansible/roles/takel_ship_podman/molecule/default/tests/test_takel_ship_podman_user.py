import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_podman_user_bash_aliases_copied(host, testvars):
    podman = testvars['takel_ship_podman_user']['owner']
    bashrc_d = f"/home/{podman}/.bashrc.d"
    dir = host.file(bashrc_d)

    assert dir.exists


def test_takel_ship_podman_user_bash_logout_removed(host, testvars):
    podman = testvars['takel_ship_podman_user']['owner']
    bash_logout = f"/home/{podman}/.bash_logout"
    file = host.file(bash_logout)

    assert not file.exists


def test_takel_ship_podman_user_run_dir_added(host, testvars):
    user = testvars['takel_ship_podman_user']['owner']
    group = testvars['takel_ship_podman_user']['group']
    mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
    home_dir = testvars['takel_ship_compose_home_dir']
    run_dir = f"{home_dir}/.run"
    dir = host.file(run_dir)

    assert dir.exists
    assert dir.is_directory
    assert dir.user == user
    assert dir.group == group
    assert dir.mode == mode
