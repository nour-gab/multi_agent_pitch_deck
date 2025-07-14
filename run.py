# run.py

from shared.protocols import Message
from market_research_agent.agent import MarketResearchAgent
from business_plan_agent.agent import BusinessPlanAgent
from pitch_deck_gen.agent import PitchDeckGeneratorAgent

def run_agents_pipeline(business_idea: str):
    print("\nSTARTING MULTI-AGENT PIPELINE USING A2A PROTOCOL\n")

    # Step 1: Market Research Agent
    market_agent = MarketResearchAgent()
    market_request = Message(sender="run_pipeline", receiver="market_research_agent", content=business_idea)
    market_response = market_agent.handle_request(market_request)
    print("Market Research Output:\n", market_response.content[:500], "...\n")  # Truncated

    # Step 2: Business Plan Agent
    business_agent = BusinessPlanAgent()
    business_request = Message(sender="run_pipeline", receiver="business_plan_agent", content=business_idea)
    business_response = business_agent.handle_request(business_request)
    print("Business Plan Output:\n", business_response.content[:500], "...\n")

    # Step 3: Pitch Deck Generator Agent
    pitch_agent = PitchDeckGeneratorAgent()
    pitch_request = Message(sender="run_pipeline", receiver="pitch_deck_generator", content=business_idea)
    pitch_response = pitch_agent.handle_request(pitch_request)
    print("Final Pitch Deck:\n", pitch_response.content)

    return {
        "market_research": market_response.content,
        "business_plan": business_response.content,
        "pitch_deck": pitch_response.content
    }

if __name__ == "__main__":
    idea = "AI-powered noise monitoring for smart cities"
    results = run_agents_pipeline(idea)
