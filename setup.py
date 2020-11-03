import setuptools

setuptools.setup(
    name="streamlit-scatterplot-selection",
    version="0.0.1",
    author="Fanilo ANDRIANASOLO",
    author_email="andfanilo@gmail.com",
    description="Code companion for Dev.to article Streamlit components - Scatterplot with selection using Plotly.js ",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/andfanilo/streamlit-scatterplot-selection",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "plotly >= 4.9"
    ],
)
