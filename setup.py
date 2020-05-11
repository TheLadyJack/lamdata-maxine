
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lamdata-pt5", # the name that you will install via pip
    version="1.3",
    author="Jackie Maxine Morey",
    author_email="maxine.e.morey@gmail.com",
    description="A lambda school project module",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/TheLadyJack/lamdata-maxine",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)