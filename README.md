# Habit tracker app
## Introduction
Simple command line habit tracking app design project for the
course  DLBDSOOFPP01 through IU International University of
Applied Sciences.
## Installation
* clone this repo to your local folder
```bash
git clone https://github.com/takavarasha-desire/habittracker1_1
cd habittracker1_1
```
* make your virtualenv
```bash
virtualenv env
```
* and activate it

on Windows:
```bash
env/scripts/activate
```
on macOS and Linux
```bash
source env/Scripts/activate
```
* install package 
```bash
pip install -r requirements.txt
```
* Done!

## Usage
habit entry point (Terminal command)
``` bash
cll
```
Getting help
```bash
cll --help
```
Creating a new habit
* Periodicity can be Daily, Weekly, Monthly, or Annually (case-sensitive)
```bash
cll create <activity> <periodicity>
```
Completing a habit
```bash
cll complete <habitid>
```
Deleting a habit
```bash
cll delete <habitid>
```
Habit Analysis entry point
```bash
cll analyse
```
Analysing habits
```bash
cll analyse <subcommand>
```
## Tests
```bash
pytest .
```
