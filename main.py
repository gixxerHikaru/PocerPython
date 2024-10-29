from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pocer import distribution, judge
app = FastAPI()


@app.get("/pocer/", response_class=HTMLResponse)
async def read_items():
    cards = distribution.func()
    result = judge.func(cards)
    return """
    <html>
        <head>
            <title>Pocer</title>
        </head>
        <body>
            <h1>Your Card</h1>
            <h2>
    """ + str(cards) + """</h2>
    <h3>Your Hand is...</h3>
    <h2>
    """ + str(result) + """</2>

        </body>
    </html>
    """    
    