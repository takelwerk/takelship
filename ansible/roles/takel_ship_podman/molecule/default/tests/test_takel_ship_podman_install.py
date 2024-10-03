import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_podman_install_packages_installed(host, testvars):
    takel_docker_deb_install_packages = \
        testvars['takel_ship_podman_deb_install_packages']

    for package in takel_docker_deb_install_packages:
        deb = host.package(package)

        assert deb.is_installed

def test_takel_ship_podman_create_bat_symlink(host):
    bat = host.file('/usr/local/bin/bat')

    assert bat.exists
    assert bat.is_symlink
    assert bat.linked_to == '/usr/bin/batcat'
    assert bat.user == 'root'
    assert bat.group == 'root'
    assert bat.mode == 0o755
