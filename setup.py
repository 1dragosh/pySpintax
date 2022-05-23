import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pySpintax",
    version="2.0",
    author="1dragosh",
    author_email="contact@1dragosh.me",
    description="Simple Spintax Spinner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1dragosh/pySpintax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)