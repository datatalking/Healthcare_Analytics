import re

# TODO build extension to access index of past data imported
regex_patterns = {
    "names": r"[A-Za-z'-]+(?:\s[A-Za-z'-]+)*",
    "street addresses": r"\d{1,5}\s[A-Za-z]+\s[A-Za-z]+\s[A-Za-z]+",
    "telephone numbers": r"\d{3}-\d{3}-\d{4}",
    "fax numbers": r"\d{3}-\d{3}-\d{4}",
    "e-mail addresses": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}",
    "Social Security numbers": r"\d{3}-\d{2}-\d{4}",
    "medical records numbers": r"\d{8}",
    "health plan beneficiary numbers": r"\d{8}",
    "account numbers": r"\d{4}-\d{4}-\d{4}-\d{4}",
    "certificate license numbers": r"[A-Za-z0-9]{8,12}",
    "vehicle identifiers and serial numbers": r"[A-Z0-9]{17}",
    "device identifiers and serial numbers": r"[A-Za-z0-9]+",
    "URLs": r"https?://[A-Za-z0-9.-]+/[A-Za-z0-9.-]+",
    "IP address numbers": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
    "biometric identifiers": r"[A-Za-z0-9]+",
    "full face photos": r".*\.(jpg|jpeg|png|gif)",
}

# TODO look for other patterns than regex, NLP, NLTK, BERT
compiled_patterns = {
    key: re.compile(pattern) for key, pattern in regex_patterns.items()
}

# TODO create index of text containing the specified data
sample_text = """
Patient Name: John Doe
Address: 123 Main St, Anytown, USA
Phone: 555-555-5555
Email: johndoe@example.com
SSN: 123-45-6789
Medical Record Number: 98765432
Health Plan Beneficiary Number: 87654321
Account Number: 1234-5678-9012-3456
License Number: ABC12345678
Vehicle Identifier: ABCDEFGHIJKLMNOPQ1
Device Identifier: XYZ123
URL: http://example.com
IP Address: 192.168.1.1
Biometric Identifier: FingerPrint123
Photo: sample.jpg
"""

# TODO add elastic search for matches in the sample text
matches = {}
for key, pattern in compiled_patterns.items():
    match = pattern.search(sample_text)
    if match:
        matches[key] = match.group()

# TODO expand to display more than just the matched data
for key, value in matches.items():
    print(f"{key}: {value}")
