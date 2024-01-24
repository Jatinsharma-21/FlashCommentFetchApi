from flask import Flask, request, jsonify
import requests
from datetime import datetime
app = Flask(__name__)

BASE_URL = "https://app.ylytic.com/ylytic/test"


@app.route("/search", methods=["GET"])
def search_comments():
    search_author = request.args.get("search_author", None)
    at_from = request.args.get("at_from", None)
    at_to = request.args.get("at_to", None)
    like_from = request.args.get("like_from", None)
    like_to = request.args.get("like_to", None)
    reply_from = request.args.get("reply_from", None)
    reply_to = request.args.get("reply_to", None)
    search_text = request.args.get("search_text", None)

    # Build parameters for the request to the original API
    params = {
        "search_author": search_author,
        "at_from": at_from,
        "at_to": at_to,
        "like_from": like_from,
        "like_to": like_to,
        "reply_from": reply_from,
        "reply_to": reply_to,
        "search_text": search_text,
    }

    # Make a request to the original API
    response = requests.get(BASE_URL, params=params)

    # Parse the response from the original API
    comments = response.json()["comments"]

    # Perform additional filtering based on the search parameters
    filtered_comments = filter_comments(comments, search_author, at_from, at_to, like_from, like_to, reply_from, reply_to, search_text)

    return jsonify({"comments": filtered_comments})


def filter_comments(comments, search_author, at_from, at_to, like_from, like_to, reply_from, reply_to, search_text):
    filtered_comments = []

    for comment in comments:
        # Apply filters based on search parameters
        if (
            (not search_author or search_author.lower() in comment["author"].lower())
            and (not at_from or filter_by_date(comment["at"], at_from, at_to))
            and (not like_from or filter_by_likes(comment["like"], like_from, like_to))
            and (not reply_from or filter_by_replies(comment["reply"], reply_from, reply_to))
            and (not search_text or search_text.lower() in comment["text"].lower())
        ):
            filtered_comments.append(comment)

    return filtered_comments

def filter_comments(comments, search_author, at_from, at_to, like_from, like_to, reply_from, reply_to, search_text):
    filtered_comments = comments
    # Apply filters based on search parameters
    if search_author:
        filtered_comments = filter_by_author(filtered_comments, search_author)
    if at_from or at_to:
        filtered_comments = filter_by_date(filtered_comments, at_from, at_to)
    if like_from or like_to:
        filtered_comments = filter_by_likes(filtered_comments, like_from, like_to)
    if reply_from or reply_to:
        filtered_comments = filter_by_replies(filtered_comments, reply_from, reply_to)
    if search_text:
        filtered_comments = filter_by_text(filtered_comments, search_text)

    return list(filtered_comments)


def filter_by_author(comments, search_author):
    return [comment for comment in comments if search_author.lower() in comment["author"].lower()]

def filter_by_date(comments, at_from, at_to):
    filtered_comments = []

    for comment in comments:
        try:
            comment_date = datetime.strptime(comment["at"], "%a, %d %b %Y %H:%M:%S %Z")
            formatted_date = comment_date.strftime("%d-%m-%Y")
        except ValueError:
            print(f"Invalid date format: {comment['at']}")
            continue

        if (not at_from or formatted_date >= at_from) and (not at_to or formatted_date <= at_to):
            filtered_comments.append(comment)

    return filtered_comments



def filter_by_likes(comments, like_from, like_to):
    return [comment for comment in comments if (not like_from or (comment["like"] is not None and like_from <= comment["like"])) and
            (not like_to or (comment["like"] is not None and comment["like"] <= like_to))]


def filter_by_replies(comments, reply_from, reply_to):
    return [comment for comment in comments if (not reply_from or (comment["reply"] is not None and reply_from <= comment["reply"])) and
            (not reply_to or (comment["reply"] is not None and comment["reply"] <= reply_to))]


def filter_by_text(comments, search_text):
    return [comment for comment in comments if search_text.lower() in comment["text"].lower()]


if __name__ == "__main__":
    app.run(debug=True)
