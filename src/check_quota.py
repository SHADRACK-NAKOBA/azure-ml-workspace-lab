"""Check whether you have enough Azure ML vCPU quota for the lab's VM size.

Usage (Cloud Shell, inside the repo, with the virtual environment active):
    python src/check_quota.py
    python src/check_quota.py --vm-size Standard_DS2_v2
"""
import argparse

from workspace import get_ml_client


def _name(usage) -> str:
    n = usage.name
    return getattr(n, "value", None) or str(n or "")


def _label(usage) -> str:
    n = usage.name
    return getattr(n, "localized_value", None) or _name(usage)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vm-size", default="Standard_DS3_v2")
    args = parser.parse_args()

    ml_client = get_ml_client()
    location = ml_client.location

    sizes = {(s.name or "").lower(): s for s in ml_client.compute.list_sizes(location=location)}
    size = sizes.get(args.vm_size.lower())
    if size is None:
        print(f"{args.vm_size} is not offered in {location}. Pick another size or region.")
        return
    family = str(size.family or "")
    vcpus = getattr(size, "v_cp_us", None) or getattr(size, "v_cpus", None) or 0
    print(f"{args.vm_size}: {vcpus} vCPUs, family '{family}'")

    # Prefer the subscription-level VM family quota; fall back to any entry with that name.
    matches = [u for u in ml_client.compute.list_usage(location=location)
               if _name(u).lower() == family.lower()]
    matches.sort(key=lambda u: 0 if "vmfamily" in str(u.type or "").lower() else 1)
    if not matches:
        print(f"No quota entry found for family '{family}' in {location}. "
              f"Check Studio > Manage > Compute > Quota.")
        return

    usage = matches[0]
    used, limit = int(usage.current_value or 0), int(usage.limit or 0)
    free = limit - used
    print(f"Quota '{_label(usage)}' in {location}: {used} used of {limit} -> {free} free")
    if free >= vcpus:
        print(f"OK - enough quota to run the AutoML job on {args.vm_size}.")
    else:
        print(f"NOT ENOUGH - need {vcpus} free vCPUs. Try another size, e.g.\n"
              f"    python src/check_quota.py --vm-size Standard_DS2_v2\n"
              f"or request more quota (see docs/09-troubleshooting.md, E7).")


if __name__ == "__main__":
    main()
