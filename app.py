# app.py

from alicepy.alice import Component, html
from styles import couter_style


def app():
    template = html(
        f"""
        <p>Counter: <span id="n">0</span></p>
        <button id="inc-btn">Increment</button>
        <AnotherCouter />
    """
    )

    states = {"n": 0}

    counter = Component(template, states, style=couter_style.style)

    @counter.reactive("inc-btn")
    def increment(self, event):
        return self.set_state("n", self.states["n"] + 1)

    return counter.render()
