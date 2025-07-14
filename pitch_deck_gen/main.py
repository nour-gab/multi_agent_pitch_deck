from agent import PitchDeckGeneratorAgent
from shared.protocols import Message

agent = PitchDeckGeneratorAgent()
idea = "AI-powered noise monitoring for smart cities"
response = agent.handle_request(Message("main", "pitch_deck_generator", idea))
print("Final Pitch Deck:\n", response.content)
