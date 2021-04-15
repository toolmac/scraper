import feedparser
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def fetch():
    mcpt = feedparser.parse('https://mcpt.ca/feed/blog/atom/')
    wlmac = feedparser.parse('https://wlmac.ca/feed/')

    announcements = []

    announcements.extend(mcpt.entries)
    announcements.extend(wlmac.entries)

    announcements.sort(key=lambda x: x.published_parsed)
    announcements.reverse()

    return jsonify(announcements)
