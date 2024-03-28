import json


def handler(event, context):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample Page</title>
        <style>
            /* Your CSS styles here */
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                color: blue;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to my Serverless Page</h1>
        <p>This is a sample HTML page served by a Python serverless function.</p>
        <script>
            // Your JavaScript code here
            console.log('This is JavaScript running on the client side.');
        </script>
    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "body": html_content,
        "headers": {"Content-Type": "text/html"},
    }
