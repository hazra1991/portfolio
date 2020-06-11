from flask import render_template,Flask,request
import json,os,logging

logging.basicConfig(filename="./app_logs/app.logs", filemode="a+", level=logging.ERROR)
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/timeline/")
def timeline():
    try:
        timeline = load_json_data("timeline.json")["timeline"]
        return render_template("timeline.html", timeline=timeline)
    except TypeError:
        return render_template("timeline.html")

@app.route("/projects/")
def projects():
    try:
        data = load_json_data("projects.json")["projects"]

        if request.args:
            # logging.error(request.args["value"],data[0]["link_id"])
            project_data = next((x for x in data if "link_id" in x and x["link_id"] == request.args["value"]),None)
            if project_data is not None:
                return render_template("project.html", project=project_data)
        return render_template("projects.html", projects=data)
    except TypeError:
        return render_template("projects.html", no_data="No data available")


@app.route("/Download_cv/")
def download_cv():
    return "Page under construction"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def load_json_data(filename):
    try:
        json_data = json.load(open(get_file_path(filename),"r"))
        return json_data
    except FileNotFoundError:
        logging.error("The file {} not found".format(filename))
    except json.decoder.JSONDecodeError:
        logging.error("wrong json data format in the file {} please correct the same".format(filename))


def get_file_path(file):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_dir,"json_data_file/{}".format(file))
    return file_path



if __name__ == "__main__":
    app.run(debug=True)