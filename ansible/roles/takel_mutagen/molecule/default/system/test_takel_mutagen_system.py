import takeltest
import re
import requests

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_mutagen_system_mutagen_version(host, testvars):
    takel_mutagen_mutagen_version = \
        str(testvars['takel_mutagen_mutagen_version'])
    mutagen_version_output = \
        host.check_output('mutagen version')
    mutagen_version_search = re.search(
        r'(\d{1,2}\.\d{1,2}\.\d{0,2})', mutagen_version_output)

    assert mutagen_version_search is not None, 'Unable to get mutagen version'

    if takel_mutagen_mutagen_version == 'latest':
        url = "https://api.github.com/repos/mutagen-io/mutagen/releases/latest"
        response = requests.get(url)
        mutagen_version = response.json()["tag_name"]
    assert f"v{mutagen_version_search.group(1)}" == mutagen_version, \
        'Unable to get mutagen version'
