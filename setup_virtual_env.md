# Python Virtual Environment Setup

## Prerequisite
 Python should be installed.

## Windows

1. Creation : ```python -m venv projectenv ```
py -3.10 -m venv projectenv
2. Activate :```.\projectenv\Scripts\activate```
3. Deactivate: ```deactivate```

## Linux

1. Creation : ```python3 -m venv projectenv ```
2. Activate : ```source /bin/activate```
3. Deactivate: ```deactivate```

## Package installation

```pip install requests
pip install numpy playsound gtts
pip install plotly
python -m pip install pillow
pip install tensorflow
```


## Requirements

1. Freeze the requirements : ```pip freeze > requirements.txt```
2. Installing the requirements: ```pip install requirements.txt```