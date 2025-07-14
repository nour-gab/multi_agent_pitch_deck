from agent import BusinessPlanAgent
from shared.protocols import Message

agent = BusinessPlanAgent()
idea = "AI-powered noise monitoring for smart cities"
response = agent.handle_request(Message("main", "business_plan_agent", idea))
print("Business Plan:\n", response.content)
