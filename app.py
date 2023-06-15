# app.py

from alicepy.alice import Component
from components.another import another_couter


def counter():
    template = f"""
        <p>Counter: <span id="n">0</span></p>
        <button id="inc-btn">Increment</button>

        {another_couter()}
        {another_couter()}
        {another_couter()}
    """
    states = {"n": 0}
    style = """
        p, button {
            font-size: 30px;
        }
    """

    counter = Component(template, states, style=style)

    def increment(event):
        return counter.set_state("n", counter.states["n"] + 1)

    counter.reactive("inc-btn", increment)
    return counter
