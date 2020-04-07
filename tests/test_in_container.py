import in_container


def test_in_container_on_host():
    assert in_container.in_container() is False
