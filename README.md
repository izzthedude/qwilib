# Qwilib

## Description

Qwilib is an opinionated (Python) Qt6 widget library based on PySide6 that aims to minimise the amount of setting up
needed to get a GUI application up and running. It does this by predefining many widgets and layouts in an opinionated
way that can be used in development immediately with minimal setup.

This project started off as a *'copy-paste from that project to this one and then back'* kinda thing and became
increasingly difficult to maintain once it started growing in size. So I decided to extract it as its own little project
with its own repo.

### Current Progress (v0.1.1):

- [PR#2](https://github.com/izzthedude/qwilib/pull/2) Restructured source files into sub-packages appropriately, used
  qresource for Qwilib resources and cleaned up some unused enums.

## Installation

### Environment

This project is developed and tested on:

- Windows 10
- Python 3.10+

No tests have been made in other environments, so issues will very likely occur if you choose to do so.

### Install from Git

Currently, Qwilib can only be installed from git with the following command:  
`pip install git+https://github.com/izzthedude/qwilib.git@main`

## Plans

1. Refactor project for more general-use.
2. Documentation/widget gallery for browsing Qwilib widgets.
3. Publish to PyPi

## License

Qwilib is licensed under the MIT license. The icons used in Qwilib are from Google Material Symbols, which are available
under the Apache License Version 2.0.
