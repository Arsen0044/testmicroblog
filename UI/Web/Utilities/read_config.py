import os
import configparser


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def set_env_config():
    abs_path = f'{ROOT_DIR}/configuration.ini'
    config = configparser.RawConfigParser()
    config.read(abs_path)
    return config


class ReadInfoConfig:

    def __init__(self):
        self.config = set_env_config()

    def get_base_url(self):
        return self.config.get('links', 'base_url')

    def get_logout_url(self):
        return self.config.get('links', 'logout_url')

    def get_user_name(self):
        return self.config.get('user_data', 'user_name')

    def get_password(self):
        return self.config.get('user_data', 'password')


class Constants:

    info_config = ReadInfoConfig()

    """Constants"""
    base_url = info_config.get_base_url()
    logout_url = info_config.get_logout_url()
    user_name = info_config.get_user_name()
    password = info_config.get_password()
