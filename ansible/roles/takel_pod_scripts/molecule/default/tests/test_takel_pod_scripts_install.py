import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_pod_scripts_install_files(
        host, testvars):
    scripts = testvars['takel_pod_scripts_scripts']
    for script in scripts:
        dir = testvars['takel_pod_scripts_dir']
        user = 'root'
        group = 'root'
        mode = 0o755
        if 'path' in script:
            dir = script['path']
        if 'owner' in script:
            user = script['owner']
        if 'group' in script:
            group = script['group']
        if 'mode' in script:
            if script['mode'] == '0755':
                mode = 0o755
            elif script['mode'] == '0644':
                mode = 0o644
        file = host.file(f"{dir}/{script['name']}")

        assert file.exists
        assert file.is_file
        assert file.user == user
        assert file.group == group
        assert file.mode == mode
