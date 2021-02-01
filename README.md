## API
We have a simple API that is responsible for displaying the current local time for a user. 
Right now, you can hit the */time/* endpoint and recieve back the local time OR pass in a timezone as a 
keyword to get the current time for that timzezone */time?tz=America/Los+Angeles*. 

## Deliverable:
    - We'd like an endpoint that would return back all the current times in all US timezones.

## Applicable documentation:
    - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - [Pytz](https://pythonhosted.org/pytz/)
    - [datetime](https://docs.python.org/3/library/datetime.html)