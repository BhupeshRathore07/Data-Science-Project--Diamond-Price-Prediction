from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def getRequirements(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as f:
        requirements=f.readlines()

        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='DiamondPicePredictionProject',
    version='0.0.1',
    author='Bhupesh',
    author_email='bsinghrathore32@gmail.com',
    install_requires=getRequirements('requirements.txt'),
    packages=find_packages()

)