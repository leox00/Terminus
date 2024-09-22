from setuptools import setup, Extension

module = Extension('terminus.renderer', sources=['src/c/renderer.c'])

setup(
    name='terminus',
    version='0.1',
    description='Terminus Terminal Emulator',
    ext_modules=[module],
    packages=['terminus'],
)