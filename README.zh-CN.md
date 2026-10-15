[English](README.md) · [简体中文](README.zh-CN.md)

# STPS：让机器人导航走出死胡同

**FURP 团队研究：让机器人摆脱导航陷阱，同时保持狭窄通道中的精度。**

**[研究海报 PDF](FURP_Showcase.pdf) · [演示文稿 PPTX](FURP_Showcase.pptx)**

[![STPS 研究海报](docs/assets/stps-poster.png)](FURP_Showcase.pdf)

## 项目价值与个人贡献

持续朝目标前进的机器人可能困在 U 型障碍中；探索奖励有助于脱困，却可能降低通过窄门所需的精度。团队提出**停滞触发策略切换（STPS）**：保持精确导航和探索策略的参数冻结，在运动停滞时切换两种互补策略。

**熊泽贤（Zexian Xiong / Sean）**是团队海报的共同作者。[个人项目记录](docs/00_weekly_CN.md)涵盖环境搭建、GridWorld 导航、IR-SIM 场景构建与随机策略评估，以及 ROS2/SLAM/Nav2 集成实验。这些材料体现仿真、Python 评估和导航失败分析能力，尚不能确认每个 STPS 模块的个人分工，因此 STPS 研究成果归于团队。

## 方法与成果证据

海报描述：20 步位移小于 0.15 m，或振荡达到 5/12 时切换到探索策略；脱困模式至少执行 120 步且位移超过 0.5 m 后返回。切换机制组合已训练策略，无需额外训练。

| 证据 | 结果 | 复现状态 |
| --- | --- | --- |
| 团队海报：STPS v2 | 报告困难场景平均成功率 94%，基线 67%；U-trap 75±7%；窄门 100%；标准环境 88% | 仅有海报，缺少 STPS 源码、模型与原始试验记录 |
| GridWorld BFS | 18 次移动、19 个位置、回报 2 | 有可运行脚本 |
| 存档 basic-world 随机策略 | 10 回合：成功率 0%，碰撞率 10%，超时率 90% | 可从 CSV 重算 |
| 存档 U-trap 随机策略 | 10 回合：成功率 0%，碰撞率 100%，超时率 0% | 可从 CSV 重算 |

海报的“场景平均”不包含单列的标准环境：(75 + 100 + 100 + 100) / 4 = 93.75%，四舍五入为 94%。± 的含义、试验次数与种子未充分说明。团队结果、计算开销和实机部署说法在本次整理中均**未独立验证**。`sample_eval_results.csv` 是说明用样例，不是实验依据。

## 快速开始

CSV 评估只依赖 Python 标准库，不需要 GPU、账号、付费服务或下载数据集。

```sh
git clone https://github.com/Sean-xzx/FURP-2026-Zexian-Xiong-RL-Navigation-for-AMR.git
cd FURP-2026-Zexian-Xiong-RL-Navigation-for-AMR
python src/eval/evaluate_csv.py --file results/u_trap_random_eval.csv
```

预期最后一行：

```text
SR=0.00%, CR=100.00%, TR=0.00%, AvgSteps=44.40, AvgPathLength=2.23, N=10
```

运行 GridWorld 和 IR-SIM，请建立 Python 3.12 环境：

```sh
python -m venv .venv
# Windows PowerShell：
.venv\Scripts\Activate.ps1
# Linux/macOS shell 则使用：source .venv/bin/activate
python -m pip install -r requirements/reproducible.txt
python tools/verify_project.py
python tools/run_random_baseline.py --seed 42 --world src/irsim_env/worlds/u_trap_world.yaml --scenario u_trap --goal-x 5 --goal-y 9 --episodes 2 --max-steps 100 --output artifacts/u_trap_seed42.csv
python src/eval/evaluate_csv.py --file artifacts/u_trap_seed42.csv
```

验证覆盖 GridWorld、存档指标与仿真行为，生成文件保存到 `artifacts/`。随机运行生成逐回合 CSV，不能复现海报中的训练策略。安装需联网，可能耗时数分钟；简短 CPU 示例通常数秒完成。[复现说明](docs/REPRODUCIBILITY.md)列有配置、环境与限制。

## 结构与数据流程

- `FURP_Showcase.pdf`、`FURP_Showcase.pptx`：团队展示材料；`docs/assets/` 提供预览。
- `src/irsim_env/worlds/`：YAML 定义几何、起点与目标；`evaluate_random_policy.py` 向 IR-SIM 发送随机速度，记录回合 CSV。
- `src/eval/`：读取 CSV，聚合成功率 SR、碰撞率 CR、超时率 TR、步数与路径长度。
- `docs/evidence-week01/`：独立 BFS GridWorld 脚本与原始证据。
- `results/`：逐字节保留的原始表格；`tools/` 在不改变核心代码的前提下增加带种子启动与验证。
- `tests/`、`.github/workflows/verify.yml`：回归测试与 CI；`docs/` 保留历史记录。

可运行主线为 **世界 YAML → 仿真器与随机动作 → 回合 CSV → 指标**。GridWorld 独立验证离散最短路。STPS 策略切换由海报描述，当前代码未包含其实现。

## 项目状态、开发与权利

仓库用于研究展示，提供可运行的早期实验。ROS2、Gazebo、Cartographer、Nav2、Qwen 和 Habitat 里程碑属于历史记录，完整启动文件、地图与场景资源未收录；训练后 STPS 复现及实机部署暂不可用。历史随机试验未记录种子；旧演示的超时步数多计一次。实际执行情况见[验证记录](docs/VALIDATION.md)。

标准库测试：`python -m unittest discover -s tests -v`；安装依赖后完整验证：`python tools/verify_project.py`。通过 [GitHub Issues](https://github.com/Sean-xzx/FURP-2026-Zexian-Xiong-RL-Navigation-for-AMR/issues)反馈命令、环境与不含凭据的报错。复用或修改前须取得许可。

**保留所有权利，不授予开源许可证。**公开仓库供通过平台查看，其他使用、再分发或修改须取得相关权利人的许可。团队署名与第三方权利保持不变，详见 [RIGHTS.md](RIGHTS.md)。
