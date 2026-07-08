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


### Week 5 — 2026-07-07~

**Attended this week's meeting:** Yes

**Progress this week**

- 完成 Ubuntu 22.04.5 系统安装，并恢复 RTX 3060 驱动与 `nvidia-smi`。
- 安装并验证 ROS2 Humble，跑通 TurtleSim、键盘控制和 topic / pose 读取。
- 配置 `irsim_rl` 环境，安装并验证 IR-SIM。
- 跑通 IR-SIM basic world，完成随机策略 episode 运行、CSV 保存和 SR / CR / TR 评估。
- 搭建第一个 hard scenario：U-trap，并完成 random baseline 评估：SR=0%，CR=100%，TR=0%。

**Challenges & blockers**

- 当前仍处于 hard scenario benchmark 搭建阶段，尚未开始 CNNTD3 训练。
- U-trap 场景已能运行，但还需要继续补齐 Double-U、Narrow Door、Dead-end Maze 和 Symmetric Corridor。

**Next steps**

- 完成其余 4 个 IR-SIM hard scenarios。
- 汇总 basic world 与 hard scenarios 的 random baseline 结果。
- 开始复现 CNNTD3 baseline，并在 S1-S5 场景上评估。

**Hours spent (optional):** 26–28h

**Links (optional):**


### Week 4 — 2026-06-29~

**Attended this week's meeting:** 是

**Progress this week**

- 在 Gazebo 中成功运行 TurtleBot3 自定义环境。
- 完成 Cartographer SLAM 建图，并保存地图文件。
- 启动 Nav2，完成 AMCL 定位。
- 在 RViz 中使用 Nav2 Goal，实现小车自动导航到目标点。
<img width="464" height="488" alt="Screenshot 2026-07-01 155649" src="https://github.com/user-attachments/assets/12513ccd-2411-42ac-aa6d-5c8199dcf95c" />
<img width="1279" height="761" alt="Screenshot 2026-07-01 154829" src="https://github.com/user-attachments/assets/093292ea-f70f-442f-ac95-b39652b4ce46" />
<img width="1279" height="761" alt="Screenshot 2026-07-01 155343" src="https://github.com/user-attachments/assets/5f2d0529-8126-4b86-8f6b-86d93609698a" />


**Challenges & blockers**

- Gazebo 中机器人 spawn 有时不稳定，需要手动补进世界。
- Nav2 初始阶段出现 TF 报错，设置 2D Pose Estimate 后解决。

**Next steps**

- 整理本次 SLAM + Nav2 流程，作为后续自然语言导航和 RL 导航的 baseline。

**Hours spent (optional):**

**Links (optional):**

### Week 3 — 2026-06-22~

**Attended this week's meeting:**

**Progress this week**

**Challenges & blockers**

**Next steps**

**Hours spent (optional):**

**Links (optional):**

### Week 2 — 2026-06-15~

**Attended this week's meeting:** 是

**Progress this week**

- 完成了一次 Habitat-Sim 冒烟测试。
- 接入 Qwen 大模型，实现了 turtlesim 中小乌龟受**自然语言控制移动**
  `<img width="853" height="370" alt="image" src="https://github.com/user-attachments/assets/a3101c12-6670-481d-8152-9112fba4189b" />`
  `<img width="253" height="265" alt="image" src="https://github.com/user-attachments/assets/0cd74339-8e7d-4205-89ff-a660ea2511bc" />`

**Challenges & blockers**

- 本次冒烟测试**仅为无传感器(no-sensor)模式**:RGB/深度渲染与截图输出尚未测试。

**Next steps**

- 学习 Habitat-Lab 的 PointNav 任务结构。

**Hours spent (optional):**

**Links (optional):**

### Smoke Test Update in Week 1 — 2026-06-13

**Progress**

- 完成了第三个冒烟测试示例:**跑一个最短路导航回合(shortest-path navigation episode)**。
- 在 Windows 11 上实现了一个简单的 10×10 GridWorld 导航任务。
- agent 从 `(0, 0)` 移动到 `(9, 9)`,并绕开了障碍物。
- 脚本打印了轨迹、移动步数、episode return,并保存了一张渲染出的轨迹图。

**Evidence**

- `gridworld_shortest_path_smoke.py`
- `smoke_test_output.txt`
- `gridworld_trajectory.png`

**Result**

- 路径长度:19 个位置
- 移动步数:18
- Episode return:2
- 状态:**SMOKE TEST PASSED(冒烟测试通过)**

**Note**

- 这是一个 Windows 兼容的 GridWorld 冒烟测试,**不是** Habitat-Sim 的冒烟测试。
- Habitat-Sim 的渲染在当前 Windows/WSL 环境下仍被阻断。

**Next steps**

- 实现随机策略(random-policy)导航。
- 加入奖励设计(reward design)。
- 启动一个基础的 Q-learning baseline。

### Week 1 — 2026-06-11

**Attended this week's meeting:** 是

**Progress this week**

- 基于 FURP 模板建立了仓库;选定方向:**RL Navigation for AMR(Habitat 路线)**。
- 在 Windows 11 + WSL2(Ubuntu 22.04.5)上搭建了工作环境:conda 环境 `habitat`,Python 3.10.20;无冲突地安装了 habitat-sim 0.3.3(源码编译)与 habitat-lab 0.3.3。
- 确认 GPU 计算通路正常:NVIDIA RTX 3060,驱动 546.30,CUDA 12.3(`nvidia-smi` 正常)。
- 编写并运行了 `smoke_test.py`。测试通过:habitat-sim 成功导入(v0.3.3),场景 / agent / 完整 Configuration 对象均能创建(agent count: 1)—— 证明该栈安装正确、可被调用。
- 提交了第 1 周 checkpoint(中 + 英)、环境说明、冒烟测试截图,以及一份错误记录。

**Challenges & blockers**

- **主要阻碍 —— 渲染:** WSL2 透传了 GPU 的 CUDA 计算通路,但**未**透传 EGL 渲染通路。`Simulator()` 需要一个 CUDA 绑定的 EGL 设备,而 WSL 中不存在 → 报错 `unable to find CUDA device 0 among 1 EGL devices`。这阻断了全部四个示例(加载场景 / 推理 / 回合 / 渲染),因此冒烟测试只验证了导入 + 配置,而非真正的渲染。
- 尝试了源码重编(GUI 开/关)和 Xvfb 虚拟显示器 —— 均为同一根因。
- 顺带解决的其他安装问题:conda 服务条款未接受;pillow 版本冲突;git-lfs 缺失;Python 3.9 依赖断代(改用 3.10 重建);编译内存耗尽(限制并行度);WSL 文件系统崩溃(`wsl --shutdown` 恢复)。

**Next steps**

- 阅读(优先级从高到低):1)Habitat-Lab 文档 + PointNav 任务定义;2)PPO 的直觉理解;3)(进阶)DD-PPO 论文。参考清单第 1 节的 VLN 论文(R2R / Speaker-Follower / PREVALENT / RxR / VLN-CE)对 RL 路线仅需了解。
- Baseline 目标(分级):**第 1 级(本周目标)**—— 在可渲染的环境下,让 `Simulator()` 真正启动、加载测试场景、执行几个随机动作并拿到观测(即补完第 1 周未完成的最基础示例)。**第 2 级(之后)**—— 跑通一个最小的 PointNav 训练流程(需 GPU 渲染)。

**Support needed**

- 需要一台原生 Linux / 实验室 GPU 机器以获得完整 EGL 渲染支持,从而真正加载场景并运行带渲染的回合。

**Hours spent (optional):** 20h

**Links (optional):**
