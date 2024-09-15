
Running all docker process for websploit makes Thinkpad heat up and blow hot air through the fan. Stop all Docker processes :

```
docker stop $(docker ps -a -q
```

This will stop all the Docker process. No more hot blowing or heating up the laptop. This laptop has 16 GB RAM. 

- Install websploit on 64 GB Yoga and see if the problem goes away.
