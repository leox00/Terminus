from setuptools import setup, Extension
import platform
import os

# Define the renderer module
renderer_module = Extension('terminus.renderer', sources=['src/c/renderer.c'])

# Define the pty_handler module based on the platform
if platform.system() == 'Windows':
    winpty_lib_dir = os.path.join('libs', 'winpty')
    winpty_include_dir = os.path.join(winpty_lib_dir, 'include')

    pty_handler_module = Extension(
        'terminus.pty_handler',
        sources=['src/c/pty_handler_win.c'],
        include_dirs=[winpty_include_dir],
        library_dirs=[winpty_lib_dir],
        libraries=['winpty'],
        extra_compile_args=['/DWINPTY_EXPORTS'],
        extra_link_args=[os.path.join(winpty_lib_dir, 'winpty.lib')]
    )
else:
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