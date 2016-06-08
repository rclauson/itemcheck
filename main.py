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
#
import webapp2
import jinja2
import os

my_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ItemHandler(webapp2.RequestHandler):
    def get(self):
        item_template=my_environment.get_template('templates/check.html')
        self.response.write(item_template.render())

class CheckHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Let me check on what you are looking for.')

app = webapp2.WSGIApplication([
    ('/', ItemHandler),
    ('/check', CheckHandler),
], debug=True)