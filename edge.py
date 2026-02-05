def apply_config(cfg, dry_run):
    if dry_run:
        print("[DRY-RUN] skip applying edge config")
        return
    print("[edge] apply config:", cfg)
