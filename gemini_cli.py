import os
import pathlib
import textwrap
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
from rich.style import Style
from rich.style import Color
from pathlib import Path

exit_commands = ['/q', '\q', '/quit', '\quit', '/exit', '\exit']
clear_commands = ['/c', '\c', '/cls', '\cls', '/clear', '\clear']

def read_gemini_api_key():
    try:
        if 'GOOGLE_API_KEY' in os.environ:
            return os.environ['GOOGLE_API_KEY']
        return Path('key.txt').read_text().strip()
    except:
        return None

GOOGLE_API_KEY = read_gemini_api_key()
if GOOGLE_API_KEY is None:
    print("The API Key is not defined")
    print("Export GOOGLE_API_KEY variable and try again")
    exit()
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')
chat = model.start_chat(history=[])
console = Console()

def to_markdown(text):
  text = text.replace('•', '  *')
  md = Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  return md

while True:
    user_input = input('\> ')
    if user_input in exit_commands:
        exit()
    if user_input in clear_commands:
        os.system('clear')
        continue
    #response = model.generate_content(user_input, stream=True)
    response = chat.send_message(user_input)
    for chunk in response:
        # text color doesn't change because in to_markdown it's converted from
        # normal text to quote > text
        #style = Style(color="white", bold=True)
        style = Style(bgcolor="black", bold=True)
        console.print(to_markdown(chunk.text), style=style)
