from setuptools import find_packages, setup

setup(
    name = "mcq_generator",
    version = "0.0.1",
    author = "Manoj Baniya",
    author_email = "manojbaniya727@gmail.com",
    description = "A simple MCQ generator",
    packages = find_packages(),
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"]
)