from setuptools import setup

setup(
    name="yamlify",
    version="1.1.0",
    description="YAMLify is a versatile and user-friendly tool that facilitates seamless conversion between YAML and JSON data formats. It offers a comprehensive set of features that cater to diverse needs, making it an invaluable asset for developers, data analysts, and anyone working with these data formats.",
    long_description=open("README.md").read() + "\n\n" +
    open("CHANGELOG.txt").read(),
    url="https://github.com/aliftech/YAMLify",
    author="Wahyu Krisna Aji",
    author_email="wahyukrisnaaji32@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 — Production/Stable",
        "Intended Audience :: Education",
        "Operating System :: MacOS",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords="yamlify",
)
