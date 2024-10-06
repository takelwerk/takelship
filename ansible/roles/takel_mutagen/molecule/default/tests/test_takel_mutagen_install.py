import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_mutagen_install_packages_installed(host, testvars):
    takel_gpg_install_packages = \
        testvars['takel_mutagen_deb_install_packages']

    for package in takel_gpg_install_packages:
        rpm = host.package(package)

        assert rpm.is_installed


def test_takel_mutagen_install_mutagen_installed(host, testvars):
    mutagen_bin = f"{testvars['takel_mutagen_bin_path']}/mutagen"
    file = host.file(mutagen_bin)

    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o755


def test_takel_mutagen_install_mutagen_agents_installed(host, testvars):
    mutagen_bin = f"{testvars['takel_mutagen_bin_path']}/mutagen-agents.tar.gz"
    file = host.file(mutagen_bin)

    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o644
