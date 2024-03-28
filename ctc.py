import json


def handler(event, context):
    # Read the content of the HTML file
    with open("./Salary Calculation/intraCTC.html", "r") as file:
        html_content = file.read()

    return {
        "statusCode": 200,
        "body": html_content,
        "headers": {"Content-Type": "text/html"},
    }
