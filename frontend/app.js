// function executes on button click
async function fixIssue() {

    // get incident text
    const incident =
        document.getElementById("incident").value;

    // call FastAPI
    const response =
        await fetch(
            "http://localhost:8002/fix-incident",
            {

                // HTTP method
                method: "POST",

                // JSON content
                headers: {
                    "Content-Type":"application/json"
                },

                // request body
                body: JSON.stringify({
                    incident: incident
                })
            }
        );

    // convert json
    const data =
        await response.json();

    // show output
    document.getElementById("result").innerText =
        JSON.stringify(data,null,2);
}
