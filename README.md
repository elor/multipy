# Multipy

*Multipy*: Multiple Python modules in the same git repository, which can be installed selectively or all together.

## What?

A server and client combination, sharing common code between them.

## Why?

Mainly consistency through shared code, don't-repeat-yourself, and a bit of separation of concerns.
Testability, too.

Also, I wanted to see how well it works

## How?

It's mainly pyproject files referencing themselves

`./pyproject.toml`: allows to install `multipy[server]` or `multipy[client]` selectively, via extras.

`./multipy_client/pyproject.toml` and `./multipy_server/pyproject.toml`: reference `./multipy_common` as a dependency

## Installation

Only the server:

    pip install git+https://github.com/elor/multipy#egg=multipy[server]
    - or locally -
    pip install /path/to/multipy[server]

Only the client:

    pip install git+https://github.com/elor/multipy#egg=multipy[client]

Both:

    pip install git+https://github.com/elor/multipy#egg=multipy[all]
    - or -
    pip install git+https://github.com/elor/multipy#egg=multipy[all]

## Usage

Start the server:

    multipy_server

Start the client:

    multipy_client

