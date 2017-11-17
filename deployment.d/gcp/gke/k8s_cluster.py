# Google Deployment-Manager template for creation of kubernetes clusters.
#
# see ./k8s_cluster.schema for details.


def GenerateConfig(context):
    return {
        'resources': [
            {
                'name': context.properties['cluster_name'],
                'type': 'container.v1.cluster',
                'properties': {
                    'zone': context.properties['zone'],
                    'cluster': {
                        'name': context.properties['cluster_name'],
                        'description': context.properties['description'],
                        'initialNodeCount': 1,
                        'network': context.properties['network'],
                        'subnetwork': context.properties['subnetwork'],
                        'nodeConfig': {
                            'machineType': context.properties['machine_type'],
                            'imageType': 'cos'
                        }
                    }
                }
            }
        ]
    }

