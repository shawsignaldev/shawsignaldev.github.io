from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ROOT / "index.html",
    ROOT / "projects.html",
    ROOT / "papers.html",
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
        "research-queue-state-machine",
        "hardware-software-co-design-lab",
        "deeplob-reproduction-lab",
        "deeplob-leakage-test-harness",
        "hlob-depth-persistence-study",
        "lobench-representation-lab",
        "lob-bench-generative-evaluator",
        "abides-agent-strategy-zoo",
        "hlob-feature-research",
        "optimal-execution-rl-lab",
        "fpga-feed-handler-paper-reproduction",
        "ptp-hardware-timestamping-reproduction",
        "abides-market-sim-lab",
        "market-sim-scenario-library",
        "lobframe-metric-dashboard",
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
        "auction-imbalance-alpha-lab",
        "adaptive-order-slicing-lab",
        "synthetic-market-data-generator",
        "causal-graph-market-lab",
        "explainable-alpha-attribution-lab",
        "trade-surveillance-rules-lab",
        "fpga-fifo-depth-planner",
        "hardware-cache-coherence-lab",
        "market-data-schema-contracts",
        "incident-response-runbook-engine",
        "cross-venue-latency-arbitrage-lab",
        "options-market-maker-greeks-lab",
        "volatility-surface-arbitrage-detector",
        "market-data-reconciliation-engine",
        "deterministic-replay-debugger",
        "pcie-descriptor-ring-simulator",
        "fpga-packet-checksum-offload",
        "feature-store-point-in-time-lab",
        "model-risk-validation-lab",
        "research-lineage-ledger",
        "tick-data-lakehouse-simulator",
        "event-sourced-market-feed-pipeline",
        "backtest-result-warehouse",
        "alert-event-bus-adapters",
        "reproducible-experiment-registry",
        "branch-predictor-lab",
        "noc-packet-routing-simulator",
        "systolic-array-market-accelerator",
        "hardware-formal-coverage-lab",
        "portfolio-project-map-generator",
        "queue-position-fill-probability-lab",
        "spread-impact-slippage-estimator",
        "realistic-fill-backtester",
        "tft-market-forecasting-lab",
        "options-liquidity-scanner",
        "skew-term-structure-monitor",
        "axi-lite-register-map-generator",
        "uvm-lite-verification-harness",
        "hls-pipeline-scheduler-lab",
        "pcie-throughput-budget-lab",
        "opra-options-feed-normalizer",
        "fix-session-replay-analyzer",
        "market-halt-circuit-breaker-simulator",
        "risk-limit-policy-dsl",
        "order-throttle-leaky-bucket-lab",
        "corporate-action-price-adjuster",
        "factor-exposure-neutralizer",
        "walk-forward-regime-validator",
        "rtl-lint-rule-engine",
        "clock-domain-reset-sequencer-lab",
        "earnings-iv-crush-model",
        "contract-selector-options-lab",
        "options-pnl-attribution-engine",
        "kernel-bypass-ring-buffer-lab",
        "multicast-gap-recovery-engine",
        "smartnic-flow-table-simulator",
        "riscv-orderbook-coprocessor-lab",
        "memory-bandwidth-benchmark-suite",
        "thermal-aware-fpga-placement-lab",
        "research-paper-reproduction-tracker",
        "order-flow-toxicity-vpin-lab",
        "intraday-seasonality-curve-lab",
        "liquidity-heatmap-engine",
        "news-event-volatility-linker",
        "sec-filing-xbrl-factor-lab",
        "cache-aware-orderbook-layout-lab",
        "dma-burst-coalescer-simulator",
        "hardware-timing-constraint-checker",
        "formal-liveness-monitor-lab",
        "hft-config-drift-detector",
        "lockfree-order-gateway",
        "kernel-bypass-feed-handler-cpp",
        "cacheline-aware-risk-engine",
        "deterministic-replay-cpp-engine",
        "single-writer-ringbuffer-benchmark",
        "queue-reactive-orderbook-model",
        "lob-transformer-reproduction",
        "hawkes-liquidity-clustering-lab",
        "cross-venue-latency-arb-simulator",
        "auction-imbalance-predictor",
        "fpga-transformer-attention-kernel",
        "systolic-array-backtester-accelerator",
        "riscv-vector-alpha-engine",
        "hbm-orderbook-layout-simulator",
        "quantized-ml-fpga-inference-lab",
        "nasdaq-itch-parser-rtl-lab",
        "fix-fast-decoder-benchmark",
        "multicast-feed-arbitration-fpga",
        "ptp-nanosecond-timestamp-core",
        "market-data-tickerplant-simulator",
        "zero-dte-options-backtester",
        "option-replay-report-engine",
        "dealer-gamma-feedback-lab",
        "options-flow-anomaly-detector",
        "iv-surface-microstructure-lab",
        "contract-routing-risk-engine",
        "agentic-strategy-search-lab",
        "paper-to-alpha-reproduction-suite",
        "walk-forward-auto-optimizer",
        "llm-market-hypothesis-auditor",
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
        "degraded-mode-operator-console",
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


def test_public_site_uses_human_facing_milestone_language() -> None:
    combined = "\n".join(read(page).lower() for page in PAGES)
    forbidden = ["system-design docs", "milestone-doc tests"]
    for phrase in forbidden:
        assert phrase not in combined

    assert "system design docs" in combined
    assert "milestone documentation tests" in combined


def test_research_papers_are_visible_and_role_relevant() -> None:
    papers = read(ROOT / "papers.html")
    homepage = read(ROOT / "index.html")

    expected = [
        "Market Data Infrastructure Whitepaper",
        "Strategy Robustness Whitepaper",
        "FPGA Trading Architecture Whitepaper",
        "papers/market-data-infrastructure-whitepaper.md",
        "papers/strategy-robustness-whitepaper.md",
        "papers/fpga-trading-architecture-whitepaper.md",
        "low-latency market data",
        "walk-forward validation",
        "hardware/software trading datapath",
    ]
    for phrase in expected:
        assert phrase in papers

    assert "papers.html" in homepage
    assert "Research Papers" in homepage


def test_research_papers_page_links_reading_map() -> None:
    papers = read(ROOT / "papers.html")
    expected = [
        "Research Reading Map",
        "RESEARCH_READING_MAP.md",
        "DeepLOB",
        "ABIDES",
        "FPGA HFT acceleration",
        "Precision Time Protocol",
    ]
    for phrase in expected:
        assert phrase in papers


def test_review_guide_links_role_packets() -> None:
    guide = read(ROOT / "review-guide.html")
    expected = [
        "Role Packets",
        "ROLE_PACKETS.md",
        "Hardware / FPGA Engineer",
        "Quant Developer",
        "Market Infrastructure Engineer",
        "Cyber-Physical Systems Engineer",
        "AI / Software Engineer",
    ]
    for phrase in expected:
        assert phrase in guide


def test_technical_depth_links_evidence_ledger() -> None:
    depth = read(ROOT / "technical-depth.html")
    expected = [
        "Evidence Ledger",
        "PORTFOLIO_EVIDENCE_LEDGER.md",
        "Low-latency market data",
        "Strategy robustness",
        "FPGA and hardware verification",
        "Cyber-physical systems",
        "AI research governance",
        "Public proof artifacts",
        "Validation method",
        "Honest boundary",
    ]
    for phrase in expected:
        assert phrase in depth


def test_technical_depth_links_reproducibility_guide() -> None:
    depth = read(ROOT / "technical-depth.html")
    expected = [
        "Reproducibility Guide",
        "REPRODUCIBILITY_GUIDE.md",
        "Profile verification",
        "Site verification",
        "Representative repository verification",
        "python -m pytest -q -p no:cacheprovider",
        "gh run list",
        "What this proves",
    ]
    for phrase in expected:
        assert phrase in depth


def test_technical_depth_links_flagship_systems_map() -> None:
    depth = read(ROOT / "technical-depth.html")
    expected = [
        "Flagship Systems Map",
        "FLAGSHIP_SYSTEMS_MAP.md",
        "Low-Latency Market Data and FPGA Trading Datapath",
        "Limit Order Book Intelligence and Market Simulation",
        "Options Microstructure and 0DTE Research OS",
        "AI-Governed Quant Research Factory",
        "Cyber-Physical Timing, Control, and Operator Systems",
        "DeepLOB",
        "ABIDES",
        "LOBFrame",
        "High Frequency Trading Acceleration using FPGAs",
        "not isolated repo count",
    ]
    for phrase in expected:
        assert phrase in depth


def test_review_guide_links_advanced_research_build_queue() -> None:
    guide = read(ROOT / "review-guide.html")
    expected = [
        "Advanced Research Build Queue",
        "ADVANCED_RESEARCH_BUILD_QUEUE.md",
        "Selection standard",
        "Wave 1: Flagship Hardening",
        "Wave 2: Paper Reproduction and Benchmarking",
        "Wave 3: Hardware Acceleration and Formal Verification",
        "Wave 4: Options and Intraday Trading Research",
        "Wave 5: Cyber-Physical and Operator Systems",
        "not count-only expansion",
        "Proof required before promotion",
    ]
    for phrase in expected:
        assert phrase in guide


def test_projects_page_includes_shared_market_packet_fixtures() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "Shared Market Packet Fixtures",
        "shared-market-packet-fixtures",
        "canonical packet contract",
        "CSV round trip",
        "sequence-gap",
        "top-of-book projection",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_fpga_orderflow_formal_properties() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "FPGA Orderflow Formal Properties",
        "fpga-orderflow-formal-properties",
        "SVA-style",
        "halt latch",
        "bounded acknowledgement latency",
        "coverage matrix",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_lob_benchmark_report_generator() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "LOB Benchmark Report Generator",
        "lob-benchmark-report-generator",
        "cost-adjusted",
        "Brier",
        "latency pass",
        "Markdown reports",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_market_sim_scenario_library() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "Market Sim Scenario Library",
        "market-sim-scenario-library",
        "ABIDES-style",
        "deterministic seeds",
        "latency matrices",
        "liquidity-drought",
        "Markdown reports",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_synthetic_options_chain_generator() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "Synthetic Options Chain Generator",
        "synthetic-options-chain-generator",
        "IV skew",
        "open interest",
        "target-delta",
        "Greeks",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_option_replay_report_engine() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "Option Replay Report Engine",
        "option-replay-report-engine",
        "contract PnL",
        "theta drag",
        "volatility contribution",
        "Promote/Watchlist/Reject",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_research_queue_state_machine() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "Research Queue State Machine",
        "research-queue-state-machine",
        "Evidence-gated workflow",
        "promoted",
        "watchlisted",
        "missing-evidence checks",
        "human approval gates",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_degraded_mode_operator_console() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "Degraded Mode Operator Console",
        "degraded-mode-operator-console",
        "Precision Time Protocol",
        "operator acknowledgement",
        "recovery",
        "safe mode",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_deeplob_leakage_test_harness() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "DeepLOB Leakage Test Harness",
        "deeplob-leakage-test-harness",
        "chronological split",
        "label horizon",
        "lookahead leakage",
        "baseline metrics",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_lobframe_metric_dashboard() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "LOBFrame Metric Dashboard",
        "lobframe-metric-dashboard",
        "macro F1",
        "calibration",
        "turnover",
        "cost-adjusted PnL",
        "latency pass rate",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_hlob_depth_persistence_study() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "HLOB Depth Persistence Study",
        "hlob-depth-persistence-study",
        "deep-level persistence",
        "ablation report",
        "shallow",
        "deep",
        "persistence features",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_lobench_representation_lab() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "LOBench Representation Lab",
        "lobench-representation-lab",
        "transferability",
        "downstream tasks",
        "representation family",
        "symbol split",
        "leakage-aware",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_lob_bench_generative_evaluator() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "LOB-Bench Generative Evaluator",
        "lob-bench-generative-evaluator",
        "realism metrics",
        "synthetic message-by-order data",
        "event mix",
        "interarrival",
        "order lifetime",
        "invariant checks",
        "public-safe",
    ]
    for phrase in expected:
        assert phrase in projects


def test_projects_page_includes_abides_agent_strategy_zoo() -> None:
    projects = read(ROOT / "projects.html")
    expected = [
        "ABIDES Agent Strategy Zoo",
        "abides-agent-strategy-zoo",
        "market maker",
        "momentum",
        "noise",
        "informed",
        "latency-arbitrage",
        "deterministic event simulation",
        "agent PnL",
        "inventory risk",
        "public-safe",
    ]
    for phrase in expected:
        assert phrase in projects
