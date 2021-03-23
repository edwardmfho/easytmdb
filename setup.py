import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easytmdb",
    version="0.0.1",
    author="Edward M.F. Ho",
    author_email="edwardho@hey.com",
    packages=["easytmdb"],
    description="A Python Package to retrieve data from The Movie Database (TMDB).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edwardmfho/easytmdb",
    license='GPT',
    python_requires='>=3.6',
    install_requires=[
         "requests>=2.22.0",
    ]
)