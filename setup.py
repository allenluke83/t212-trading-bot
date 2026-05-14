from setuptools import setup

setup(
    name="trading-bot",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "yfinance",
        "pandas",
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'trade-run = main:main_function_name', 
        ],
    },
)