import os

import pytest

from utils.path_utils import get_root


@pytest.mark.sanity
@pytest.mark.dev
@pytest.mark.staging
def test_login(app):
    app.login_page.navigate().login_to_system(
        user_email=os.environ.get('USER_NAME'),
        user_pswd=os.environ.get('USER_PASSWORD')
    )

    user_name = app.login_page.account_item.get_account_name()
    assert user_name == os.environ.get('USER_NAME'), 'User name is incorrect'


@pytest.mark.sanity
@pytest.mark.dev
def test_login_fail(app):
    app.login_page.navigate().login_to_system(
        user_email=os.environ.get('USER_NAME'),
        user_pswd=os.environ.get('USER_PASSWORD')
    )

    assert 1 > 2


@pytest.mark.regression
@pytest.mark.dev
def test_upload_video(app):
    app.login_page.navigate().login_to_system(
        user_email=os.environ.get('USER_NAME'),
        user_pswd=os.environ.get('USER_PASSWORD')
    )

    app.home_page\
        .open_upload_video_modal()\
        .upload_video(f'{get_root()}/fixtures/SampleVideo_1280x720_1mb.mp4')\
        .close_modal()

