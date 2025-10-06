from crewai import Crew
from crew.developers.agent_developers import *
from crew.tasks.tasks_developers import *

crew_doc = Crew(
    agents=[editor_doc],
    tasks=[write_doc]
)

crew_test = Crew(
    agents=[tester],
    tasks=[write_tests]
)

crew_review = Crew(
    agents=[editor_review],
    tasks=[review]
)