import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_podman_install_packages_installed(host, testvars):
    takel_docker_deb_install_packages = \
        testvars['takel_ship_forgejo_deb_install_packages']

    for package in takel_docker_deb_install_packages:
        deb = host.package(package)

        assert deb.is_installed


def test_takel_ship_podman_create_bat_symlink(host):
    tea = host.file('/usr/local/bin/tea')

    assert tea.exists
    assert tea.is_symlink
    assert tea.linked_to == '/usr/bin/tea-cli'
    assert tea.user == 'root'
    assert tea.group == 'root'
    assert tea.mode == 0o755
