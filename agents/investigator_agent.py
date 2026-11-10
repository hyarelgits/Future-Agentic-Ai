# import CrewAI agent
from crewai import Agent

# create investigator agent
investigator = Agent(

    # agent role
    role="SRE Investigator",

    # agent objective
    goal="Find root cause",

    # background information
    backstory="Expert SRE engineer",

    # print reasoning
    verbose=True
)


# investigate incident
def investigate(incident):

    # check incident text
    if "CrashLoopBackOff" in incident:

        # root cause discovered
        return {

            # root cause
            "cause": "OOM",

            # recommendation
            "hint": "Check memory usage"
        }

    # unknown incident
    return {

        # cause not found
        "cause": "Unknown",

        # generic recommendation
        "hint": "Check logs"
    }
