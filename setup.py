from setuptools import setup, find_packages
from ez_setup import use_setuptools
use_setuptools()


setup(
    name='FacebookPostPlugin',
    version="1.0",
    description="This is a plugin to post on facebook",
    author="Ruyther Costa",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["CMS>=1.0"],
    entry_points={
        'plugin': [
            'post_plugin = facebook_post_plugin.plugin:post_on_facebook',
        ],
    },
)
