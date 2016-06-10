#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# We have all these libraries that other people already created. So we are stealing (importing) with pride.
import webapp2
#jinja2 is the html magic that renders our templates
import jinja2
import os

my_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#is the main root domain on our browesr but what is a class, and it's signifiance
class ItemHandler(webapp2.RequestHandler):

#when it goes to the root route, it pulls the item handler. If request is a get request.
    def get(self):
        #showing our form on the root domain
        item_template=my_environment.get_template('templates/check.html')
        #we got our form templete, and now we stored it in variable item_template, we are now going to render the template as a response to the get request.
        self.response.write(item_template.render())

#now, post request allows us to recieve user imput.
    def post(self):
    #So a request is made and goes to controller which knows that the / route should go to the ItemHandler. At that point it figures out that it should go to post because our form says the method is "post" instead of "get". Thus we are now in the post function which we've defined below
        def checkItem(item):
            item_list =["Apple","Airheads","Boiled Egg"]
            if item in item_list:
                message = "In Stock"
            else:
                message = "Not in Stock"
            return message
    #
        instock_results = checkItem(self.request.get("item_name"))
        #Print instock_results = message
        message_variables = {"in_stock_or_not":instock_results}
        results_template=my_environment.get_template('templates/results.html')
        self.response.write(results_template.render(message_variables))

#we created this route as practice, but no one should go to this route.
class CheckHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Let me check on what you are looking for.')

app = webapp2.WSGIApplication([
    ('/', ItemHandler), #/ is the route that would lead to the ROOT domain
    ('/check', CheckHandler),
], debug=True)
