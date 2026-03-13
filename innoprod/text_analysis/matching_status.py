from enum import StrEnum

class MatchingStatus(StrEnum):
    UNVERIFIED = 'Match that needs verification'
    NO_MATCH = 'No match'
    VERIFIED = 'Verified match'
    INCORRECT = 'Match that has been found to be incorrect during verification'
    BROKEN = 'Match that was verified but is now broken'
    

initial_map = {
    True: MatchingStatus.UNVERIFIED,
    False: MatchingStatus.NO_MATCH
}

def update_status(current_status, new_match):
    if current_status == MatchingStatus.UNVERIFIED:
        return current_status
    
    if current_status == MatchingStatus.NO_MATCH:
        if new_match:
            return MatchingStatus.UNVERIFIED
        else:
            return current_status
    
    if current_status == MatchingStatus.VERIFIED:
        if new_match:
            return current_status
        else:
            return MatchingStatus.BROKEN
    
    if current_status == MatchingStatus.INCORRECT:
        if new_match:
            return current_status
        else:
            return MatchingStatus.VERIFIED
        
    if current_status == MatchingStatus.BROKEN:
        if new_match:
            return MatchingStatus.VERIFIED
        else:
            return current_status
