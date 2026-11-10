# investigator function
from agents.investigator_agent import investigate

# planner function
from agents.planner_agent import make_plan

# executor function
from agents.executor_agent import execute_plan

# main workflow
def run_sre_workflow(incident):

    # find root cause
    finding = investigate(incident)

    # create action plan
    plan = make_plan(finding["cause"])

    # execute fix
    result = execute_plan(plan)

    # return complete output
    return {

        # investigation result
        "finding": finding,

        # generated plan
        "plan": plan,

        # final execution result
        "result": result
    }
