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
        "shaw-latency-research-lab",
        "market-microstructure-research-platform",
        "fpga-trading-system-soc",
        "ai-quant-research-os",
        "hardware-software-co-design-lab",
        "deeplob-reproduction-lab",
        "hlob-feature-research",
        "optimal-execution-rl-lab",
        "fpga-feed-handler-paper-reproduction",
        "ptp-hardware-timestamping-reproduction",
        "abides-market-sim-lab",
        "lobframe-benchmark-suite",
        "option-vol-surface-lab",
        "gamma-exposure-estimator",
        "smartnic-packet-classifier",
        "symbiyosys-formal-risk-gates",
        "hls-vs-rtl-latency-lab",
        "paper-to-code-research-agent",
        "market-impact-propagator-lab",
        "neural-lob-transformer-lab",
        "graph-lob-gnn-lab",
        "neural-hedging-risk-lab",
        "volatility-regime-hmm-lab",
        "kalman-market-state-space-lab",
        "cointegration-stat-arb-lab",
        "convex-portfolio-optimizer-lab",
        "p4-market-data-router-lab",
        "riscv-vector-market-accelerator",
        "tinyml-industrial-anomaly-lab",
        "causal-event-study-lab",
        "differentiable-backtester-lab",
        "bayesian-strategy-optimizer",
        "contextual-bandit-trading-lab",
        "rough-volatility-simulator",
        "avellaneda-stoikov-mm-lab",
        "portfolio-stress-var-lab",
        "distributed-orderbook-consensus-lab",
        "zero-trust-trading-audit-lab",
        "time-sync-attack-simulator",
        "hawkes-order-flow-lab",
        "copula-tail-risk-lab",
        "optimal-transport-portfolio-lab",
        "jump-diffusion-options-lab",
        "liquidity-fragility-stress-lab",
        "fpga-axi-stream-verifier",
        "fpga-cdc-metastability-lab",
        "ptp-servo-controller-lab",
        "ebpf-market-telemetry-lab",
        "wasm-strategy-sandbox",
        "kernel-bypass-feed-latency-lab",
        "fpga-low-latency-market-data-engine",
        "fpga-nanosecond-orderbook-risk-gate",
        "fpga-udp-market-data-feed-handler",
        "fpga-latency-arbitration-crossbar",
        "fpga-pcie-market-data-dma-engine",
        "shaw-alpha-lab",
        "options-ev-estimator",
        "agentic-quant-researcher",
        "latency-budget-workbench",
        "market-microstructure-lab",
        "strategy-survivorship-analyzer",
        "fixed-point-finance-lab",
        "deterministic-trading-state-machine",
        "risk-gate-co-simulation-lab",
        "repo-context-engineer",
        "obsidian-trading-memory-sync",
        "ai-runbook-operator",
        "esp32-market-alert-display",
        "sensor-fusion-risk-monitor",
        "fpga-fix-protocol-parser",
        "fpga-lob-reconstruction-engine",
        "fpga-hardware-timestamping-core",
        "market-data-line-rate-simulator",
        "execution-router-simulator",
        "cyber-physical-threat-models",
        "real-time-scheduler-lab",
        "udp-telemetry-control-plane",
        "edge-device-health-monitor",
        "industrial-control-sim-lab",
        "financial-report-summarizer",
        "market-news-signal-ranker",
        "ai-dashboard-commentary-engine",
        "prompt-eval-lab",
        "llm-trading-guardrails",
        "distributed-clock-sync-lab",
        "embedded-signal-processing-lab",
        "operator-console-design-system",
        "event-driven-alpha-pipeline",
        "market-replay-hardware-harness",
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


def test_homepage_features_verified_fpga_portfolio() -> None:
    html = read(ROOT / "index.html")
    assert "FPGA and Low-Latency Hardware Portfolio" in html
    assert "CI verification" in html
    assert "without unmeasured timing claims" in html
    assert "fpga-low-latency-market-data-engine" in html
    assert "fpga-nanosecond-orderbook-risk-gate" in html
    assert "fpga-udp-market-data-feed-handler" in html
    assert "fpga-latency-arbitration-crossbar" in html


def test_profile_mark_and_contact_are_present() -> None:
    assert (ROOT / "assets" / "profile-mark.svg").exists()
    assert (ROOT / "assets" / "shawsignaldev-avatar.png").exists()
    assert "shawsignaldev@proton.me" in read(ROOT / "index.html")


def test_public_site_avoids_sensitive_language() -> None:
    forbidden = ["api key", "secret key", "password", "private key", "broker credential"]
    combined = "\n".join(read(page).lower() for page in PAGES)
    for phrase in forbidden:
        assert phrase not in combined


def test_public_site_avoids_unverified_hardware_claims() -> None:
    forbidden = ["timing closed", "fmax", "post-route", "board deployed", "measured vivado"]
    combined = "\n".join(read(page).lower() for page in PAGES)
    for phrase in forbidden:
        assert phrase not in combined
