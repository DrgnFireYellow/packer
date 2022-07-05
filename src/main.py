import os

import requests
import rich
import typer
import pathlib

app = typer.Typer()


@app.command()
def get(owner: str, repo: str, packet: str):
    rich.print("[yellow]Fetching packet...")
    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/content/{packet}")
    packet_json = r.json()
    PACKET_LOCATION = f"{pathlib.Path().home}/.packer/{packet}"
    os.mkdir(PACKET_LOCATION)
    for i in packet_json:
        if i["name"] != "bin":
            with open(f"{PACKET_LOCATION}/{i['path']}", 'x') as f:
                f.write(requests.get(i["download_url"]).content)
        else:
            



if __name__ == "__main__":
    app()
