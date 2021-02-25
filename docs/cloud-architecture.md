# Cloud architecture

* Graphql-based backend in Hasura
  * Hasura exposes graphql schema based on db structure
  * schema is then riched with custom logic, for example audio file uploading
* Database in Yugabyte:
  * users
  * threads
  * messages
  * TODO: add db structure
* authorization in auth0:
  * user registers / logins against auth0 service, which sends mutation to Hasura and 
    returns Bearer token if successful
* file storage in Azure:
  * user sends file as base64 encoded via hasura
  * hasura sends file to azure
  * azure function takes file, processes it, saves file to s3 bucket, then sends 
    mutation to hasura to add file url to db
