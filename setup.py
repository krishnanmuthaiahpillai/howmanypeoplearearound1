from setuptools import setup

setup(
    name='howmanypeoplearearound1',
    packages=['howmanypeoplearearound1'],
    version='0.0.1',
    description='A tshark wrapper to count the number of cellphones in the vicinity',
    author='krishnan',
    url='https://github.com/krishnanmuthaiahpillai/howmanypeoplearearound1',
    author_email='krishnanmuthaiahpillai@gmail.com',
    download_url='https://github.com/krishnanmuthaiahpillai/howmanypeoplearearound1/archive/v1.0.tar.gz',
    keywords=['tshark', 'wifi', 'location'],
    classifiers=[],
    install_requires=[
        "click",
        "netifaces",
        "pick",
    ],
    setup_requires=[],
    tests_require=[],
    entry_points={'console_scripts': [
        'howmanypeoplearearound1 = howmanypeoplearearound1.__main__:main',
    ], },
)
