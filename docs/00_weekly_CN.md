# 每周进度日志

> **每周**更新此文件。每一周在最上方新增一条记录。
> 这是我们审阅时最先检查的东西。保持诚实、具体 —— 它同时计入你的出勤记录(规则 1)。

**使用方法:** 每新增一周,复制下方的 *周记模板* 块。最新的一周放在最上面。

---

## 周记模板 —— 复制我

### 第 N 周 — YYYY-MM-DD

**本周是否参加会议:** 是 / 否(若否,是否已邮件请假?是 / 否)

**本周进度**

- _你实际做了/完成了什么?_

**挑战与阻碍**

- _什么挡住了你?你卡在哪里?_

**下一步**

- _下周你打算做什么?_

**投入时长(可选):** _例如 6h_

**链接(可选):** _commit、notebook、文档、数据集……_

---

<!-- =================  以下为你的记录  ================= -->

### 第 2 周 — 2026-06-15~

**本周是否参加会议:** 是

**本周进度**

- 完成了一次 Habitat-Sim 冒烟测试。
- 接入 Qwen 大模型，实现了 turtlesim 中小乌龟受**自然语言控制移动**
<img width="853" height="370" alt="image" src="https://github.com/user-attachments/assets/a3101c12-6670-481d-8152-9112fba4189b" />
<img width="253" height="265" alt="image" src="https://github.com/user-attachments/assets/0cd74339-8e7d-4205-89ff-a660ea2511bc" />



**挑战与阻碍**

- 本次冒烟测试**仅为无传感器(no-sensor)模式**:RGB/深度渲染与截图输出尚未测试。

**下一步**

- 学习 Habitat-Lab 的 PointNav 任务结构。

**投入时长(可选):** 

**链接(可选):**

### 第 1 周冒烟测试补充 — 2026-06-13

**进度**

- 完成了第三个冒烟测试示例:**跑一个最短路导航回合(shortest-path navigation episode)**。
- 在 Windows 11 上实现了一个简单的 10×10 GridWorld 导航任务。
- agent 从 `(0, 0)` 移动到 `(9, 9)`,并绕开了障碍物。
- 脚本打印了轨迹、移动步数、episode return,并保存了一张渲染出的轨迹图。

**证据**

- `gridworld_shortest_path_smoke.py`
- `smoke_test_output.txt`
- `gridworld_trajectory.png`

**结果**

- 路径长度:19 个位置
- 移动步数:18
- Episode return:2
- 状态:**SMOKE TEST PASSED(冒烟测试通过)**

**说明**

- 这是一个 Windows 兼容的 GridWorld 冒烟测试,**不是** Habitat-Sim 的冒烟测试。
- Habitat-Sim 的渲染在当前 Windows/WSL 环境下仍被阻断。

**下一步**

- 实现随机策略(random-policy)导航。
- 加入奖励设计(reward design)。
- 启动一个基础的 Q-learning baseline。

### 第 1 周 — 2026-06-11

**本周是否参加会议:** 是

**本周进度**

- 基于 FURP 模板建立了仓库;选定方向:**RL Navigation for AMR(Habitat 路线)**。
- 在 Windows 11 + WSL2(Ubuntu 22.04.5)上搭建了工作环境:conda 环境 `habitat`,Python 3.10.20;无冲突地安装了 habitat-sim 0.3.3(源码编译)与 habitat-lab 0.3.3。
- 确认 GPU 计算通路正常:NVIDIA RTX 3060,驱动 546.30,CUDA 12.3(`nvidia-smi` 正常)。
- 编写并运行了 `smoke_test.py`。测试通过:habitat-sim 成功导入(v0.3.3),场景 / agent / 完整 Configuration 对象均能创建(agent count: 1)—— 证明该栈安装正确、可被调用。
- 提交了第 1 周 checkpoint(中 + 英)、环境说明、冒烟测试截图,以及一份错误记录。

**挑战与阻碍**

- **主要阻碍 —— 渲染:** WSL2 透传了 GPU 的 CUDA 计算通路,但**未**透传 EGL 渲染通路。`Simulator()` 需要一个 CUDA 绑定的 EGL 设备,而 WSL 中不存在 → 报错 `unable to find CUDA device 0 among 1 EGL devices`。这阻断了全部四个示例(加载场景 / 推理 / 回合 / 渲染),因此冒烟测试只验证了导入 + 配置,而非真正的渲染。
- 尝试了源码重编(GUI 开/关)和 Xvfb 虚拟显示器 —— 均为同一根因。
- 顺带解决的其他安装问题:conda 服务条款未接受;pillow 版本冲突;git-lfs 缺失;Python 3.9 依赖断代(改用 3.10 重建);编译内存耗尽(限制并行度);WSL 文件系统崩溃(`wsl --shutdown` 恢复)。

**下一步**

- 阅读(优先级从高到低):1)Habitat-Lab 文档 + PointNav 任务定义;2)PPO 的直觉理解;3)(进阶)DD-PPO 论文。参考清单第 1 节的 VLN 论文(R2R / Speaker-Follower / PREVALENT / RxR / VLN-CE)对 RL 路线仅需了解。
- Baseline 目标(分级):**第 1 级(本周目标)**—— 在可渲染的环境下,让 `Simulator()` 真正启动、加载测试场景、执行几个随机动作并拿到观测(即补完第 1 周未完成的最基础示例)。**第 2 级(之后)**—— 跑通一个最小的 PointNav 训练流程(需 GPU 渲染)。

**仍需支持**

- 需要一台原生 Linux / 实验室 GPU 机器以获得完整 EGL 渲染支持,从而真正加载场景并运行带渲染的回合。

**投入时长(可选):** 20h

**链接(可选):**
