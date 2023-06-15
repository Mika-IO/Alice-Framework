# app.py

from alicepy.alice import Component


def another_couter():
    template = f"""
        <div>
            <p>Counter: <span id="n">0</span></p>
            <button id="inc-btn">Increment</button>  
        </div>
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
    return counter.render()
