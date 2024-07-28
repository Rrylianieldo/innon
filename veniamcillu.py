response = requests.get(url, headers=jira_headers, auth=(JIRA_USERNAME, JIRA_API_TOKEN), params=query)
