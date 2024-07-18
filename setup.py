from setuptools import setup, find_packages

setup(
    name='wcpl',
    version='1.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wcpl=wcpl.__main__:main',
        ],
    },
    install_requires=[
        'requests==2.26.0',
        'numpy==1.21.1',
        'matplotlib==3.4.3',
    ],
    author='Joey Soprano 420',
    description='WordCom-ProLang (WCPL) Programming Language',
    long_description='A programming language that combines features from Comrite and WordMaze.',
    long_description_content_type='text/plain',
    url='https://github.com/joeysoprano420/wcpl',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    license='Modified QSRLC License',
)
