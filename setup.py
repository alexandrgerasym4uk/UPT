from setuptools import setup, find_packages

setup(
    name="AI",  
    version="0.1.0", 
    packages=find_packages(), 
    install_requires=[
        "threading", 
    ],
    author="Alex Gerasymchuk",
    author_email="alexandrgerasym4uk@gmail.com",
    description="Пакет для генерації курсів і перевірки відповідей з використанням AI.",
    url="https://github.com/alexandrgerasym4uk/AI_funcs.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
