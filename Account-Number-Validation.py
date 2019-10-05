def process(line: str) -> str:
    import string
    # Return 'VALID' or 'INVALID'
    
    if not (all(c in string.hexdigits for c in line)):
        return "INVALID"
   
    checksum = int(line[:2], 16)
    ac_no = int(line[2:], 16)
    
    ac_no_list = [int(d) for d in str(ac_no)]
    ac_no_sum = sum(ac_no_list)
    
    if checksum == ac_no_sum:
        return 'VALID'
    else:
        return 'INVALID'
    