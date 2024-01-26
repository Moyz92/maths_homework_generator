import random as rnd
from jinja2 import Environment, FileSystemLoader

class make_homework:
    def __init__(self):
        self.template = '''
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                </head>
                
                <body>
                    <ol>
                        {% for index in range(0, 10): %}
                            {% if index <= 1: %}
                              <li><h3> √{{rnd.randint(7, 200)}} </h3></li>
                            {% elif index >= 2 and index <= 4: %}
                              <li><h3> √{{rnd.randint(7, 99)}}.{{ rnd.randint(2, 99)}} </h3></li>
                                                    
                            {% elif index >= 5 and index <= 7: %}
                              <li><h3> {{ rnd.randint(8, 100) }}^2 </h3></li>  
                            {% elif index >= 8 and index <= 9: %}
                              <li><h3> {{rnd.randint(7, 100)}}.{{rnd.randint(2, 99)}}^2 </h3></li>
                            {% endif %}
                        {% endfor %}
                    </ol>
                </body>
            </html>
            '''

    def get_template(self):
        env = Environment(loader=FileSystemLoader('/'))
        env.globals['rnd'] = rnd
        template = env.from_string(self.template)
        rendered_template = template.render()
        return rendered_template