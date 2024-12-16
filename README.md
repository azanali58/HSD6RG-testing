## Behavior Testing w/ Python, Selenium and Behave

This repository contains the code for a test automation project written in Python. The project uses the `behave` library for behavior driven testing and `selenium` for interacting with web elements.

The project uses the [HSD6RG](https://tutorialsninja.com/demo/) website for automation.

## Usage
In order to run the features, first of all you have to clone the repository or download it in a `.zip` file. 

### Setting up `venv`
The project uses `behave` and `selenium` libraries so you have to set them up before running the features. Open a terminal and write the following commands.
```
python -m venv venv
venv\Scripts\activate
```

After that, install the libraries using the following command.
```
pip install -r requirements.txt
```

After that, navigate to the project directory and enter the following command to run all the features.
```
behave features
```
