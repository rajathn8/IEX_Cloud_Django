'''
 this course is from codemy.com
'''

1 - made virtual environment

---> pip freeze
---> activate.fish
--> pytz python time zone
---> sqlparser database

2-  8000 ---> local default

--- never mess with wgsi file 

3- django admin is used for database stuff.

create the database
then migrate it

makemigrations+migrate

-techsupport.
-messageboard.
--build a messaging app

everythin is an app in django.

add the app in the settings file in the main app file


django interaction
[ views---urls----pageitself]

template-- views --- urls 

websites
- navigation bar at the top
- header at the top 
- footer at the bottom

Base File : --designate a base file
{% %}
will pull every other base file we have on our screen and put it inside this 

 -- above and below : is for keeping the headers and footers -- this is making sure we dont have to make any changes on each and every website.


JSon - is a python dictionary

json looping:
'''
{% for key, value in api.items %}
			{{ key }}: {{ value }}<br/>
		{% endfor %}

''' 