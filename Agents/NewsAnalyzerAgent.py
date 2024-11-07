from swarm import Swarm, Agent
from openai import OpenAI
import os

api_key = os.getenv('API_KEY')

client = OpenAI(
    api_key= api_key,
    base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",
)


swarm_agent = Swarm(client)
def transfer_to_agent_b():
    return agent_b

agent_a = Agent(
    model = "internlm2.5-latest",
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    model = "internlm2.5-latest",
    name="Agent B",
    instructions="Only speak in Haikus.",
)

response = swarm_agent.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "你好"}],
)

print(response.messages[-1]["content"])