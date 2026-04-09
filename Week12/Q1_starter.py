# ============================================================
#  WEEK 12 LAB — Q1: SCANNER INHERITANCE
#  COMP2152 — Samuel Barth-Ibe
# ============================================================

import socket
import urllib.request


class Scanner:
    """Parent class — shared by all scanner types."""

    def __init__(self, target):
        self.target = target
        self.results = []

    # TODO: Write display_results(self)
    #   Print "Results for {self.target}:"
    #   If self.results is empty: print "  (no results)"
    #   Otherwise: print each result with "  " indent
    def display_results(self):
        print(f"Results for {self.target}:")
        if not self.results:
            print("  (no results)")
        else:
            for result in self.results:
                print(f"  {result}")


class PortScanner(Scanner):
    def __init__(self, target, ports):
        super().__init__(target)   # inherit from Scanner
        self.ports = ports

    def scan(self):
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                self.results.append(f"Port {port}: OPEN")
            else:
                self.results.append(f"Port {port}: CLOSED")
            sock.close()
        self.display_results()


class HTTPScanner(Scanner):
    def __init__(self, target, paths):
        super().__init__(target)   # inherit from Scanner
        self.paths = paths

    def scan(self):
        for path in self.paths:
            url = f"http://{self.target}{path}"
            try:
                response = urllib.request.urlopen(url, timeout=2)
                self.results.append(f"{path}: {response.status} OK")
            except urllib.error.HTTPError as e:
                self.results.append(f"{path}: {e.code} Error")
            except Exception:
                self.results.append(f"{path}: Unreachable")
        self.display_results()


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: SCANNER INHERITANCE")
    print("=" * 60)

    print("\n--- Port Scanner ---")
    ps = PortScanner("127.0.0.1", [22, 80, 443])
    print(f"  Scanning {ps.target} ports...")
    ps.scan()
    ps.display_results()

    print("\n--- HTTP Scanner ---")
    hs = HTTPScanner("127.0.0.1", ["/", "/admin", "/.git/config"])
    print(f"  Scanning {hs.target} paths...")
    hs.scan()
    hs.display_results()

    print("\n" + "=" * 60)
