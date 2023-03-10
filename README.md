# erpipc

#### Description

Using Python3 programming language, a Python library erpipc was developed to realize the calculation function of ionic conductivity of composite polymer solid electrolyte.

#### Software Architecture

（1） initial_structure

The module implements the function of initializing the composite polymer conductor structure, including the size of the model, the occupation of the inorganic phase, and the initial site state of the walkers.

（2） ions_jumping_process

This module implements the algorithm of how walkers choose to migrate.

（3） samples_to_generate

The module is used to record the information of each step of walkers migration, including time step and site coordinates.

（4） parameter_calculation

The module implements the ionic conductivity calculation algorithm, and solves the ionic conductivity according to the Nernst Einstein equation by recording enough walkers migration information.

####Required packages

python 3.7.4   pandas 1.3.2   pip 21.2.2   python-dateutil 2.8.2  pytz 2021.1  setuptool 57.4.0   six 1.16.0

####Instructions for use

The dependent packet information is stored in the requirements.txt file. 
 
Installation command :
``` shell
pip intall erpipc
```
