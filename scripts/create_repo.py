#!/usr/bin/env python3
"""
Create a GitHub repository using the REST API.

Usage:
  python scripts/create_repo.py --name my-repo --private --description "..." [--org ORG]

Requires the environment variable `GITHUB_TOKEN` with repo/create scope.

This script deliberately avoids extra third-party dependencies and
uses the standard library for HTTP requests.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
import urllib.error


def create_repo(token: str, name: str, private: bool, description: str | None, org: str | None) -> dict:
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "github-starter-create-repo-script",
    }

    payload = {
        "name": name,
        "private": private,
    }
    if description:
        payload["description"] = description

    data = json.dumps(payload).encode("utf-8")

    if org:
        url = f"https://api.github.com/orgs/{org}/repos"
    else:
        url = "https://api.github.com/user/repos"

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        raise SystemExit(f"GitHub API error {e.code}: {body}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create a GitHub repository from the command line.")
    parser.add_argument("--name", required=True, help="Repository name")
    parser.add_argument("--private", action="store_true", help="Make the repo private")
    parser.add_argument("--description", help="Repository description")
    parser.add_argument("--org", help="Organization name (create under org instead of user)")

    args = parser.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: set GITHUB_TOKEN environment variable with a token that has repo/create rights.")
        return 2

    result = create_repo(token, args.name, args.private, args.description, args.org)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
