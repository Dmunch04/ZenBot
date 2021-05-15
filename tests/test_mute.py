from zenbot.models import Mute


def test_mute_expires_at_calculation():
    mute = Mute("12M", "id")
    print(str(mute.timestamp))
    print(str(mute.expires_at))
    assert mute.expires_at is not None
