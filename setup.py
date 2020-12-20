import setuptools

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except UnicodeDecodeError:
    with open("README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

with open("idm_lp/const.py") as f:
    exec(f.read())

setuptools.setup(
    name="idm_lp",
    version=locals()["__version__"],
    author=locals()["__author__"],
    description="IDM LP module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/lordralinc/idm_lp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["vkbottle", "tortoise-orm", "requests", "aiomysql", "aiohttp"],
    include_package_data=True,
)
