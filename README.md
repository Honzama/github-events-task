# github-events-task

Using Flask framework to load events from [https://api.github.com/events](https://api.github.com/events) API

## How to run in localhost

- Run and build project with "docker-compose up"

## Localhost endpoints

- List of repositories with pull request avg time: [http://localhost:8080/repositories](http://localhost:8080/repositories)
- Total number of events grouped by the event type: [http://localhost:8080/events/type](http://localhost:8080/events/type)
  - With 10 minute offset: [http://localhost:8080/events/type?offset=10](http://localhost:8080/events/type?offset=10)
- Plot of total number of events grouped by the event type: [http://localhost:8080/events/plot](http://localhost:8080/events/plot) 

## C4 (level 1) Model

![image](https://user-images.githubusercontent.com/13302578/192516146-918df841-5354-4d33-abc7-fd2bfccd475e.png)

## Assumptions

- Flask framework is a good choice because of its simplicity and flexibility

- Using Docker is good for reproducibility across multiple machines

- Calling the GitHub Events API every minute is near optimal frequency because of the 60 calls per minute rate limit

- Picking up an external ID from the GitHub Events API is an easier approach than generating a custom ID in the database
