from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("provision.html", title="Provision", active="provision")

@app.route('/provision', methods=["GET", "POST"])
def provision():
    if request.method == "POST":
        vm_name = request.form["vm_name"]
        cpu = int(request.form["cpu"])
        memory = int(request.form["memory"])

        # Backend validation (security check)
        if cpu < 1 or cpu > 8:
            return f"Invalid CPU count: {cpu}. Must be between 1 and 8."
        if memory < 512 or memory > 16384:
            return f"Invalid memory: {memory} MB. Must be between 512 and 16384 MB."

        # If valid, continue with provisioning
        return f"Provision request sent for {vm_name} ({cpu} CPU, {memory} MB RAM)"

    return render_template("provision.html", title="Provision", active="provision")


@app.route('/revert', methods=["GET", "POST"])
def revert():
    if request.method == "POST":
        vm_id = request.form["vm_id"]
        return f"Revert request sent for VM {vm_id}"
    return render_template("revert.html", title="Revert", active="revert")

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        vm_id = request.form["vm_id"]
        return f"Delete request sent for VM {vm_id}"
    return render_template("delete.html", title="Delete", active="delete")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)