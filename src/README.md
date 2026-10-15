# Source map / 源码导览

World YAML → `irsim_env/evaluate_random_policy.py` → episode CSV → `eval/evaluate_csv.py` → `eval/metrics.py`.

YAML defines geometry and robot states; the evaluator sends random velocities, records episodes and aggregates outcomes. `irsim_env/demos/` retains earlier implementations and its own basic-world YAML for existing callers. Its timeout counter differs from the later evaluator; use `tools/run_random_baseline.py` for new runs.

YAML 定义几何与机器人状态，随机策略产生 CSV，指标模块汇总结果。保留旧演示及其独立 YAML 以兼容已有调用，新试验使用根目录的带种子启动器。

See [English](../README.md), [中文](../README.zh-CN.md), [reproduction / 复现](../docs/REPRODUCIBILITY.md). STPS training and switching code are absent. 当前未包含 STPS 训练与切换实现。
