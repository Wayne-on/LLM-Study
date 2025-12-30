# /lab — Code Experiments & Benchmarks (Run and Measure)

`/lab` is the **execution playground**: runnable code, reproducible experiments, and benchmark evidence.
If you can run it, time it, profile it, or compare it, it belongs here.

## What belongs here
- Runnable scripts / minimal repros / prototypes
- Benchmarks and profiling (latency, throughput, memory, cost)
- Configs used in experiments (Docker, env, model args, dataset sampling)
- Logs, outputs, tables, and plots produced by experiments

## What does NOT belong here
- Deep conceptual write-ups → go to `/tracks`
- Long narrative explanations (keep lab docs short, link to tracks for theory)

## Recommended structure per experiment folder
Each experiment folder should be self-contained and reproducible.

Suggested files (choose what you need):
- `README.md` — goal, setup, how to run, expected outputs
- `run.sh` / `run.py` — the actual entrypoint
- `requirements.txt` or `environment.yml` — dependencies
- `configs/` — configs used for runs
- `results/` — outputs (tables, plots, summaries)
- `logs/` — logs (avoid committing huge files if you later use git)

## Recording results (lightweight but consistent)
When you run an experiment, record at least:
- **Date** and **machine** (CPU/GPU, RAM, OS/container)
- **Model/version** and key parameters
- **Dataset/sample** and evaluation method
- **Metrics** (what you measured and how)
- **Conclusion** (one paragraph) + next action

A minimal template you can paste into `results/summary.md`:
- Goal:
- Setup:
- Command:
- Metrics:
- Findings:
- Next:

## Example mapping to your folders
- `lc-v1-lab/` — LangChain v1.0 runnable experiments
- `ds-optimization/` — DeepSpeed performance tests (ZeRO, offload, memory usage, speed)
