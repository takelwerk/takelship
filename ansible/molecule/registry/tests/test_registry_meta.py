import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_registry_meta_env_exists(image_meta_data):
    assert image_meta_data['Config']['Env'] is not None


def test_registry_meta_env_version(testvars, image_meta_data):
    version = testvars['project']['version']
    envvar = f"VERSION={version}"

    assert envvar in image_meta_data['Config']['Env']


def test_registry_meta_entrypoint(testvars, image_meta_data):
    expected = ['/entrypoint']

    assert expected == image_meta_data['Config']['Entrypoint']


def test_registry_meta_work_dir(image_meta_data):
    assert '/' == image_meta_data['Config']['WorkingDir']
