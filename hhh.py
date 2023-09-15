from flask import Flask, request
from flask import make_response as resp
from flask import render_template_string as render
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
known_user_facts = defaultdict(int)
get_ua = lambda r: r.headers.get("User-Agent", "unknown")


@app.get("/")
def _():
    known_user_facts["telemetry"] += 1
    user_info = get_ua(request)
    if not user_info:
        return render_resp("OK", 200)
    known_user_facts[user_info] += 1
    return render_resp("OK", 200)


@app.get("/metrics")
def metrics():
    frm = f"""# Req at {datetime.now()}, total {known_user_facts["telemetry"]}, from {get_ua(request)}
{{% for k, v in d.items() %}}useragent_metric{{% raw %}}{{device={{% endraw %}}{{{{ k }}}}}} {{{{ v }}}}\n{{% endfor %}}\n# Unique data entires: {known_user_facts["unique data"]}"""
    response = render_resp("", 200, frm, {"d": known_user_facts})
    response.mimetype = "text/plain"
    return response


def render_resp(ctx, code, additional="", data={}):
    return resp(render(f"{ctx}\n"+additional, **data), code)


if __name__ == '__main__':
    app.run("0.0.0.0", 8080)
print(known_user_facts)