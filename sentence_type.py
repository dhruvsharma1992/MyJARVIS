def get_sentence_type(text):
    if any(i in ['HOW','WHO','WHAT','WHEN'] for i in text):
        return 0
    if any(i in ['HOW','WHO','WHAT','WHEN'] for i in text):
        return 2
    return 1