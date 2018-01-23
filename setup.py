from setuptools import setup

setup(
    name='click_config_file',
    author='Philipp Hack',
    author_email='philipp.hack@gmail.com',
    url='http://github.com/phha/click_config_file',
    version='0.4.0',
    license='MIT',
    description='Configuration file support for click applications.',
    long_description="""Easily add configuration file support to your click
    application by adding a single no-arguments decorator.""",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['click_config_file'],
    install_requires=['click >= 6.7', 'configobj >= 5.0.6'],
)
