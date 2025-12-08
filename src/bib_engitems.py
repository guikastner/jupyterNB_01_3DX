import requests, json
from .credentials import creds



class EngItems:
    '''
    Docstring for EngItems
    '''

    def __init__(self):
        # reutiliza uma sessão autenticada (cookies/ticket) ou cria uma nova
        self.space_url = creds.space_url
        self.compass_url = creds.compass_url
        self.security_context = creds.role + "." + creds.company + "." + creds.collaborative_space
        self.engitems = creds.engitems
        self.engitemmask = "dsmveng:EngItemMask.Details"

    def getEngItemsDetails (self, session, id, mask=None):
        if mask is None:
            mask = "dsmveng:EngItemMask.Details"
        endpoint = self.space_url + self.engitems + "/dseng:EngItem/" + id + "?$mask=" + mask
        # print (endpoint)
        
        headers = {
            "SecurityContext": self.security_context,
            "Content-Type": "application/json"
        }
        # print(f"[engitems] headers: {headers}")

        response = session.get(endpoint, headers=headers, allow_redirects=True)
        # response = session.get(endpoint, headers={"SecurityContext": "VPLMProjectLeader.Company Name.Kastner - Workshop", "Content-Type": "application/json"}, allow_redirects=True)
        data = response.json()

        print("Physical Product Data:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

        return data
