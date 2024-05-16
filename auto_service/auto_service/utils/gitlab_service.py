import requests


def get_all_items\
        (private_token,
        gitlab_domain='https://gitlab.licelus.com',
        gitlab_project_id='129',
        branch='master',
        path='downloads', per_page=5000, start_page=1) -> list:

    headers = {"PRIVATE-TOKEN": f"{private_token}"}
    url = f"{gitlab_domain}/api/v4/projects/{gitlab_project_id}/repository/tree"
    params = {
        "ref": branch,
        "path": path,
        "per_page": per_page,
        "page": start_page
    }
    gitlab_response = requests.get(url, params=params, headers=headers)
    files = gitlab_response.json()

    if not files:
        pass
    else:
        return files
