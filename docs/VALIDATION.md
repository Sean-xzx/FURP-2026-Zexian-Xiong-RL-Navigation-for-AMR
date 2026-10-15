# Validation record / 验证记录

Date / 日期: 2026-10-15 (Asia/Shanghai).

Original baseline / 整理前基线: `9616f22`.

The original metrics CLI returned 33.33%/33.33%/33.33% on its built-in example; sample CSV 40%/20%/40%; basic-world archive 0%/10%/90%; U-trap archive 0%/100%/0%. These are baseline behavior checks, not new policy performance claims.

整理前内置样例、sample CSV、basic world 与 U-trap 的 SR/CR/TR 分别为上述数值；这是行为对照，不是新策略成果。

Core code, YAMLs, evidence scripts and result tables are protected by comparison with the baseline commit. The poster is supplied material; it is not execution evidence for STPS. The public copy removes student IDs without changing scientific content. PDF and PNG were exported with installed Microsoft PowerPoint and visually checked.

核心代码、YAML、证据脚本与结果通过与基线提交比较保护。海报属于用户提供材料，不作为 STPS 已运行证据；公开副本只移除学号等隐私元信息，PDF/PNG 使用已安装的 PowerPoint 导出并检查。

Local and remote verification outcomes are recorded below once executed. CI status is available in the repository Actions tab; a committed workflow alone does not establish that it passed.

实际本地与远程验证结果在执行后补记于下方；CI 状态见仓库 Actions，不能仅凭存在工作流文件认定通过。

## Executed locally / 本地已执行

- A new isolated `.venv`, Python 3.12.14 on Windows 11 Home 10.0.26200, with the exact pinned dependencies installed from PyPI; `pip check` passed. / Windows 11 新建隔离环境安装固定依赖，无依赖冲突。
- Five standard-library regression tests passed: archived rates/counts, illustrative sample, empty input, missing file CLI, malformed numeric CSV. / 5 项回归测试通过。
- Original GridWorld produced 19 positions, 18 moves, return 2 and a PNG; additional checks confirmed legal adjacent moves, obstacle avoidance and no path when isolated. / 原脚本及有效路径、不可达场景验证通过。
- IR-SIM basic-world and U-trap: 2 episodes each, seed 42, max 100 steps, repeated twice. Within each world the two CSV files were byte-identical. Basic: 2 timeouts, average path length 5.07005. U-trap: 2 collisions at 49/47 steps, average path length 2.36845. / 两场景各两回合、重复两次，同种子结果一致。
- README local links and public poster hashes passed. The 19 protected source, YAML, evidence and result files were byte-identical to the private backup; Git also reports no changes against the baseline (Git checkout applies Windows line-ending conversion). / 19 个核心源码、场景、证据及结果文件与私有备份字节一致，Git 与基线亦无差异；Git 检出时存在 Windows 换行转换。
- The complete pre-existing Git object history was scanned for common token/private-key patterns (236 objects, no pattern hits); this is a bounded pattern scan, not proof that every possible secret format is absent. No credential was added. / 历史常见凭据模式扫描无命中，未新增凭据。

Logs and generated CSV/PNG files are local `artifacts/` outputs, excluded from Git. Numerical behavior is verified; original archived stochastic runs and poster experiments are not regenerated. / 日志及生成文件保留本地并排除出 Git；未重生成历史随机试验或海报实验。
