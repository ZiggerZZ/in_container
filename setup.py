import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="in_container",
    version="0.0.1",
    author="Zigfrid Zvezdin",
    author_email="ziggerzz@gmail.com",
    description="Check if running inside a Docker container",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZiggerZZ/in_container",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)