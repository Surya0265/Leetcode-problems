class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        if '.' in queryIP:
            parts=queryIP.split('.')
            if len(parts)!=4:
                 return "Neither"
            for part in parts:
                  if not part.isdigit():
                    return "Neither"
                  if not 0<=int(part)<=255:
                    return "Neither"
                  if part[0]=='0' and len(part)!=1:
                      return "Neither"
            return "IPv4"
        elif ':' in queryIP:
                hexadecimal="0123456789ABCDEFabcdef"
                parts=queryIP.split(':')
                if len(parts)!=8:
                 return "Neither"
                for part in parts:
                  if len(part)==0 or len(part)>4:
                    return "Neither"
                  for char in part:
                    if char not in hexadecimal:
                        return "Neither"
                
                return "IPv6"
        return "Neither"

                            