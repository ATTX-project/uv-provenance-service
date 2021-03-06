import datetime
import json
import falcon
from uvprov_api.utils.logs import app_logger
from uvprov_api.uv.workflow_metadata import workflow_get_output


class Workflow(object):
    """Retrieve the latest workflow and associated datasets."""

    def on_get(self, req, resp):
        """Respond on GET request to map endpoint."""
        # modifiedSince = req.get_param('modifiedSince')
        data = workflow_get_output()
        # resp.body = json.dumps(data)
        # resp.content_type = 'application/json'
        result = self.format_response(data)
        if 'data' in result:
            resp.data = result['data']
            resp.content_type = 'application/json'
        else:
            resp.last_modifed = lambda x: result['modified'] if result['modified'] is not None else None
        resp.status = result["status"]
        app_logger.info('Finished operations on /workflow GET Request.')

    def format_response(self, data):
        """Create proper response based on format."""
        if data is 'Empty':
            return {"status": falcon.HTTP_204}
        elif data is not None:
            return {"status": falcon.HTTP_200, "data": json.dumps(data)}
        else:
            return {"status": falcon.HTTP_406, "modified": datetime.datetime.now()}
