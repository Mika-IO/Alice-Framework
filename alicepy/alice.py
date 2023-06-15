# alicePy.py

from browser import document


class Component:
    def __init__(self, html_content: str, states: dict, style=None):
        if style:
            html_content = f"<style>{style}</style>{html_content}"
        self.container = document.createElement("div")
        self.container.innerHTML = html_content.strip()
        self.states = states

    def mount(self):
        return self.container

    def run(self, element_id=None):
        print("render")
        if element_id:
            document[element_id].appendChild(self.container)
        else:
            document["root"].appendChild(self.container)

    def render(self):
        return f"<div onload={self.run()}></div>"

    def set_state(self, key, value):
        self.states[key] = value
        element = self.container.querySelector(f"#{key}")
        element.textContent = f"{self.states[key]}"
        print("set-state")

    def reactive(self, element_id, function, event="click"):
        element = self.container.querySelector(f"#{element_id}")
        element.addEventListener(event, function)
        print("reactive")
