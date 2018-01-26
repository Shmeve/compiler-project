# COMP 442 - Compiler Design

Steve Ferreira, 27477546  
Section: Winter 2018 - NN

## Prerequisites
- Python 3
- pip

## Setup
1. `cd` to repository
2. `pip install virtualenv`
3. `virtualenv venv`
4. `source venv/bin/activate`
5.  `pip install -r requirements.txt`
6.  `deactivate`

## Running the Compiler
`python main.py`

## Testing Project
This projects test suit can be run using [nose (installed via requirements.txt)](http://nose.readthedocs.io/en/latest/)
1. `cd` to repository
2. `source venv/bin/activate`
3. `nosetests tests`