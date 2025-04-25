from setuptools import setup, find_packages

setup(
    name='pytest-plugin-project',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'pytest11': [
            'pytest_plugin = plugin.plugin',
        ],
    },
)
