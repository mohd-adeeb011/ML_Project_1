## With this file we will be able to built whole machine learning project as a project which can also be installed in other projects as well.
## And can also deploy in PypI universal package then andone can install it from there.


from setuptools import find_packages,setup
from typing import List

def get_requirements(file_url:str)->List[str]:
    '''
    this function will return the list of requirements'''

    requirements=[]
    HYPEN_E='-e .'
    with open(file_url) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    

setup(
    name='ML_Project_1',
    version='0.0.1',
    author="Mohd Adeeb",
    author_email='mohdadeeb110@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)