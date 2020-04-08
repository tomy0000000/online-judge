class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        tmp = set()
        for each in emails:
            local = each[:each.find("@")]
            local = local.replace(".","")
            local = local[:local.find("+")]
        #     print(local)
            tmp.add(local+each[each.find("@"):])
        # print(len(list(tmp)))
        return len(list(tmp))
