import requests

username = "AshishMittal33"

repos = requests.get(
    f"https://api.github.com/users/{username}/repos"
).json()

with open("../data/github/repos.txt", "w", encoding="utf-8") as f:

    for repo in repos:
        f.write(f"Repository: {repo['name']}\n")
        f.write(f"Description: {repo.get('description')}\n\n")

print("Saved")