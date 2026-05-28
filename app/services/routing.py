LANE_KEYWORDS = {
    "SBIR/STTR": ["sbir", "sttr", "research", "innovation", "phase i", "phase ii"],
    "OTA": ["ota", "prototype", "other transaction"],
    "Grant Operations": ["grant", "deadline", "funding", "award"],
    "EV / Infrastructure": ["ev", "charging", "nevi", "transportation", "infrastructure"],
    "Healthcare Access": ["health", "clinic", "provider", "credentialing", "practolytics"],
    "Micro-Community": ["food", "childcare", "housing", "workforce", "community"],
}


def classify_lane(text: str, default: str = "General Operations") -> str:
    """Public reference classifier. Proprietary Sentinel routing logic is excluded."""
    normalized = text.lower()
    for lane, keywords in LANE_KEYWORDS.items():
        if any(keyword in normalized for keyword in keywords):
            return lane
    return default
