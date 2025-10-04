from crewai import Crew
from crew.developers.agent_developers import *
from crew.tasks.tasks_developers import *

crew = Crew(
    agents=[editor_doc, tester, editor_review],
    tasks=[write_doc, write_tests, review]
)
