# Generates a Google Deployment Manager Configuration for a Cloud SQL instance with proxy user
# see cloudsql_db.py.schema for details

def GenerateConfig(context):
  """Generate configuration."""

  database_name = 'db---freiheit-' + context.env['name'] + str(context.env['current_time'])
  
  # Properties for the cloudSQL instance
  database = {
      'region': 'europe-west1',
      'databaseVersion': 'MYSQL_5_7',
      'settings': {
          'tier': 'db-n1-standard-1',
          'locationPreference': {
              'zone': context.properties['zone']
          },
          'activationPolicy': 'ALWAYS',
          'dataDiskSizeGb': '10',
      }
  }
  # Properties for the cloudSQL instance user
  dbuser = {
      'kind': 'sql#user',
      'name': 'cloudsqlproxy~%',
      'project': context.env['project'],
      'instance': '$(ref.' + context.properties['database_name'] + '.name)',
      'host': '%'
  }



  # Resources to return.
  resources = {
    'resources': [
      {
        'name': context.properties['database_name'],
        'type': 'sqladmin.v1beta4.instance',
        'properties': database
      },
      {
        'name': 'phoenix-cloudsqlproxy-user',
        'type': 'sqladmin.v1beta4.user',
        'properties': dbuser,
        'metadata': {
          'items': [
            {
              'dependsOn': [
                context.properties['database_name']
              ]
            }
          ]
        }
      }
    ]
  }

  return resources
