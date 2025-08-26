def normalize_address(addr: str) -> str:
    import re
    import unicodedata

    # Lowercase
    text = addr.lower()
    
    # Remove accents (México → Mexico)
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    
    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    
    # Expand common Mexican abbreviations
    replacements = {
        r"\bav\b": " avenida",
        r"\bavda\b": " avenida",
        r"\bblvd\b": " bulevar",
        r"\bcol\b": " colonia",
        r"\bfracc\b": " fraccionamiento",
        r"\bno\b": " numero",
        r"\bcd\b": " ciudad",
        r"\bcdmx\b": " ciudad de mexico",
        r"\bedo mex\b": " estado de mexico"
    }
    for k, v in replacements.items():
        text = re.sub(k, v, text)
    
    return text