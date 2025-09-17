from flask import Flask, render_template, request

app = Flask(__name__)

# Mock provisioning function
def provision_resources(name, resource_type, quantity):
    # Here you would call APIs or scripts to provision resources
    return f"Provisioned {quantity} {resource_type}(s) for {name}!"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        name = request.form.get("name")
        resource_type = request.form.get("resource_type")
        quantity = request.form.get("quantity")
        result = provision_resources(name, resource_type, quantity)
    return render_template("form.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)