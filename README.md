# Photoluminescence Spectrum Analysis Tool

A program to assist in the analysis of photoluminescence spectrum

**Contributors**

Jose Felix and Alban Desoutter

**Description**

User must provide a '.txt'file containing the data of the photoluminescence spectrum. 
The program will prompt for the desired width of the wavelength windows, the minimum and maximum wavelengths that will be plotted. An option to show the normalized spectrum will also be given. Finally, the user will have the option to save the data to a new '.txt' file. 

**Python version**

Python 3.12.7

**Licence**

This file is under the Python Software Foundation License

**Context**

Diodes are essential components in any electronic circuit, more precisely, laser diode is a well known device used in a wide range of domains. One of the most common materials found in this diodes is Gallium Arsenide (GaAs), which emits light at approximately 850 nm. Using a spectrometer, the emission spectrum of this material can be captured. In order to study any emission spectrum, it is often necessary to focus the study on different wavelength windows as well as obtaining the information concerning the emission peaks.  
The file Spectre.txt in this repository contains a sample spectrum of this material. Any file used as input for this program should follow the same format as the sample file, specifically with wavelengths and intensities listed in separate columns, and with the measurements' descriptions placed on lines different from the data.

**General Operation of the Script**

This script is composed of three files. All three files must be present in the same folder, however the only file that has to be executed by the user is *main.sh* which will then use the python scripts *intensite* and *recherche_plot*. The program will then ask for certain information regarding the custom spectrum that will be plotted. Finally, the user will have the option to create a new *.txt* file that will contain the information of the different windows and/or the intensity spectrum in the specified range. These files will be created in the same folder where the *main.sh* script is located unless a file path is specified by the user. 
The program is also designed to help detect emission peaks at a given spectrum. It is important to know that the criteria that were used in the *recherche_pics* function in the *recherche_plot.py* script were designed for this particular spectrum. For different measurements, it might be needed to adjust these criteria depending on the expected length of the emission peaks. 

**Specifications**

The best detection threshold for the sample spectrum is around 0.06, but it may vary for different measurements.
All answers given by the user must be written as *'Y'* for yes or *'N'* for no. 
The files containing the data will be created in the same folder where the *main.sh* is located unless a specific file path is given by the user. 
