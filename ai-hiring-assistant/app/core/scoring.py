from typing import Dict, List, Tuple
from .utils import tokenize, to_set
from app.core.utils import clean_text


def jaccard_similarity(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a.intersection(b))
    union = len(a.union(b))
    return inter / union if union else 0.0

def keyword_coverage(jd_tokens: List[str], resume_tokens: List[str]) -> float:
    jd_set = to_set(jd_tokens)
    res_set = to_set(resume_tokens)
    if not jd_set:
        return 0.0
    covered = len(jd_set.intersection(res_set))
    return covered / len(jd_set)

def score_resume(resume_text: str, job_desc_text: str) -> Dict:
    jd_tokens = tokenize(job_desc_text)
    res_tokens = tokenize(resume_text)

    jd_set = to_set(jd_tokens)
    res_set = to_set(res_tokens)

    sim = jaccard_similarity(jd_set, res_set)          # 0..1
    cov = keyword_coverage(jd_tokens, res_tokens)       # 0..1

    # weighted score (tunable)
    score = (0.6 * sim + 0.4 * cov) * 100.0

    # simple recommendation
    if score >= 70:
        verdict = "Strong match"
    elif score >= 50:
        verdict = "Moderate match"
    else:
        verdict = "Low match"

    matched_keywords = sorted(list(jd_set.intersection(res_set)))[:40]  # cap for UI

    return {
        "score": round(score, 1),
        "verdict": verdict,
        "matched_keywords": matched_keywords,
    }

def rank_resumes(resumes: List[Tuple[str, str]], job_desc_text: str) -> List[Dict]:
    """
    resumes: list of (filename, resume_text)
    returns list of dict with filename, score, verdict
    """
    results = []
    for filename, text in resumes:
        s = score_resume(text, job_desc_text)
        results.append({
            "filename": filename,
            "score": s["score"],
            "verdict": s["verdict"],
            "matched_keywords": ", ".join(s["matched_keywords"]),
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
