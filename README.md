# BBGenerator
Here is a example project to show how it is possible to create a simple CI/CD pipeline and deploy a Flask application on Gandi.net simple hosting thanks to Github actions.
Live demo [_here_](https://bibigen.bougetb.fr/).

## Table of Contents
- [BBGenerator](#bbgenerator)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Setup](#setup)
  - [Project Status](#project-status)
  - [Contact](#contact)
  - [License](#license)



## General Information
This project is a Flask application that just display a random generated (bullshit) baseline for your startup.
Actually it only intends to details how it is possible to configure a CI/CD pipeline for an application deployed and hosted on a [Gandi Simple Hosting](https://www.gandi.net/en/simple-hosting).

## Technologies Used
- Python 3.8


## Features
No really useful feature. Just a random bullshit sentence generator :-)

## Setup
It is quite simple:
* Create a Python Gandi Simple hosting
* Create a website on your simple where you want to deploy the application. Ensure the Record DNS are Ok
* Clone this repository
* Create a SSH keypair, store the PV Key in your and upload the public key on your Gandi Simple Hosting instance.
* in the Github Action Workflown, add the known_host information to your repository secret, and the other required informations related to your instance (id, git address)
* build your project in order to launch the CI/CD workflow

## Project Status
Project is: _complete_ 

## Contact
Feel free to contact me if you have any question.

## License
The code in this project is licensed under MIT license.
