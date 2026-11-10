# create plan
def make_plan(cause):

    # check cause
    if cause == "OOM":

        # return fix plan
        return {

            # action plan
            "plan": "Increase Memory",

            # risk level
            "risk": "LOW"
        }

    # unknown issue
    return {

        # action
        "plan": "Escalate",

        # high risk
        "risk": "HIGH"
    }
