# another_couter.py

from alicepy.alice import Component, html
from styles.another_couter_style import style


def another_couter():
    template = html(
        f"""
        <div id="another">
            <Text />
            <p>Counter: <span id="n">0</span></p>
            <button id="inc-btn">Increment</button>
        </div>
    """
    )
    states = {"n": 0}

    counter = Component(template, states, style=style)

    def increment(event):
        return counter.set_state("n", counter.states["n"] + 1)

    counter.reactive("inc-btn", increment)
    return counter.render()
