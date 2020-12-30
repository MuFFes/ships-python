def character_limit(entry_text, limit):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:limit])
