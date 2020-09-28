import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="touchportal-api-ff-sclark",
    version="1.0.0",
    author="Shane Clark",
    author_email="contact@sclark.ml",
    description="A client to connect to Touch Portal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FrostfireMedia/touchportal-python-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyee==8.0.1",
        "simple-socket==0.0.5"
    ],
    python_requires=">=3.6"
)
