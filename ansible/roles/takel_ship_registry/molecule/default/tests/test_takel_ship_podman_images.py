import takeltest
import json

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ship_registry_images_downloaded(host, testvars):
    takel_images = testvars['takel_ship_registry_takelship_images']
    images = [f"{takel_image['name']}:{takel_image['tag']}"
              for takel_image in takel_images]
    cmd = testvars['takel_ship_scripts_script_pod']['name']
    cmd = f"{cmd} podman images --format=json"
    sys_images = json.loads(host.check_output(cmd))
    podman_images = [sys_image['Names'][0] for sys_image in sys_images]

    assert images.sort() == podman_images.sort()
