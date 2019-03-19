import setuptools

setuptools.setup(
    name='codex',
    version='0.1.0',
    packages=['codex'],
    include_package_data=True,
    install_requires=[
        'Flask==1.0.2',
        'Flask-Testing==0.7.1',
        'html5validator==0.3.1',
        'pycodestyle==2.4.0',
        'pydocstyle==3.0.0',
        'pylint==2.2.2',
        'pytest==4.1.1',
        'requests==2.21.0',
        'selenium==3.141.0',
        'sh==1.12.14',
    ],
)