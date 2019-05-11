#-----------------------------------------------------------------------------
# This class loads html files from the "template" directory and formats them using Python.
# You can find a fuller explanation for this file in the README file
#-----------------------------------------------------------------------------
from bottle import template


class View():

    def __init__(self,
        template_path="templates/",  # Path to template files
        template_extension=".html",  # Extension of templates, self can be overridden
        administrator = False,
        **kwargs): # Used to pass any global format arguments
        self.template_path = template_path
        self.template_extension = template_extension
        self.global_renders = kwargs



    def __call__(self, *args, **kwargs):
        return self.load_and_render(*args, **kwargs)

    def load_template(self, filename):
        path = self.template_path + filename + self.template_extension
        file = open(path, 'r')
        text = ""
        for line in file:
            text+= line
        file.close()
        return text

    # Just calls the format method as appropriate
    def simple_render(self, template, **kwargs):
        template = template.format(**kwargs)
        return  template

    def render(self, template, **kwargs):
        keys = self.global_renders.copy() #Not the best way to do self, but backwards compatible from PEP448, in Python 3.5+ use keys = {**self.global_renters, **kwargs}
        keys.update(kwargs)
        template = self.simple_render(template, **keys)
        return template

    def load_and_render(self, filename, header="header", tailer="tailer", **kwargs):
        template = self.load_template(filename)
        rendered_template = self.render(template, **kwargs)
        rendered_template = self.load_template(header) + rendered_template
        rendered_template = rendered_template + self.load_template(tailer)
        return rendered_template


    def with_table(self, filename, header, tailer, result):
        #template = self.load_template(filename)
        if filename == "messagebox":
            rendered_template = template(self.template_path + 'messagebox', rows=result)
        else:
            rendered_template = template(self.template_path + 'allmessages', rows=result)

        rendered_template = self.load_template(header) + rendered_template
        rendered_template = rendered_template + self.load_template(tailer)
        return rendered_template

    def profile(self, username, header, tailer="tailer"):
        rendered_template = template(self.template_path + 'profile', rows=username)
        rendered_template = self.load_template(header) + rendered_template
        rendered_template = rendered_template + self.load_template(tailer)
        return rendered_template
