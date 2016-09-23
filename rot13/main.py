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
import os
import webapp2
import jinja2

form = """
    <h1>Enter some text to ROT13:</h1>
    <form method="post" action="/rot13">
        <textarea style="height: 100px; width: 400px;" name="text"></textarea>
        <input type="submit">
    </form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
    def post(self):
        text = self.request.get("text")
        newText = ""
        for letter in text:
            numericValue = ord(letter)
            if numericValue >=97 and numericValue <= 122:
                if numericValue + 13 > 122:
                    newText += chr(((numericValue + 13) - 122) + 96)
                else:
                    newText += chr(numericValue + 13)
            elif numericValue >=65 and numericValue <= 90:
                if numericValue + 13 > 90:
                    newText += chr(((numericValue + 13) - 90) + 64)
                else:
                    newText += chr(numericValue + 13)
            else:
                newText += letter
        #self.response.out.write(newText)
        self.redirect("/rot13")



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rot13',MainHandler)
], debug=True)