from flask import Flask, request
import datetime
import pytz
import json

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "ok", 200


@app.route('/time', methods=['GET'])
def get_time():
    """
    The endpoint takes in optional `tz`
    argument to specify a timezone, returning
    current time in the HH:MM:SS format.

    Example:
        /time?tz=America/Los+Angeles
    Returns:
        {"America/Los_Angeles": "11:16:28"}
    """
    def _get_local_time():
        local_time = datetime.datetime.now()
        time_string = local_time.strftime("%H:%M:%S")
        return time_string


    if request.args:
        tz = request.args.get('tz')
        try:
            tz = tz.replace(" ", "_")
        except Exception:
            return f"Could not process timezone: {tz}", 404
        try:
            local_time = datetime.datetime.now()
            tz_time = pytz.timezone(tz)
            tz_localized = local_time.astimezone(tz_time)
            time_string = tz_localized.strftime("%H:%M:%S")
            return json.dumps({f"{tz}": time_string})
        except Exception:
            return f"Could not process timezone: {tz}", 404
    else:
        try:
            time_string = _get_local_time()
            return json.dumps({"Local time": time_string})
        except Exception as e:
            return f"Could not process time information. {e}", 404

#TODO Add a route that displays the current time for all US timezones.
@app.route('/us-timezones', methods=['GET'])
def get_us_timezones():
    us_timezones = ['Los_Angeles','Denver','Chicago','New_York']

    for zone in us_timezones:
      try:
        local_time = datetime.datetime.now()
        tz_time = pytz.timezone(f"America/{zone}")
        tz_localized = local_time.astimezone(tz_time)
        time_string = tz_localized.strftime("%H:%M:%S")
        return json.dumps({f"{zone}": time_string})
      except Exception as e:
        print(e)



if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')