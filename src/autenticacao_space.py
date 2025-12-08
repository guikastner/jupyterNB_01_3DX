import requests, json, base64
from .credentials import creds


class AutenticacaoSpace:
    def __init__(self):
        self.user = creds.user
        self.password = creds.password
        self.passport_URL = creds.passport_url
        self.space_URL = creds.space_url
        self.tenant = creds.tenant
    def get_login_session(self): 
        """Perform CAS login using a persistant session object.
        1. Create session
        2. Get login ticket
        3. Login using username / password
        4. Return session object, will be used in subsequent calls (holds cookies etc)
        """

        session = requests.Session()
        
        # Get login ticket
        url = self.passport_URL + '/login?action=get_auth_params'
        print('Requesting login ticket...')
        response = session.get(url, verify=True)
        print(f"Ticket request status: {response.status_code}")
        response.raise_for_status()

        # Full JSON returned by the ticket endpoint
        ticket_payload = response.json()
        # print("Ticket response JSON:")
        # print(json.dumps(ticket_payload, indent=2, ensure_ascii=False))

        login_ticket = str(ticket_payload['lt'])

        # CAS authentication
        # url = self.passport_URL + '/login'
        url = self.passport_URL + "/login?service="+ self.space_URL +"/resources/modeler/pno/person?current=true%26tenant="+ self.tenant + "%26select=collabspaces%26select=preferredcredentials"
        # print(url)
        data = 'lt=' + login_ticket + '&username=' + self.user + '&password=' + self.password + '&rememberMe=no'
        headers = {
            'tenant': self.tenant,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        print(headers)
        print('Authenticating using CAS...')
        response = session.post(url, headers=headers, data=data, verify=True)
        print(f"CAS auth status: {response.status_code}")

        auth_payload = response.json()
        # print("Ticket response JSON:")
        # print(json.dumps(auth_payload, indent=2, ensure_ascii=False))

        # Return both the JSON ticket payload and the active session
        return ticket_payload, session
