from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ROOT / "index.html",
    ROOT / "projects.html",
    ROOT / "review-guide.html",
    ROOT / "technical-depth.html",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_pages_exist_and_have_site_navigation() -> None:
    for page in PAGES:
        html = read(page)
        assert "Ephraim Shaw" in html
        assert "projects.html" in html
        assert "technical-depth.html" in html
        assert "review-guide.html" in html
        assert "github.com/shawsignaldev" in html


def test_project_catalog_includes_core_repositories() -> None:
    html = read(ROOT / "projects.html")
    expected = [
        "argus",
        "cipher",
        "ares",
        "oracle",
        "deploq",
        "aurora-market-network-explorer",
        "market-data-ingestion-lab",
        "cpse-engineering-labs",
        "eidenhall",
        "m2m-learning-systems",
    ]
    for repo in expected:
        assert f"github.com/shawsignaldev/{repo}" in html


def test_profile_mark_and_contact_are_present() -> None:
    assert (ROOT / "assets" / "profile-mark.svg").exists()
    assert (ROOT / "assets" / "shawsignaldev-avatar.png").exists()
    assert "shawsignaldev@proton.me" in read(ROOT / "index.html")


def test_public_site_avoids_sensitive_language() -> None:
    forbidden = ["api key", "secret key", "password", "private key", "broker credential"]
    combined = "\n".join(read(page).lower() for page in PAGES)
    for phrase in forbidden:
        assert phrase not in combined
