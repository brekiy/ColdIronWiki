import json
import os
import logging
import jinja2

def generate(verbose, input_dir, config_obj):
    """Generate the pages from the config."""
    logging.debug('entered generate')
    base_output = input_dir + '/html'
    template_dir = input_dir + '/templates'
    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        autoescape=jinja2.select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    if not os.path.exists(template_dir):
        print('Error_FileNotFound: couldn\'t find the template directory')
        exit(1)
    if not os.path.exists(base_output):
        os.makedirs(base_output)
    else:
        print('Error: output directory already contains files: ' + base_output)
        exit(1)
    # Check for optional static directory
    if os.path.exists(input_dir + '/static'):
        logging.debug('found static files')
        try:
            distutils.dir_util.copy_tree(input_dir + '/static', base_output)
        except FileNotFoundError:
            print('Error_FileNotFound: coudln\'t copy the static files')
            exit(1)
        if verbose:
            print('Copied ' + input_dir + '/static/ -> ' + base_output + '/')
    for page in config_obj:
        logging.debug('url: %s', page["url"])
        try:
            template = template_env.get_template(page['template'])
        except jinja2.TemplateError:
            print('Error_Jinja: couldn\'t find template ' + page['template'])
            exit(1)
        output = ''
        for key in page['context']:
            logging.debug('key=%s', key)
            logging.debug('val=[%s]', page['context'][key])
            try:
                output = template.render(page['context'])
            except jinja2.TemplateError:
                print('Error_Jinja: couldn\'t render ' + page['template'])
        url = base_output + page['url'] + 'index.html'
        # Check that the path exists
        if not os.path.exists(base_output + page['url']):
            os.makedirs(base_output + page['url'])
        with open(url, 'w+', encoding='utf-8') as html:
            html.write(output)
            if verbose:
                print('Rendered ' + page["template"] + ' -> ' + url)
