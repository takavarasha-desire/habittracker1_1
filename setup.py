from setuptools import setup, find_packages

setup(
    name="habit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Click',
        'sqlalchemy',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'cll = habit.cll:startt',
        ],
    },
)
