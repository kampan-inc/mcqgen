from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="deepak yadav",
    email="deepakyadav@engineer.comn",
    install_requires=["openaia","langchain","PyPDF2","streamlit","python-dotenv"],
    packages= find_packages()
    )