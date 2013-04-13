#!/usr/bin/env python
"""
todo:
* refactor parsing of the command line args, especially generating output
* add tags, archive and rss feeds
* use Makefile for interfacing with takataka.py
* add search functionality
* make server compatible with WSGI
"""

import sys
import os
import settings
from markdown import markdownFromFile
from jinja2 import Environment,FileSystemLoader

# root path of this folder
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# path to articles
CONTENT_PATH = os.path.join(ROOT_PATH, settings.CONTENT_DIR)

# path to generated html
OUTPUT_PATH = os.path.join(ROOT_PATH, settings.OUTPUT_DIR)

# path to current theme's static directory
THEME_DIR = os.path.join(ROOT_PATH, "themes", settings.THEME) 
STATIC_DIR = os.path.join(THEME_DIR, settings.STATIC_DIR)

# the default listening port
DEFAULT_LISTENING_PORT = 9840

def render_template(template_name, context):
    extensions = context.pop('extensions', [])
    # globals = context.pop('globals', {})
    # print context

    THEME_TEMPLATE_DIR = os.path.join(THEME_DIR, "templates")
    jinja_env = Environment(loader=FileSystemLoader(THEME_TEMPLATE_DIR), 
            extensions=extensions,)
    
   # jinja_env.globals.update(globals)

    #jinja_env.update_template_context(context)
    rendered_html_template = jinja_env.get_template(template_name).render(context)
    
    # return the rendered template
    return rendered_html_template

def generate_html(content_path, output_path): 
    """generates html output from markdown by 
    recursivley scanning content directory"""
    
    from fnmatch import fnmatch
    import os.path
    from markdown import Markdown

    # instantiate markdown parser
    md = Markdown(extensions=['meta', 'codehilite', 'nl2br', 'extra'])
    
    """group content under the directories found in the CONTENT_APTH
     For example, if you have pages, posts, poems directories in the CONTENT_PATH,
     all the files in these directories should be parsed and categorized accordinly.
     So, we would have something like this
     CONTENT_DIRECTORIES['PAGES'] = [articles foundin the pages directory and parse]
     CONTENT_DIRECTORIES['POSTS'] = [articles foundin the posts directory and parse]
     CONTENT_DIRECTORIES['POEMS'] = [articles foundin the poems directory and parse]

    """
    # global variable that holds all the metadata 
    CONTENT_DIRECTORIES = {}
   
    # convert all markdown files to html
    def md_to_html(pattern, dirname, files):
        # create placeholder for this directory to hold all posts found in it
        # CONTENT_DIRECTORIES['POSTS'].append('article')
        dir_basename = os.path.basename(dirname).upper()
        CONTENT_DIRECTORIES[dir_basename] = []
       
        for filename in files:
            if fnmatch(filename, pattern):
                src = os.path.join(content_path, dirname, filename)
                modified_filename = os.path.splitext(filename)[0] + '.html'
                dest = os.path.join(output_path, os.path.basename(dirname), 
                        modified_filename)
                # print "processing ",  dirname
                with open(src) as f:
                    html_content = md.convert(f.read().decode('utf-8'))
                    metadata = md.Meta
                    #  print metadata
                    if('status' in metadata and metadata['status'][0] == 'draft'):
                          #  print dest +  metadata['status'][0]
                          pass
                    else:
                        # article url
                        url = dir_basename.lower() + '/' + modified_filename 
                        # add parsed html to dict
                        metadata.update({'content': html_content, 'url' : url,
                            'dest_path' : dest, 'category' : dir_basename.lower()})
                        
                        # here, we are building a list of articles - hash objects
                        CONTENT_DIRECTORIES[dir_basename].append(metadata)
                        # print ("NUMBER OF %s === " + 
                        #    str(len(CONTENT_DIRECTORIES[dir_basename]))) % dir_basename

    # now, recursively process files in the content directory
    os.path.walk(content_path, md_to_html, '*.md')

    # print CONTENT_DIRECTORIES['PAGES']
    CONTENT_DIRECTORY_FOLDERS =  CONTENT_DIRECTORIES.keys()
    
   # print "NUMBER OF POSTS === " + str(len(CONTENT_DIRECTORIES['PAGES']))
    # export all globals variables in here and i
    import copy
    TEMPLATE_GLOBALS = copy.deepcopy(CONTENT_DIRECTORIES)
    TEMPLATE_GLOBALS.update(vars(settings))
    # finally render each post by parsing the jinja template files
    for directory_name in CONTENT_DIRECTORY_FOLDERS:
        for post in CONTENT_DIRECTORIES[directory_name]:
            TEMPLATE_GLOBALS.update({'article': post})
            
            # now render the jinja2 template file
            jinja2_html = render_template('post.html', 
                    TEMPLATE_GLOBALS)
            
            # recreate the directories in the content diretory in the output directory
            if not os.path.isdir(output_path):
                os.mkdir(output_path)
            
            # path to output directory for this category of posts
            output_category_directory = os.path.join(output_path,  directory_name.lower())
            if not os.path.isdir(output_category_directory):
                os.mkdir(output_category_directory)

            with open(post['dest_path'], 'w') as f:
                f.write(jinja2_html.encode('utf-8'))
            
    # now, generate the index.html file
    with open(os.path.join(OUTPUT_PATH, 'index.html'), 'w') as f:
            TEMPLATE_GLOBALS.update({'articles': CONTENT_DIRECTORIES['POSTS']})
            jinja2_html = render_template('index.html', TEMPLATE_GLOBALS)
            f.write(jinja2_html.encode('utf-8'))

def generate(content_path, output_path):
    "generates the html files by recursively scanning the content directory"
    if (content_path and output_path) :
         generate_html(content_path, output_path)

         # copy static files into output directory
         OUTPUT_PATH_STATIC_DIR = os.path.join(OUTPUT_PATH, 'assets')
         
         import shutil 
         shutil.rmtree(OUTPUT_PATH_STATIC_DIR)
         import shutil
         shutil.copytree(STATIC_DIR, OUTPUT_PATH_STATIC_DIR)
    else:
        print "Error: invalid content path or output path"

def help():
  "prints command usage"
  print "USAGE: python takataka.py [serve | generate] OPTIONS"

def serve(server_address):
    "starts server to handle http requests"   
    # start SimpleHTTPServer in verbose mode
    import sys
    import BaseHTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler


    HandlerClass = SimpleHTTPRequestHandler
    ServerClass  = BaseHTTPServer.HTTPServer
    Protocol     = "HTTP/1.0"


    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    
    # cd into the output directory
    os.chdir(OUTPUT_PATH)
    httpd.serve_forever()


def watch_dir(path):
  "wathes content directory for changes and "
  pass


if __name__ == "__main__":
  if "serve" in sys.argv:
     # ternary logic : a = 1 if True else 0
      port = int(sys.argv[3].strip()) if '-p' in sys.argv else DEFAULT_LISTENING_PORT 
      serve(('127.0.0.1', port))
  elif "generate" in sys.argv:
      #print ROOT_PATH,  CONTENT_PATH, OUTPUT_PATH
      generate(CONTENT_PATH, OUTPUT_PATH)
  else:
     "print usage for unknown commands"
     help()


