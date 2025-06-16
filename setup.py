from setuptools import setup, find_packages

setup(
    name="tourism_backend",
    version="1.0.0",
    author="Your Name",
    description="Backend Algorithm for Tourism App",
    python_requires='==3.10.0',
    packages=find_packages(where='Service'),
    package_dir={'': 'Service'},
    install_requires=[
        'langchain_core==0.3.61',
        'langchain_ollama==0.3.3',
        'uvicorn==0.34.2',
        'fastapi==0.115.12',
        'funasr==1.2.6',
        'pyaudio==0.2.14',
        'transformers==4.52.3',
        'python-multipart==0.0.20'
    ],
    entry_points={
        'console_scripts': [
            'tourism-backend=main:main',
        ],
    },
)