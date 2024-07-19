from setuptools import setup, find_packages

setup(
    name='wcpl',
    version='1.0.2',
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
        'qiskit==0.39.0',         # For quantum computing
        'pygame==2.1.3',          # For game development
        'pydub==0.25.1',          # For music creation
        'midiutil==1.2.0',        # For MIDI music creation
        'manim==0.15.1',          # For animated movie creation
    ],
    author='Joey Soprano 420',
    description='WordCom-ProLang (WCPL) Programming Language',
    long_description=(
        'WordCom-ProLang (WCPL) is a cutting-edge programming language combining features from Comrite and WordMaze, '
        'designed to handle a wide range of applications including quantum computing, 3D game design, music creation, '
        'and animated movie production. This language features an advanced interpreter capable of executing complex tasks '
        'with high efficiency and versatility.'
    ),
    long_description_content_type='text/plain',
    url='https://github.com/joeysoprano420/wcpl',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    license='Modified QSRLC License',
)
