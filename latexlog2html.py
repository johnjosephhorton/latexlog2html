import os 
import re 


def create_anchor(notice_type, n): 
    return "</pre><a name='%s%s'><a href='#top'><h2>Back to top</h2></a><pre>" % (
        notice_type, n)

def parse_latex_log(log_file_name):
    warning_re = r"""LaTeX Warning: .*"""
    error_re = r"""!.*"""
    warnings, errors, body = [], [], []
    log_file = open(log_file_name, "r")   
    body = []
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
    list_items = []
    for index, item in enumerate(item_list):
        list_items.append("<li><a href='#%s%s'>%s</a></li>" % (tagname, index + 1, item))
    return """<h1>%s</h1>""" % heading  + """<ol>%s</ol>""" % ''.join(list_items)


def convert_log(log_file_name, header_template, css_hotlink):
    """ 
    Parses a latex log file and returns HTML. 
    """
    warnings, errors, body = parse_latex_log(log_file_name)
    new_log = []
    new_log.append(header_template % css_hotlink)
    new_log.append(create_ordered_list("Errors", "error", errors))
    new_log.append(create_ordered_list("Warning", "warn", warnings))
    new_log += ["<h1>Full Log</h1><pre>"] + body + ['</pre></body></html>']
    return new_log 


    latex_log = os.path.join(output_dir, "writeup", "%s.log" % topic)
    html_latex_log = l2h.convert_log(latex_log, 
                                    templates.LATEX_LOG_FILE_HEADER,
                                    settings.CSS_HOTLINK)
    # write the log file
    f = open(os.path.join(output_dir, settings.LATEX_HTML_FILE_NAME), "w")
    f.writelines(html_latex_log)
    f.close() 
      
    report_location = os.path.join(output_dir, settings.EXEC_REPORT)
    os.system("%s %s" % (settings.BROWSER, report_location))
    return True    
