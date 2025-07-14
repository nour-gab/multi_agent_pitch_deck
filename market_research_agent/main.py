from agent import MarketResearchAgent
from shared.protocols import Message

agent = MarketResearchAgent()
idea = "AI-powered noise monitoring for smart cities"
response = agent.handle_request(Message("main", "market_agent", idea))
print("Market Research:\n", response.content)
