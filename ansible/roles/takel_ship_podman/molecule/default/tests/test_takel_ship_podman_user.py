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
