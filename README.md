# Pong Olympics

Pong Olympics is a Python-based spinoff of [Video Olympics](https://en.wikipedia.org/wiki/Video_Olympics) on the Atari 2600, with unique features and gameplay.

![pong-olympics](./docs/pong-olympics.png)

## Ubuntu Prerequisites

Before you can run Pong Olympics, you'll need to make sure you have the following installed on your system:

1. [Python](https://www.python.org/downloads/) (python 3.10)
2. [Make](https://www.gnu.org/software/make/)

## Installation

To install Pong Olympics and its dependencies, run the following command:

```bash
$ make install
```

## Running the game

To start playing Pong Olympics, run the following command:

```bash
$ make run
```

## Running Tests

To run the test suite for Pong Olympics, use the following command:

```bash
$ make test
```

## Troubleshooting

If you encounter an error message about the Tkinter module not being found, you may need to install it. You can do this by running the following command:

```bash
$ apt-get install python3-tk
```

**Note:** Pong Olympics is still a work in progress and currently only has one level.
