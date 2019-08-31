class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            name, domain = email.split('@')
            if '+' in name:
                name = name[:name.index('+')]
            result.add(name.replace('.','') + '@' + domain)
        return(len(result))