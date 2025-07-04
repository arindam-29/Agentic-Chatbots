from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot loing Implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State) -> dict:
        """
        Process the input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state["messages"])}