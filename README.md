<img width="128" height="128" alt="icon-128" src="https://github.com/user-attachments/assets/8b0bd45a-1f3e-42a2-93f9-39d6dbb77644" /># RL Navigation for AMR 项目记录

> FURP 本科科研项目
> 
> 项目方向：强化学习导航、机器人控制、奖励设计
> 
> 当前阶段：ROS2 小乌龟自动导航 + 国产大模型自然语言接口

## 1. 项目信息

| 项目     | 内容                                                           |
| -------- | -------------------------------------------------------------- |
| 学生     | 熊泽贤（Zexian Xiong / Sean）                                  |
| 项目名称 | RL Navigation for AMR                                          |
| 项目方向 | Reinforcement Learning Navigation for Autonomous Mobile Robots |
| 当前路线 |                                                                |
| 当前定位 |                                                                |
---

## 2. 当前最新成果

目前已完成一个最小版 **国产大模型 + ROS2 turtlesim 自然语言导航 demo** 的前置验证：

```text
中文自然语言指令
    ↓
Qwen / 通义千问解析目标坐标
    ↓
ROS2 控制小乌龟自动移动到目标点
```

当前已经完成：

- ROS2 `turtlesim` 自动到点 baseline；
- Qwen / 通义千问自然语言解析测试；
- 小乌龟可以被自然语言导航

## 3. 当前进展概览

详细过程写在 `docs/00_weekly.md` 中。README 只保留主线概览。

| 阶段                    | 状态   | 简要说明                                                        |
| ----------------------- | ------ | --------------------------------------------------------------- |
| Habitat 最小冒烟测试    | 已完成 | 启动 Habitat-Sim，运行 no-sensor random episode                 |
| ROS2 turtlesim 手动控制 | 已完成 | 启动小乌龟仿真，并用键盘控制移动                                |
| ROS2 turtlesim 自动到点 | 已完成 | 使用 P-controller 控制小乌龟移动到 `(8.0, 8.0)`               |
| Qwen 自然语言解析       | 已完成 | 将“让小乌龟去右上角”解析为 `{"goal_x": 8.0, "goal_y": 8.0}` |
| Qwen + ROS2 完整闭环    | 进行中 | 将自然语言解析结果接入小乌龟自动导航程序                        |
| 学习 Habitat PointNav  | 进行中 |  |

## 4. 项目目标 / 项目规划


---

## 5. 阅读资料
正在读：

**1. VLN-R2R:** https://openaccess.thecvf.com/content_cvpr_2018/papers/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.pdf

**2. Q-Learning:** https://link.springer.com/content/pdf/10.1007/BF00992698.pdf

阅读计划:

**1. R2R benchmark:** [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html)  
   The classic benchmark that made instruction-following navigation concrete and measurable.

**2. Speaker-Follower:** [Speaker-Follower Models for Vision-and-Language Navigation](https://arxiv.org/abs/1806.02724)  
   A strong early baseline with data augmentation and pragmatic training ideas.

**3. PREVALENT:** [PREVALENT: Learning Representations for Vision and Language Navigation](https://arxiv.org/abs/2001.10266)  
   Useful for understanding pretraining and representation learning in VLN.

**4.RxR:** [Room-Across-Room: Multilingual Vision-and-Language Navigation](https://arxiv.org/abs/2010.07954)  
   Important if you care about multilingual or richer instruction descriptions.

**5. VLN-CE:** [Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2004.02857)  
   Bridges graph-based VLN benchmarks and more realistic continuous navigation.
