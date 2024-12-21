import re


def find_ipv4_addresses(text):
    """Знаходить усі IPv4-адреси у тексті."""
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    potential_ips = re.findall(ipv4_pattern, text)
    valid_ips = [ip for ip in potential_ips if all(0 <= int(part) <= 255 for part in ip.split('.'))]
    return valid_ips


text = """
Here are some IP addresses:
Valid: 192.168.1.1, 8.8.8.8, 127.0.0.1
Invalid: 256.256.256.256, 123.456.78.90, 999.999.999.999
"""

found_ips = find_ipv4_addresses(text)
print("Знайдені IPv4-адреси:", found_ips)
