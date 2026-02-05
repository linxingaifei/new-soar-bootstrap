import argparse

def parse_args():
    p = argparse.ArgumentParser(description="SOAR Edge Bootstrap")
    p.add_argument("--cloud", default="https://ctrl.soar.example.com")
    p.add_argument("--lang", choices=["zh", "en"], default="zh")
    p.add_argument("--dry-run", action="store_true",
                   help="Dry run mode, no real changes")
    return p.parse_args()
