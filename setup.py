import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Ollivanders",
    version="0.0.1",
    author="danielsobrino",
    author_email="dsobrino343@gmail.com",
    description="REST API with flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanielSobBorja/Flask-ollivanders/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires=">=3.8",
    install_requires=[
        "aniso8601==9.0.1",
        "atomicwrites==1.4.0",
        "attrs==21.4.0",
        "click==8.1.3",
        "colorama==0.4.5",
        "distlib==0.3.4",
        "filelock==3.7.1",
        "Flask==2.1.2",
        "Flask-RESTful==0.3.9",
        "importlib-metadata==4.11.4",
        "iniconfig==1.1.1",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.1",
        "packaging==21.3",
        "platformdirs==2.5.2",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyparsing==3.0.9",
        "pytest==7.1.2",
        "pytz==2022.1",
        "six==1.16.0",
        "toml==0.10.2",
        "tomli==2.0.1",
        "tox==3.25.0",
        "virtualenv==20.14.1",
        "Werkzeug==2.1.2",
        "zipp==3.8.0"
    ],
)
