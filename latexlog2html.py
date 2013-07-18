#!/usr/bin/env python
import argparse 
import os 
import re 
import sys

HTML_HEADER =  """<html><head> 
 <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
</head><body> 
"""

def create_anchor(notice_type, n): 
    return "</pre><a name='%s%s'><a href='#top'><h2>Back to top</h2></a><pre>" % (
        notice_type, n)

def parse_latex_log(log_file_name):
    """"Iterates through each line and finds LaTeX warnings or errors.
        It them appends these error and warning messages to respective lists. 
     """
    warning_re = r"""LaTeX Warning: .*"""
    error_re = r"""!.*"""
    warnings, errors, body = [], [], []
    log_file = open(log_file_name, "r")   
    for line in log_file:
        if re.search(warning_re, line): 
            warnings.append(line)
            warning_anchor = create_anchor("warn", len(warnings))
            body.append(warning_anchor)
        if re.search(error_re, line): 
            errors.append(line)
            error_anchor = create_anchor("error", len(errors))
            body.append(error_anchor)
        body.append(line)
    return warnings, errors, body


def create_ordered_list(heading, tagname, item_list):
    """Creates an HTML ordered list """
    list_items = []
    for index, item in enumerate(item_list):
        list_items.append("<li><a href='#%s%s'>%s</a></li>" % (tagname, index + 1, item))
    return """<h1>%s</h1>""" % heading  + """<ol>%s</ol>""" % ''.join(list_items)


def convert_log(log_file_name, header_template):
    """ 
    Parses a latex log file and returns HTML. 
    """
    warnings, errors, body = parse_latex_log(log_file_name)
    new_log = []
    new_log.append(header_template)
    new_log.append(create_ordered_list("Errors", "error", errors))
    new_log.append(create_ordered_list("Warning", "warn", warnings))
    new_log += ["<h1>Full Log</h1><pre>"] + body + ['</pre></body></html>']
    return new_log 

def main():    
    parser = argparse.ArgumentParser(description='Process a LaTeX log file')
    parser.add_argument("-f", "--file", help = "Log file to parse")
    parser.add_argument("-b", "--browser", help = "Browser to use to open file")
    args = parser.parse_args()

    g = open("sample.html", "w")
    html_output = convert_log(args.file, HTML_HEADER)
    g.write(''.join(html_output))
    g.close()
    os.system(args.browser + " sample.html")   


if __name__ == '__main__':
    main()

