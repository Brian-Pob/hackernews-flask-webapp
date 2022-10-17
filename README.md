# COP4521

## Authors

Brian Poblete - bap21k

Jayen Lare - jsl19b

Group 9

## Project Notes

The production application is running on Digital Ocean. For development, we
should be running local instances of the server on other machines. This could
be our bare metal machines or on other VMs. These dev machines should have
the same or similar setups to the production machine. That means setting up
Ubuntu 22.04, python3, pip, pipenv, gunicorn, nginx, etc.

## Extra Credit

We will attempt to implement automatic CI/CD with Pulumi.

## Commands 

For local development without nginx: `pipenv run gunilocal`
With nginx (background): `pipenv run guni`
With nginx (foreground + debug mode): `pipenv run gunidebug`

For database

```
flask db stamp head
flask db migrate
flask db upgrade
```

## What does curl news.brian.pob.me do?

1. curl news.brianpob.me

2. 

## Project Security

## References

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date


