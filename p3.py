######### Fun Fact Generator App #########

from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import requests


def app():

    def get_fun_facts():

        clear()

        put_html("<p align='right'>"
                 "<h3><img src='https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png'"
                 " width='5%' bg='white'> Fun Facts Generator </h3></p>")

        put_scope("Fact")

        url = "https://uselessfacts.jsph.pl/random.json?language=en"

        data = requests.get(url).json()
        useless_fact = data["text"]

        with use_scope("Fact", clear=True):
            put_text(useless_fact).style('color: red; font-size: 20px')

        put_button("Click me", onclick=get_fun_facts)
    get_fun_facts()

start_server(app, 8080)


