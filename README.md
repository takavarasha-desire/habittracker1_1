# Habit tracker app
## Introduction
Simple command line habit tracking app
## Installation
* clone this repo to your local folder
```bash
git clone https://github.com/takavarasha-desire/habittracker1
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
pip install .
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
