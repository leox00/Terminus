from setuptools import setup, Extension

# Define the renderer module
renderer_module = Extension('terminus.renderer', sources=['src/c/renderer.c'])

# Define the pty_handler module for Linux
pty_handler_module = Extension('terminus.pty_handler', sources=['src/c/pty_handler.c'])

# Setup configuration
setup(
    name='terminus',
    version='0.1',
    description='Terminus Terminal Emulator',
    ext_modules=[renderer_module, pty_handler_module],
    packages=['terminus'],
    package_dir={'terminus': ''},
    ext_package='terminus'
)