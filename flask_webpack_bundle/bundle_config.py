import os

from flask_unchained import AppConfig


class BaseConfig(AppConfig):
    WEBPACK_MANIFEST_PATH = os.path.join(
        AppConfig.STATIC_FOLDER, 'assets', 'manifest.json')


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    # use relative paths by default, ie, the same host as the backend
    WEBPACK_ASSETS_HOST = ''


class StagingConfig(ProdConfig):
    pass


class TestConfig(BaseConfig):
    pass
