from setuptools import setup, find_packages
from typing import List



PROJECT_NAME = "Modular Machine Learning"
VERSION = "0.01"
DESCRIPTION = "Machine Learning Project In Modular Coding"
AUTHOR_NAME = "aman-srma"
AUTHOR_EMAIL = "aaa.aaa@gmail.com"


REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHON_E_DOT = "-e ."


def get_requirements_list()->List:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHON_E_DOT in requirement_list:
            requirement_list.remove(HYPHON_E_DOT)

        return requirement_list




setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements_list()
     )