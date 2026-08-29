from setuptools import setup
import py2exe

setup(
    name="SnakeGame",
    version="1.0.0",
    description="A Classic Snake Game",
    author="chanthanhvu2014-cpu",
    console=[{
        'script': 'snake_game.py',
        'dest_base': 'SnakeGame'
    }],
    options={
        'py2exe': {
            'packages': ['pygame'],
            'includes': ['pygame'],
            'bundle_files': 1,
            'compressed': True,
        }
    },
    zipfile=None,
)