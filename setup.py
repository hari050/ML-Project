from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:  ## This function will return all the requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]  ## This line \n is used to treat as blank spaces

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
name='ML project', ## we can give name of the project 
version='0.0.1', ## whenever new version comes we can change according to it
author='Narahari',
author_email='narahari421@gmail.com',
packages=find_packages(), ## using the module which imported and one of the finest methods
install_requires=get_requirements('requirements.txt') ## we have to mention what are the required packages we use where it automatically installs



)