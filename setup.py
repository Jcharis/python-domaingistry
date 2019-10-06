from setuptools import setup,find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="domaingistry",
    version="0.0.2",
    description="A Package For Generating Domain Names.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jcharis/python-domaingistry",
    author="Jesse E.Agbe(JCharis)",
    author_email="jcharistech@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click","click-didyoumean"],
    entry_points={
        "console_scripts": [
            "domain-gistry=domaingistry.cli:main",
        ]
    },
)
