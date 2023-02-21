# Mixed solid electrolyte

#### Introduction
According to the percolation conduction characteristics of composite polymer solid electrolyte, a program for calculating the ionic conductivity of composite polymer solid electrolyte was developed based on the random resistance model and effective medium theory.

#### Software Architecture

1. fike_hand.py
   File processing scripts

2. initial_structure_new.py
   Composite conductor structure initialization

3. ions_jumping_process_new1.py
   walkers select the direction to migrate and complete enough migration steps

4. samples_to_generate.py
   Record the information of each step of walkers migration

5. parameter_calculation_v1.py
   According to the recorded location and time information, the ionic conductivity is calculated.

#### Required packages

python 3.7.4 ase 3.19.0 pymatgen 2020.12.31 pandas 1.3.1 numpy 1.21.1 PyQt5 5.15.6 numba 0.55.1

#### Instructions for use

1.  xxxx
2.  xxxx
3.  xxxx



