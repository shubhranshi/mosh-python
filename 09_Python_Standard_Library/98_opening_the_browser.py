# This is about how to open a web browser in a python script.
# This is particularly useful if we are building an automation script that does a bunch of tasks
# and then open up a browser window.

# For example let's say we are building a script to deploy a website. We build the website on our
# local machine, and then deploy it to a webserver, and at the end we want to open the browser
# and type in the website page. This step is manual and can be automated.
# So we can have a python script open up a web browser at the end of the deployment

# Import the "webbrowser" module

import webbrowser

print("Deployment completed")

webbrowser.open("https://google.com")

