import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = "Practice-Project"
AUTHOR_USERNAME = "Mayuresh999"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mayuresh.madiwale@yahoo.com"


setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author= AUTHOR_USERNAME,
    author_email= AUTHOR_EMAIL,
    description= 'This project is a practice project with ML and MLOPS tools.',
    long_description= long_description,
    long_description_content= "text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls= {"cnnClassifier" : f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"},
    package_dir= {"" : "src"},
    packages=setuptools.find_packages(where="src"),
)