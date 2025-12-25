from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def calculator(expression):
    """
    This calculator function solves any arithmetic expression containing all constant values.
    It supports basic arithmetic operators +, -, *, /, and parenthesis.
    :param expression: str input arithmetic expression
    :returns expression result as str
    """
    try:
        result = eval(expression)
        result_1 = str(result) + " call by tool"
        return result_1

    except:
        return "Error: Cannot solve expression"

#create llm
llm = init_chat_model(
    model = "google/gemma-3-4b",
    model_provider = "openai",
    base_url ="http://127.0.0.1:1234/v1",
    api_key ="not_needed"
)

#create agent
agent = create_agent(
    model = llm,
    tools =[ ],
    system_prompt="You are a helpful assistant. Answer in short."
)

while True:
    #take input
    user_input = input("You :")
    if user_input == "exit":
        break
    #invoke the agent
    result = agent.invoke({
        "messages" :
        {"role" : "user" , "content" : user_input}
    })

    llm_output = result["messages"][-1]
    print("AI : ", llm_output.content)