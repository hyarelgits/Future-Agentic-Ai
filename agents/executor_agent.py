# execute remediation plan
def execute_plan(plan):

    # check risk level
    if plan["risk"] == "HIGH":

        # escalate to human
        return {

            # result status
            "status": "ESCALATED"
        }

    # execute fix
    return {

        # success status
        "status": "FIXED"
    }
