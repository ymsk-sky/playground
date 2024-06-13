import mesop as me
import mesop.labs as mel

@me.page(path="/chat")
def app():
    mel.chat(transform=transform)

def transform(input: str, history: list[mel.ChatMessage]):
    yield "OK!"
