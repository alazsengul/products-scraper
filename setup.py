from setuptools import setup, find_packages

setup(
    name="PRODUCTS-SCRAPER",
    packages=find_packages(include=["src"]),
    version="0.1.1",
    author="Alaz Sengul",
    author_email="as5456@columbia.edu",
    description="Python API that scrapes products across a variety of retail sites.",
    url="https://github.com/alazsengul/products-scraper",
    project_urls={
        "Read the Docs": "https://products-scraper.readthedocs.io/en/latest",
    },
    license="MIT",
    install_requires=[""],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)