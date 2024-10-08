import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_scripts_install_files(
        host, testvars):
    scripts = testvars['takel_ship_scripts_scripts']
    for script in scripts:
        if 'template' not in script:
            continue

        dir = testvars['takel_ship_scripts_dir']
        user = testvars['takel_ship_scripts_root']['owner']
        group = testvars['takel_ship_scripts_root']['group']
        # we assume that file is executable
        mode = int(testvars['takel_ship_podman_user']['mode']['dir'], 8)
        if 'path' in script:
            dir = script['path']
        if 'owner' in script:
            user = script['owner']
        if 'group' in script:
            group = script['group']
        if 'mode' in script:
            mode = int(script['mode'], 8)

        file = host.file(f"{dir}/{script['name']}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode
