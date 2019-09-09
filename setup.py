from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="domaingistry",
    version="0.0.1",
    description="A Package For Generating Domain Names.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jcharis/DomainGistry_CLI",
    author="Jesse E.Agbe(JCharis)",
    author_email="jcharistech@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["domain-gistry"],
    include_package_data=True,
    install_requires=["json"],
    entry_points={
        "console_scripts": [
            "domaingistry=domaingistry.domaingistry:main",
        ]
    },
)
