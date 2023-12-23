# Let n be the length of emails.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        s = set()
        for addr in emails:
            local, domain = addr.split("@")
            local = local.split("+")[0].replace(".", "")
            sanitized = f"{local}@{domain}"
            s.add(sanitized)
        return len(s)
