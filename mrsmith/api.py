import os

import gnupg

from mrsmith.helpers import get_config


def get_secret(secret_name):
    config = get_config()
    path = config.get('Paths', 'secrets')
    secretsdir_path = os.path.abspath(os.path.expanduser(path))
    secretfile_path = os.path.join(secretsdir_path, secret_name)
    gpg = gnupg.GPG(gnupghome=config.get('GPG', 'gnupghome'), use_agent=True)

    secretfile = open(secretfile_path, 'rb')
    secret = gpg.decrypt_file(secretfile)
    secretfile.close()
    return str(secret)
