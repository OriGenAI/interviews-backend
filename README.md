# Install and Run the project

## Requirements

- Python > 3.6
- SQLite3
- Virtualenv (optional)

## Install

```
pip install -r requirements.txt
```

## Run the server

```
FLASK_ENV=development flask run
```

# Database structure

## Satellite

- name: `satellite`
- structure:

```
|id|name|period|model_id|
```

## SatelliteModel

- name: `satellite_model`
- structure:

```
|id|name|
```

## HelloWorld

- name: `hello_world`
- structure:

```
|id|hello|world|
```

# Questions

## 1 - Satellite synchronization

You are a scientist at a remote satellite research observatory in Antarctica, tracking satellites as they fly overhead every day. On some days, no satellites fly over, but on others, multiple may pass by.

We have tracked all the satellites and we have added in our database the number of days that it takes to see the satellite again.

Today is the day we were able to see all of them, and we want to calculate when are we going to be able to see each satellite again in the next 21 days. Here is an example of the list that we want to create:

```json
{
  1: [],
  2: ["Satellite 1"],
  3: ["Satellite 2"],
  4: ["Satellite 1"],
  5: ["Satellite 3"],
  6: ["Satellite 1", "Satellite 2"],
  ...
}
```

## 2 - Satellite model

We also added some information about the satellite model but we have it in a different table. Can you help us listing all the models with the list of satellites associated to it?

```json
[
  {
    "id": 1,
    "name": "Model A",
    "satellites": [
      { "id": 1, "name": "satellite 1", "period": 2 },
      { "id": 2, "name": "satellite 2", "period": 3 }
    ]
  },
  {
    "id": 2,
    "name": "Model B",
    "satellites": [{ "id": 3, "name": "satellite 3", "period": 5 }]
  }
]
```
