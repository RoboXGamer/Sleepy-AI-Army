"""Defines the root agent (TaskPlannerAgent) for the Sleepy AI Army."""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# Import prompts and tools
from . import prompt
from .shared_tools import file_system

# Import sub-agents (placeholders for now, will be defined later)
# Assuming they will be defined in their respective agent.py files and exported via __init__.py
from .sub_agents.context_research import context_research_agent # Placeholder import
from .sub_agents.questions_and_answers import qna_agent # Placeholder import

# Define tools used by the TaskPlannerAgent
read_file_tool = FunctionTool(
    func=file_system.read_file
)

# Define the root agent (TaskPlannerAgent)
root_agent = Agent(
    model="gemini-2.0-flash", 
    name="TaskPlannerAgent",
    description=(
        "Acts as the entry point for processing a task. Reads the task status file "
        "and delegates control to the appropriate sub-agent (ContextResearchAgent or QnAAgent) "
        "or reports status to the user based on the content."
    ),
    instruction=prompt.TASK_PLANNER_AGENT_INSTRUCTIONS,
    tools=[read_file_tool],
    sub_agents=[
        context_research_agent, # Will handle initial context generation
        qna_agent               # Will handle Q&A iterations
    ]
)
