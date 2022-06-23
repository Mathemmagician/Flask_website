# My Website

I've always wanted to learn Flask and SQL, improve my Git/GitHub skills, work with a dedicated Linux 
server and make fully working website.
It's just a really nice idea to have an easily sharable personal space which you built from scratch, where you can show off
your personal projects, ideas and hobbies. Hopefully you enjoy it as much as I do!

This is the product of my efforts: https://www.Ramilus.com

I'll be updating it regularly since I now have all the time in the world.

If it inspires you to build your own website, please check out [Corey Schafer's Flask series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).
He is just an awesome human being and he shows you how to put all of these tools together really well.


## Useful


### For migrations:

https://flask-migrate.readthedocs.io/en/latest/

```
$ export FLASK_APP=flaskblog
$ flask db init
$ flask db migrate
$ flask db upgrade
```

### For factory application context:

```
>>> from yourapp import create_app
>>> app = create_app()
>>> app.app_context().push()
```


