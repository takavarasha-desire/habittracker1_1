# Habit tracker app
## Introduction
Simple command line habit tracking app design project for the
course  DLBDSOOFPP01 through IU International University of
Applied Sciences.
The application allows a user to create habits which they would
like to track (see usage below). Once created, a scheduling function
in the habits class is called to calculate the next date that the
habit should be completed depending on the periodicity chosen.
Created habits are considered overdue when a period of 1 day
has lapsed after the next_run date for all periodic options.
The application also allows a user to analyse their habits through
the analyse subcommands. Some of the information that can be accessed
though these subcommands is the longest streak for each habit. Which
the largest number of consecutive completions for a particular habit.

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
* Getting habitid (to see all habits with their habitids)
```bash
cll analyse show
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
