import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="goneirossPy",
    version="0.0.2",
    author="Goneiross",
    author_email="guillaume.julien.pellerin@goneiross.org",
    description="Some usefull tools used in my projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Goneiross/gonPython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)