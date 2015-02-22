try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import logging
import os

import gnupg

from mrsmith.helpers import get_config


def get_secret_path(secret_name):
    config = get_config()
    path = config.get('Paths', 'secrets')
    secretsdir_path = os.path.abspath(os.path.expanduser(path))
    secretfile_path = os.path.join(secretsdir_path, secret_name)
    return secretfile_path


def get_secret(secret_name):
    config = get_config()
    gnupghome = config.get('GPG', 'gnupghome')
    try:
        gpgbinary = config.get('GPG', 'gpgbinary')
    except configparser.NoOptionError:
        logging.info("It seems you haven't gpgbinary in your config. "
                     "For some reasons mrsmith only works with GPG2 "
                     "and you better to set explicit path to it.")
        gpg = gnupg.GPG(gnupghome=gnupghome, use_agent=True)
    else:
        gpg = gnupg.GPG(gpgbinary=gpgbinary,
                        gnupghome=gnupghome,
                        use_agent=True)
    secretfile_path = get_secret_path(secret_name)
    secretfile = open(secretfile_path, 'rb')
    secret = gpg.decrypt_file(secretfile)
    secretfile.close()
    return str(secret)
