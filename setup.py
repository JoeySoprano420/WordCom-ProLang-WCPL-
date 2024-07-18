from setuptools import setup, find_packages

setup(
    name='wcpl',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wcpl=wcpl.__main__:main',
        ],
    },
    install_requires=[
        # List any dependencies here
    ],
    author='Your Name',
    author_email='your@email.com',
    description='WordCom-ProLang (WCPL) Programming Language',
    long_description='A programming language that combines features from Comrite and WordMaze.',
    long_description_content_type='text/plain',
    url='https://github.com/yourusername/wcpl',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
