# localtomatoes

[![Build Status](https://secure.travis-ci.org/audreyr/localtomatoes.png)](http://travis-ci.org/audreyr/localtomatoes)
[![Stories in Ready](https://badge.waffle.io/audreyr/localtomatoes.png?label=ready)](https://waffle.io/audreyr/localtomatoes) [![pypi version](https://badge.fury.io/py/localtomatoes.png)](http://badge.fury.io/py/localtomatoes)
[![# of downloads](https://pypip.in/d/localtomatoes/badge.png)](https://crate.io/packages/localtomatoes?version=latest)
[![code coverage](https://coveralls.io/repos/audreyr/localtomatoes/badge.png?branch=master)](https://coveralls.io/r/audreyr/localtomatoes?branch=master)

## Overview

LocalTomatoes displays the Rotten Tomatoes ratings for the movies at your local theater.

* features
* and stuff 

## Usage

Install `localtomatoes`:

    pip install localtomatoes

## Documentation

[API Documentation](http://localtomatoes.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 localtomatoes tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir