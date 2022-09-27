# github-events-task

Using Flask framework to load events from [https://api.github.com/events](https://api.github.com/events) API

## How to run in localhost

- Run and build project with "docker-compose up"

## Localhost endpoints

- List of repositories with pull request avg time: [http://localhost:8080/repositories](http://localhost:8080/repositories)
- Total number of events grouped by the event type: [http://localhost:8080/events/type](http://localhost:8080/events/type)
- Total number of events grouped by the event type with 10 minute offset: [http://localhost:8080/events/type?offset=10](http://localhost:8080/events/type?offset=10)
- Plot of total number of events grouped by the event type: [http://localhost:8080/events/plot](http://localhost:8080/events/plot) 
