import click, os
from flask import Flask, jsonify
from Libraries.filesDB import Database
from Libraries.listFilesClass import Files

app = Flask(__name__)

@app.route('/get_method/<int:timeFrame>')
def get_api(timeFrame):
    dbObj = Database(os.environ.get("MYSQL_DB"),os.environ.get("MYSQL_HOST"),os.environ.get("MYSQL_USER"),os.environ.get("MYSQL_PASSWORD"),os.environ.get("MYSQL_PORT"))
    getReturn = dbObj.get(timeFrame)

    return jsonify(getReturn)

@click.command()
@click.option('--path', type=click.Path(exists=True), help="Path to the input file or directory")
@click.option('--time_frame', type=int, help="Time in minutes")
@click.option('--str_to_find', help="String to find in a file")
@click.option('--str_to_replace', help="String to replace another string")

def main(path, time_frame, str_to_find, str_to_replace):
    fileObject = Files(path, time_frame)
    modifiedFiles = fileObject.get()

    #Add a loop for .update

    for file in modifiedFiles:
        filePath, searchStr, replaceStr, replacedTime = fileObject.update(file, str_to_find, str_to_replace)

        if replacedTime:
            dbObj = Database(os.environ.get("MYSQL_DB"),os.environ.get("MYSQL_HOST"),os.environ.get("MYSQL_USER"),os.environ.get("MYSQL_PASSWORD"),os.environ.get("MYSQL_PORT"))
            dbObj.add(filePath, searchStr, replaceStr, replacedTime)

if __name__ == "__main__":
    app.run(host=“0.0.0.0”, debug=True)
    main()
