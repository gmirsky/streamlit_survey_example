# A Streamlit Survey Example

A simple example of using the survey class for Streamlit,

This example features some basic Streamlit survey functionality in a python program. There is minimal logic and error checking. This example is designed to show the survey capabilities of Streamlit.

## Prerequisites

- Docker or Podman installed.
- Git installed

## Run the example

Clone this library using the following command:

```shell
git clone https://github.com/gmirsky/streamlit_survey_example.git
```

Navigate to the directory that you just cloned from Github.

Build the container using the following command:

```shell
docker build -t survey:latest .
```

Verify that the docker image was built.

```shell
docker image ls
```

Run the container using the following command:

```shell
docker run -p 8501:8501 survey:latest
```

Now open your browser and open up the following web site:

```shell
http://127.0.0.1:8501
```
