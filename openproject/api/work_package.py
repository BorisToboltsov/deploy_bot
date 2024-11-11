import json

from openproject.api.requests import DbRequests


class ApiWorkPackage:
    def __init__(self):
        self.db_requests = DbRequests()

    async def get_work_package_by_user(self, openproject_user_id: int) -> dict:
        """
        :param user_id:
        :return:
        """
        value = [{ "assignee": { "operator": "=", "values": f"{openproject_user_id}" }}, {"status": { "operator": "=", "values": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "13"]}}]
        parameters = {"filters": f'{json.dumps(value)}'}
        response = await self.db_requests.get(parameters)

        return response
