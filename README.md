# Interpolation

Study project during IITP Python courses. In this project I implement some 2D interpolation techinques, including bilinear and optimal in L2 interpolation.

## Quick start

1. Clone repository to your local device

    ```pwsh
    git clone "https://github.com/alabar6/abgarian_python2025"
    ```

2. Install poetry on your device

3. In project directory run:

    ```pwsh
    poetry config virtualenvs.in-project true
    ```
    
    ```pwsh
    poetry install
    ```

## Ruff check

To check some rules, run:

```pwsh
poetry run ruff check
```

## Basic functionality

To use some interpolation techinques, run:

```pwsh
poetry run demo --image_dir [...] --method [...] --scale_x [...] --scale_y [...]
```