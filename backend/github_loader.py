import requests

username = "kuldeep0009-hub"

repos = requests.get(
    f"https://api.github.com/users/{username}/repos"
).json()

for repo in repos:

    repo_name = repo["name"]

    print(f"Downloading {repo_name}")

    readme_url = f"https://raw.githubusercontent.com/{username}/{repo_name}/main/README.md"

    response = requests.get(readme_url)

    if response.status_code == 200:

        with open(
            f"../data/github/{repo_name}.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(response.text)