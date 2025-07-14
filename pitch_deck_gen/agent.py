from shared.protocols import Message
from shared.utils import generate_text
from business_plan_agent.agent import BusinessPlanAgent

class PitchDeckGeneratorAgent:
    def __init__(self, name="pitch_deck_generator"):
        self.name = name
        self.plan_agent = BusinessPlanAgent()

    def handle_request(self, message: Message):
        idea = message.content
        print("Requesting Business Plan from BusinessPlanAgent...")
        plan_msg = self.plan_agent.handle_request(
            Message(sender=self.name, receiver="business_plan_agent", content=idea)
        )

        print("Generating Pitch Deck...")
        prompt = f"""You are a startup consultant. Create a 10-slide pitch deck based on this business plan:
        {plan_msg.content}

        Each slide should include a title and 3-4 bullet points."""
        
        deck = generate_text(prompt)
        return Message(sender=self.name, receiver=message.sender, content=deck)
