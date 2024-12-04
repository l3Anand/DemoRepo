from phi.agent import Agent, RunResponse
from phi.model.groq import Groq

agent = Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview",api_key="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"),
    markdown=True
)
# Print the response in the terminal
agent.print_response("Suggest some powerfull laptop")
