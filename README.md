![Alt text](img/circle-logo-horizontal-black-302x63-d4d5baa.png?raw=true)

![Bintray](https://img.shields.io/badge/Circle%20CI-Continuous%20Integration-brightgreen)

# Continuous Integration

An intro to using Circle CI for Continous Integration in Python projects.

More info on Circle CI [here](https://circleci.com/enterprise-trial-install/?utm_source=gb&utm_medium=SEM&utm_campaign=SEM-gb-200-Eng-ni&utm_content=SEM-gb-200-Eng-ni-CircleCI&gclid=Cj0KCQjww_f2BRC-ARIsAP3zarGT2Uz8Ug8DF7MWCAq_FCXkD8at53KYsl60sfFq00yvlNJdjJ2jc78aApMQEALw_wcB)

## Instructions for use

Create an account at Circle CI [here](https://circleci.com/enterprise-trial-install/?utm_source=gb&utm_medium=SEM&utm_campaign=SEM-gb-200-Eng-ni&utm_content=SEM-gb-200-Eng-ni-CircleCI&gclid=Cj0KCQjww_f2BRC-ARIsAP3zarGT2Uz8Ug8DF7MWCAq_FCXkD8at53KYsl60sfFq00yvlNJdjJ2jc78aApMQEALw_wcB)

Create a new repo at GitHub

Go to Circle CI and link repo

The pipeline does the following:
  1. Checks out the repository
  2. Installs dependencies in a virtual environment
  3. Runs the linter (flake8) and tests (pytest) whilst inside the virtual environment

Check if the build fails/succeeds over at Circle CI - fix/don't fix!
