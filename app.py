from flask import Flask, request
from datetime import datetime
from dateutil.relativedelta import relativedelta
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


@app.route('/time-difference', methods=['GET', 'POST','PUT'])
def time_diff():
    try:
        if request.args:
            h = request.args.get('here')
            t = request.args.get('there')

        u = pytz.timezone('utc').localize(datetime.utcnow())
        here = u.astimezone(pytz.timezone(h)).replace(tzinfo=None)
        there = u.astimezone(pytz.timezone(t)).replace(tzinfo=None)

        offset = relativedelta(here, there) 
        return json.dumps(offset.hours)
    except Exception as e:
            return f"Could not process time information. {e}", 404


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')