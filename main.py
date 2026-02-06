def print_banner():
    print("=" * 60)
    print("SOAR Cloud-Managed Edge Router Bootstrap Tool")
    print("SOAR 云管路由系统 · Edge 初始化工具")
    print("-" * 60)
    print("Mode      : Bootstrap / One-time Execution")
    print("Security  : No Backdoor · Least Privilege")
    print("Control   : HTTPS (Edge → Cloud)")
    print("Target    : VyOS Edge Device")
    print("=" * 60)
    print()

print_banner()

from config import parse_args
from i18n import init, t
import cloud
import edge

def main():
    args = parse_args()
    init(args.lang)

    print(t("开始执行 Bootstrap", "Starting bootstrap"))

    if args.dry_run:
        print("[MODE] DRY-RUN")
    else:
        print("[MODE] PRODUCTION")

    reg = cloud.register(args.cloud, args.dry_run)
    token = reg["token"]

    cfg = cloud.pull_config(args.cloud, token, args.dry_run)
    edge.apply_config(cfg, args.dry_run)

    print(t("Bootstrap 完成，可以安全退出",
            "Bootstrap finished successfully"))

if __name__ == "__main__":
    main()
