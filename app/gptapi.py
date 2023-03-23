import openai
import uuid
# openai的api——
api_key=''

def askgpt(content:str, session_id:str,state):
    global message
    openai.api_key = api_key
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "assistant", "content": content}],
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        user=session_id,
    )
    return res.choices[0].message.content
def ask(problem:str)->str:
    session_id = str(uuid.uuid4())
    state = None
    print("你在询问的问题"+problem)
    content =problem+ ",写的尽量详细一些"
    x=askgpt(content, session_id, state)
    print("一个问题回答完毕")
    return x