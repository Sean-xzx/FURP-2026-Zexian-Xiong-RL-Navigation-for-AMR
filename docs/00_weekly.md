# Weekly Progress Log

> Update this file **every week**. Add a new entry at the top for each week.
> This is the first thing we check during review. Keep it honest and specific — it also feeds your attendance record (Rule 1).

**How to use:** copy the *Week template* block below for each new week. Newest week goes at the top.

---

## Week template — copy me

### Week N — YYYY-MM-DD

**Attended this week's meeting:** Yes / No (if No, did you email leave? Yes / No)

**Progress this week**
- _What did you actually do / finish?_

**Challenges & blockers**
- _What got in the way? What are you stuck on?_

**Next steps**
- _What will you do next week?_

**Hours spent (optional):** _e.g. 6h_

**Links (optional):** _commits, notebooks, docs, datasets..._

---

<!-- =================  YOUR ENTRIES BELOW  ================= -->

### Week 1 — 2026-06-11
 
**Attended this week's meeting:** Yes
 
**Progress this week**
- Set up repository from the FURP template; chose path: **RL Navigation for AMR (Habitat)**.
- Built the working environment on Windows 11 + WSL2 (Ubuntu 22.04.5): conda env `habitat`, Python 3.10.20; installed habitat-sim 0.3.3 (built from source) and habitat-lab 0.3.3 without conflicts.
- Confirmed GPU compute path is healthy: NVIDIA RTX 3060, driver 546.30, CUDA 12.3 (`nvidia-smi` OK).
- Wrote and ran `smoke_test.py`. It passes: habitat-sim imports (v0.3.3), and scene / agent / full Configuration objects all build (agent count: 1) — proving the stack is installed and callable.
- Submitted Week 1 checkpoint (CN + EN), environment note, smoke-test screenshot, and an error log.
**Challenges & blockers**
- **Main blocker — rendering:** WSL2 passes the GPU's CUDA compute path but **not** the EGL rendering path. `Simulator()` requires a CUDA-backed EGL device that does not exist in WSL → `unable to find CUDA device 0 among 1 EGL devices`. This blocks all four lab examples (load scene / inference / episode / render), so the smoke test verifies import + config only, not actual rendering.
- Tried source rebuild (GUI on/off) and an Xvfb virtual display — both hit the same root cause.
- Other setup issues solved along the way: conda ToS not accepted; pillow version conflict; missing git-lfs; Python 3.9 dependency break (rebuilt on 3.10); compile out-of-memory (limited parallelism); WSL filesystem crash (`wsl --shutdown`).
**Next steps**
- Reading (high → low priority): 1) Habitat-Lab docs + PointNav task definition; 2) intuition for PPO; 3) (advanced) DD-PPO paper. The Section-1 VLN papers (R2R / Speaker-Follower / PREVALENT / RxR / VLN-CE) are awareness-only for the RL path.
- Baseline target (staged): **Level 1 (this week's goal)** — in a render-capable environment, get `Simulator()` to actually start, load a test scene, take a few random actions, and obtain an observation (i.e. complete the most basic example left unfinished in Week 1). **Level 2 (later)** — run a minimal PointNav training loop (needs GPU rendering).
**Support needed**
- Access to a native Linux / lab GPU machine for full EGL rendering, to actually load a scene and run a rendered episode.
**Hours spent (optional):**
 
**Links (optional):** Pull Request #1 (Week 1 submission); `assignments/Week01_Zexian_Xiong/`
