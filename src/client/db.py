from jinja2 import Environment, FileSystemLoader


class SQLTemplateExecutor:
    def __init__(self, template_file, session, template_path):
        self.template_file = template_file
        self.session = session
        self.template_path = template_path

    def execute(self, **kwargs):

        env = Environment(loader=FileSystemLoader(searchpath=self.template_path))
        template = env.get_template(self.template_file)

        sql = template.render(**kwargs)

        result = self.session.execute(sql)
        return result.fetchall()
