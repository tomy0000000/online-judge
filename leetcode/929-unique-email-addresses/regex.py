# Let n be the length of emails.
#
# Time: O(n)
# Space: O(n)

import re


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        s = set()
        matcher = re.compile(
            r"^(?P<local>[\w\.]+)(\+[\w\.]+)*@(?P<domain>[\w\.\+]+\.com)$"
        )
        for addr in emails:
            match = matcher.match(addr)
            local, _, domain = match.groups()
            sanitized = f"{local.replace('.', '')}@{domain}"
            s.add(sanitized)
        return len(s)
