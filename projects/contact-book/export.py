import json
import csv
from contacts import load

def export_csv(filename="contacts.csv"):
    contacts = load()
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
        for name, info in sorted(contacts.items()):
            writer.writerow([name, info.get("phone", ""), info.get("email", "")])
    print(f"Exported {len(contacts)} contacts to {filename}")

def export_vcf(filename="contacts.vcf"):
    contacts = load()
    with open(filename, "w") as f:
        for name, info in contacts.items():
            f.write("BEGIN:VCARD\nVERSION:3.0\n")
            f.write(f"FN:{name}\n")
            if info.get("phone"):
                f.write(f"TEL:{info['phone']}\n")
            if info.get("email"):
                f.write(f"EMAIL:{info['email']}\n")
            f.write("END:VCARD\n")
    print(f"Exported {len(contacts)} contacts to {filename}")

if __name__ == "__main__":
    import sys
    fmt = sys.argv[1] if len(sys.argv) > 1 else "csv"
    if fmt == "vcf":
        export_vcf()
    else:
        export_csv()
