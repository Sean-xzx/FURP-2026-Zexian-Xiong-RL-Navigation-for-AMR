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

## Published verification / 发布后验证

- Published implementation commit: `85c810fcc8d7bd94b7529ad42c2b52c677d7156a`, on `main` in `Sean-xzx/FURP-2026-Zexian-Xiong-RL-Navigation-for-AMR`. The original `master` branch and preceding history remain intact. The repository is public, default branch `main`, with description and research topics configured. / 整理提交已到原仓库 main，公开且默认分支为 main；原 master 与历史保留，简介及主题已设置。
- [GitHub Actions run 38747439334](https://github.com/Sean-xzx/FURP-2026-Zexian-Xiong-RL-Navigation-for-AMR/actions/runs/38747439334) passed on both `ubuntu-latest` and `windows-latest`, Python 3.12. Installation, dependency checks and all functional verification steps succeeded. / Windows/Linux 云端依赖安装、依赖检查与功能验证全部通过。
- A fresh clone from the remote `main` branch, with a newly created isolated environment, successfully installed `requirements/reproducible.txt`, passed `pip check` and completed `tools/verify_project.py`. No packages from the original project environment were used. / 远程 main 干净克隆新建环境独立安装并通过完整验证，未借用原项目环境的包。
- GitHub's rendered HTML for both READMEs contains the poster preview, PDF and reciprocal language links. Public PDF/PPTX/PNG downloads matched local SHA-256 hashes. / GitHub 生成的双语 HTML 包含预览、PDF 与语言切换链接；公开下载的海报文件哈希均一致。
- The owner confirmed that no additional STPS source, models or experiment records are available beyond this repository and supplied poster. Full STPS reproduction remains blocked by missing assets, while the included lightweight workflows are verified. / 所有者确认没有其他 STPS 源码、模型或试验记录，因此完整 STPS 复现受缺失资源阻碍；已有轻量流程验证通过。

This final documentation update references the verified implementation commit above. Later CI runs are available in [Actions](https://github.com/Sean-xzx/FURP-2026-Zexian-Xiong-RL-Navigation-for-AMR/actions). / 本记录的最终文档更新对应上述已验证实现，后续检查见 Actions。
