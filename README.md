# Pong Olympics

Pong Olympics is my own spin off of [Video Olympics](https://en.wikipedia.org/wiki/Video_Olympics) on the Atari 2600, written in python.

![pong-olympics](./docs/pong-olympics.png)

**Note:** This project is still a work in progress and currently only has one level.

## Ubuntu Prerequisites

1. [Python](https://www.python.org/downloads/) (python 3.10)
2. Make

## How to install dependencies

```bash
$ make install
```

## Troubleshoot

If you experience this error

```bash
ImportError: No module named 'Tkinter'
```

Install the following

```bash
$ apt-get install python3-tk
```

## How to run game

```bash
$ make run
```
