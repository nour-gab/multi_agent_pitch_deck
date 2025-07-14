from shared.protocols import Message
from shared.utils import generate_text
from market_research_agent.agent import MarketResearchAgent

class BusinessPlanAgent:
    def __init__(self, name="business_plan_agent"):
        self.name = name
        self.market_agent = MarketResearchAgent()

    def handle_request(self, message: Message):
        idea = message.content
        print("Sending idea to MarketResearchAgent...")
        market_analysis_msg = self.market_agent.handle_request(
            Message(sender=self.name, receiver="market_research_agent", content=idea)
        )

        print("Market Analysis Received. Generating Business Plan...")
        prompt = f"""Based on this business idea: {idea} and this market analysis: 
        {market_analysis_msg.content}, write a comprehensive business plan including:
        - Executive Summary
        - Market Analysis
        - Competitive Landscape
        - Business Model
        - Go-to-Market Strategy
        - Financial Projections"""

        plan = generate_text(prompt)
        return Message(sender=self.name, receiver=message.sender, content=plan)
