#!/usr/bin/python3
"""Defines a script that lists 10 commits of a GitHub repository"""
import sys
import requests
from datetime import datetime


def display_gh_commits():
    """Displays 10 recent commits of a GitHub repository"""
    # Get repository name and owner of repository from the commandline
    repo, owner = sys.argv[1:]
    # Set up url from which to fecth the commits data
    gh_api_url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    # Send a GET request for commits to github api
    req = requests.get(gh_api_url)

    # Create an empty list to store data we want from commits
    commits_list = []
    # Iterate the commits list from the response
    for commit in req.json():
        # Store the desired data of a commit in a temporary dictionary
        temp_dict = {}
        temp_dict['sha'] = commit.get('sha')
        temp_dict['name'] = commit.get('commit')['author']['name']
        temp_dict['date'] = commit.get('commit')['author']['date']
        # Append the desired commit data to the list
        commits_list.append(temp_dict)

    # Sort the list of commits data extracted by date ascending
    commits_list.sort(
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ'),
        reverse=True
    )

    # Iterate through only 10 of the sorted commits data
    for commit in commits_list[:10]:
        # Display a commit's data in the format `sha: <author name>``
        print(commit['sha'] + ': ' + commit['name'])


if __name__ == '__main__':
    display_gh_commits()
