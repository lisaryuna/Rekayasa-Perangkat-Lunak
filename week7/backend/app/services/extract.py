import re

def extract_action_items(text: str) -> list[str]:
    patterns = [
        re.compile(r'(?i)TODO:.*'),
        re.compile(r'(?i)Action Item:.*'),
        re.compile(r'(?i)Action:.*'),
        re.compile(r'^\s*[-*]\s*\[ \]\s*.*'),
    ]
    
    results: list[str] = []
    for line in text.splitlines():
        line_stripped = line.strip()
        if not line_stripped:
            continue
        clean_line = re.sub(r'^[-*]\s+', '', line_stripped)
        
        matched = False
        for pattern in patterns:
            if pattern.search(line_stripped):
                results.append(clean_line)
                matched = True
                break
        
        if not matched and line_stripped.endswith('!'):
            results.append(clean_line) 
    return results