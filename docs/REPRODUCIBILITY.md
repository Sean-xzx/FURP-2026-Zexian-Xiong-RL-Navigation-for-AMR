# Reproduction / 复现

## Supported scope / 范围

The lightweight path uses Python 3.12, NumPy 2.2.6, Matplotlib 3.10.3 and IR-SIM 2.10.1. Exact direct and transitive versions are in `requirements/reproducible.txt`. A clean Windows environment is verified in `VALIDATION.md`; Linux is checked by CI. macOS is not verified. CUDA and PyTorch are not needed for these examples. `requirements/irsim_rl_minimal.txt` is retained as the original unpinned research package list, not the reproducible install command.

轻量流程使用 Python 3.12、NumPy 2.2.6、Matplotlib 3.10.3、IR-SIM 2.10.1。完整固定版本见 `requirements/reproducible.txt`；Windows 干净环境验证见 `VALIDATION.md`，Linux 由 CI 检查，macOS 未验证。示例不需要 CUDA 或 PyTorch。原 `irsim_rl_minimal.txt` 是历史依赖清单，不作为可复现安装入口。

From repository root / 在仓库根目录执行：

```sh
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Linux shell alternative / Linux 替代命令
# source .venv/bin/activate
python -m pip install -r requirements/reproducible.txt
python -m pip check
python tools/verify_project.py
```

If PowerShell blocks activation, use `.venv\Scripts\python.exe` in place of `python` without changing system policy. The CSV evaluator alone requires no third-party packages. No secrets or external services are required. Installation downloads packages from PyPI; the CPU verification does not require network. No paid operation is part of the documented workflow.

PowerShell 禁止激活时可直接以 `.venv\Scripts\python.exe` 替代 `python`，无需修改系统策略。单独 CSV 评估无第三方依赖。流程无秘密配置或外部服务；安装从 PyPI 下载，CPU 验证无需联网，无付费操作。

## Minimal examples / 最小示例

```sh
python src/eval/metrics.py
python src/eval/evaluate_csv.py --file results/sample_eval_results.csv
python src/eval/evaluate_csv.py --file results/basic_world_random_eval.csv
python src/eval/evaluate_csv.py --file results/u_trap_random_eval.csv
python -m unittest discover -s tests -v
```

Expected metrics / 预期指标：

| Input | SR | CR | TR | AvgSteps | AvgPathLength | N |
| --- | --- | --- | --- | --- | --- | --- |
| metrics.py internal example / 内置示例 | 33.33% | 33.33% | 33.33% | 166.67 | 5.43 | 3 |
| sample CSV / 说明样例 | 40% | 20% | 40% | 196.00 | 6.10 | 5 |
| basic-world archive / 存档 | 0% | 10% | 90% | 191.60 | 9.48 | 10 |
| U-trap archive / 存档 | 0% | 100% | 0% | 44.40 | 2.23 | 10 |

Run the original GridWorld directly with a noninteractive plotting backend; its image is written into the working directory. `verify_project.py` runs it from `artifacts/` to protect original evidence.

原 GridWorld 直接运行时图像保存到当前工作目录。验证器使用 `artifacts/` 运行以保护原始证据。

```sh
# PowerShell
$env:MPLBACKEND = 'Agg'
python docs/evidence-week01/gridworld_shortest_path_smoke.py
# Linux: MPLBACKEND=Agg python docs/evidence-week01/gridworld_shortest_path_smoke.py
```

Success: 19 positions, 18 moves, return 2, `SMOKE TEST PASSED`, and `gridworld_trajectory.png`. BFS uses fixed obstacles and has no training. Plot pixels may vary by fonts and platform; numeric path behavior is checked instead of requiring identical PNG bytes.

成功条件为 19 个位置、18 次移动、回报 2、通过提示与轨迹图。BFS 使用固定障碍，无训练；字体和平台可影响图片像素，验证数值行为而非图片字节一致性。

```sh
python tools/run_random_baseline.py --seed 42 --world src/irsim_env/worlds/basic_world.yaml --scenario basic_world --goal-x 9 --goal-y 9 --episodes 2 --max-steps 100 --output artifacts/basic_seed42.csv
python tools/run_random_baseline.py --seed 42 --world src/irsim_env/worlds/u_trap_world.yaml --scenario u_trap --goal-x 5 --goal-y 9 --episodes 2 --max-steps 100 --output artifacts/u_trap_seed42.csv
python src/eval/evaluate_csv.py --file artifacts/u_trap_seed42.csv
```

Both worlds are 10×10 with 0.1 s simulation steps; YAMLs are the authoritative geometry and start states. CLI goal coordinates must agree with the YAML goal. Actions are uniform linear velocity [0,1] and angular velocity [-1,1]. Success threshold is 0.35 m. CSV fields: scenario, episode_id, success, collision, timeout, steps, path_length (simulation distance). Each example should emit two rows with one terminal outcome per episode and at most 100 steps, plus aggregate metrics. These runs validate function, not navigation quality.

两种场景均为 10×10、仿真步长 0.1 秒；以 YAML 中几何与起点为准，CLI 目标应与 YAML 一致。动作线速度均匀采样 [0,1]、角速度 [-1,1]，到达阈值 0.35 m。CSV 包含场景、回合编号、成功/碰撞/超时、步数、路径长度。每例应生成两条记录，每回合一个终止结果、最多 100 步，并可计算汇总指标；这是功能验证，不代表导航性能。

The wrapper seeds Python and NumPy without changing the original evaluator. Verification repeats each scene twice and compares CSV bytes within one fixed environment. Cross-platform floating-point or future simulator behavior may differ; historical CSVs have no recorded seed and cannot be regenerated exactly.

启动器在不修改评估器的前提下设置 Python 与 NumPy 种子。验证器每场景运行两次，检查同一固定环境内 CSV 字节一致。跨平台浮点或仿真差异仍可能存在；历史 CSV 未记录种子，无法严格重生成。

## Limits and missing assets / 限制与缺失资源

- Original `demos/random_action_demo.py` reports 201 steps for a 200-step timeout; original CSVs preserve this. The later evaluator reports the correct loop count. No core code or results were rewritten. / 旧演示将 200 步超时计为 201，存档保留原值；后来的评估器计数正确。未改核心代码或结果。
- The evaluator labels a non-success `env.done()` as collision; this is a simplified termination interpretation, not a general physical collision guarantee. CSV boolean parsing recognizes only case-insensitive `true`; malformed numeric/missing fields raise errors, other boolean strings become false. No input hardening was added to core code. / 评估器将未成功时的 `env.done()` 归为碰撞，仅属简化解释；布尔值仅识别忽略大小写的 `true`，错误数值或缺列会报错，其他布尔字符串视为假。未改核心输入处理。
- STPS/CNN-TD3/RCPG training code, precision/exploration weights, train/eval splits, seeds, raw trials and timing measurements are absent. Training reproduction, inference reproduction and poster performance verification are blocked by missing assets. No trained models are downloaded. / 缺少训练源码、策略权重、数据划分、种子、原始试验与计时记录，阻碍训练、推理和海报性能复现，不下载未知模型。
- ROS2/Gazebo maps and launch files, Qwen integration code and Habitat `.glb` scenes/navmeshes are absent. Historical Ubuntu 22.04/24.04 and GPU notes are not fresh compatibility guarantees. Habitat no-sensor history does not verify RGB/depth rendering or PointNav training. / 缺少 ROS2/Gazebo 地图与启动文件、Qwen 集成及 Habitat 场景/navmesh。历史 Ubuntu/GPU 笔记不作为当前兼容性承诺；无传感器试验不代表渲染或 PointNav 训练已验证。
- To restore those workflows, obtain the original authored launch/config files, appropriately licensed scenes and team-owned STPS implementation/checkpoints with full experiment configuration; verify permissions before publishing. / 后续需取得原配置、合法场景及团队 STPS 实现与模型，附完整实验设置，确认权限后再发布。

## Development / 开发

CI installs the pinned environment and runs real GridWorld and seeded IR-SIM checks on Windows and Linux. There is no separate package build. Tests protect archived rates, empty input and malformed/missing CSV handling; verification also checks GridWorld obstacles/unreachable goals, simulator row bounds, deterministic repeats, README local links and poster checksums. No credentials belong in issues or commits.

CI 在 Windows/Linux 安装固定依赖并执行真实 GridWorld 和带种子 IR-SIM 验证，无单独打包步骤。测试保护存档指标、空输入、错误 CSV；验证还检查障碍/不可达目标、仿真结果范围、重复一致性、README 本地链接与海报校验值。反馈和提交勿包含凭据。
