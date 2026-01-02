class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start: int, path: List[str]):
            # If we have 4 parts and used all characters
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            
            # Prune if too many or too few characters left
            remaining_chars = len(s) - start
            remaining_parts = 4 - len(path)
            if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start:start + length]

                # No leading zeros unless the segment is "0"
                if segment[0] == '0' and length > 1:
                    continue

                # Segment value must be <= 255
                if int(segment) <= 255:
                    backtrack(start + length, path + [segment])

        backtrack(0, [])
        return result
