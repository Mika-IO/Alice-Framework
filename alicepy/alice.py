# alicePy.py

from browser import document


"""
    TODO:
        rende father to child
        how handles component Ids
        scope css
"""


class Component:
    def __init__(self, html_content: str, states={}, style=None):
        self.html_content = html_content
        if style:
            self.html_content = f"<style>{style}</style>{self.html_content}"
        self.container = document.createElement("div")
        self.container.innerHTML = self.html_content.strip()
        self.states = states

        self.render()

    def mount(self):
        return self.container

    def run(self, element_id=None):
        if element_id:
            document[element_id].appendChild(self.container)
        else:
            document["root"].appendChild(self.container)

    def render(self):
        print(self.html_content)

        return f"<div onload={self.run()}></div>"

    def set_state(self, key, value):
        self.states[key] = value
        element = self.container.querySelector(f"#{key}")
        element.textContent = f"{self.states[key]}"

    def reactive(self, element_id, event="click"):
        def decorator(func):
            def wrapper(self, event):
                return func(self, event)

            element = self.container.querySelector(f"#{element_id}")
            element.addEventListener(event, wrapper)
            return wrapper

        return decorator


def convert_camel_to_snake(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case


def html(html):
    tags = html.split("\n")
    tags = [tag.strip() for tag in tags]
    for i in range(len(tags)):
        if tags[i].startswith("<") and tags[i].endswith("/>"):
            component = tags[i][1:-3].strip()
            if component[0].isupper():
                component_name = convert_camel_to_snake(component)
                try:
                    tags[i] = exec(
                        f"from components.{component_name} import {component_name}\n{component_name}()"
                    )
                except ImportError:
                    raise ImportError(f"Component '{component_name}' is not defined.")
    result = f"\n".join(tags).strip()
    return result
