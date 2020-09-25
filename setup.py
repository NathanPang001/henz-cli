from setuptools import setup
setup(
    name = 'henzcli',
    version = '0.1.0',
    packages = ['henzcli'],
    entry_points = {
        'console_scripts': [
            'henzcli = henzcli.__main__:main'
        ]
    })