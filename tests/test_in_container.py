import in_container


def test_in_container_travis_build():
    assert in_container.in_container() is True
