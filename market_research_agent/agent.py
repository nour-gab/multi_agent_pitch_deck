from shared.protocols import Message
from shared.utils import generate_text

class MarketResearchAgent:
    def __init__(self, name="market_research_agent"):
        self.name = name

    def handle_request(self, message: Message):
        idea = message.content
        prompt = f"Do a quick market analysis on this idea: {idea}. Include competitors, market demand, and trends."
        research = generate_text(prompt)
        return Message(sender=self.name, receiver=message.sender, content=research)
