# Let n be the length of emails.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def parse(self, email: str):
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        return f"{local}@{domain}"

    def numUniqueEmails(self, emails: list[str]) -> int:
        return len(set(map(self.parse, emails)))
