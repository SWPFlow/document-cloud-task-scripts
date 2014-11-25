"""
file: doc-put-title.py
what: updates the title for a series of documents in a project
uses: http://datadesk.github.com/python-documentcloud/

"""
# import the modules for this script
from documentcloud import DocumentCloud
from ConfigFile import config_settings

# varible to hold the project we're targeting
MY_PROJECT_ID = 123345

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

# begin function to update document metadata
def update_document_title(project_id, new_title):

    # creates an object that contains the documents in the project
    project_object = client.projects.get(id=project_id)

    # list to hold all of the documents ids
    list_of_documents = project_object.document_ids

    # begin looping through each document in our list
    for document in list_of_project_documents:

        # get an invidual document
        obj = client.documents.get(document)

        # add the new description
        obj.title = new_title

        # commit the change
        obj.put()

        print "%s updated" % (obj)

    # end group of entities for document
    print "Finished updating metadata"

if __name__ == "__main__":
    update_document_title(MY_PROJECT_ID, "#")