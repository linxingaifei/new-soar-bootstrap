import requests

def register(cloud_url, dry_run):
    print("[cloud] register:", cloud_url)
    if dry_run:
        return {"token": "dry-token"}
    return {"token": "prod-token"}

def pull_config(cloud_url, token, dry_run):
    print("[cloud] pull config")
    if dry_run:
        return {"wan": "dhcp"}
    return {"wan": "dhcp"}
