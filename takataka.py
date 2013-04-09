#!/usr/bin/env python
"""
todo:
* refactor parsing of the command line args, especially generating output
* add tags, archive and rss feeds
* use Makefile for interfacing with takataka.py
"""

import sys
import os
import settings
from markdown import markdownFromFile


# root path
ROOT_PATH = os.path.dirname(__file__)

# path to articles
CONTENT_PATH = os.path.join(ROOT_PATH, settings.CONTENT_DIR)

# path to generate html
OUTPUT_PATH = os.path.join(ROOT_PATH, settings.OUTPUT_DIR)


def generate_html(src, dest): 
  "generates html output from markdown"
  pass

def generate_posts(posts_dir):
  "generates blog posts"
  pass

def generate_pages(pages_dir):
  "generates articles in the /pages path such as about, contact etc" 
  pass

def generate(content_path, output_path):
  "generates the posts and pages by calling their respective generator functions"
  pass

def help():
  "prints command usage"
  print "USAGE: python takataka.py [serve | generate] OPTIONS"

def serve(port):
  "starts server to handle http requests"   
  pass

if __name__ == "__main__":
  if "serve" in sys.argv:
      serve()
  elif "generate" in sys.argv:
      generate()
  else:
     "print usage for unknown commands"
     help()


