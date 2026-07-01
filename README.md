# RL Navigation for AMR 项目记录

> FURP 本科科研项目
>
> 项目方向：强化学习导航、机器人控制、奖励设计
>
> 当前阶段：ROS2 + Gazebo + SLAM + Nav2 自动导航验证

## 1. 项目信息

| 项目     | 内容                                                           |
| -------- | -------------------------------------------------------------- |
| 学生     | 熊泽贤（Zexian Xiong / Sean）                                  |
| 项目名称 | RL Navigation for AMR                                          |
| 项目方向 | Reinforcement Learning Navigation for Autonomous Mobile Robots |
| 当前路线 | ROS2 / Gazebo / TurtleBot3 / Cartographer / Nav2               |
| 当前定位 | 先完成经典导航 baseline，再继续学习 RL Navigation              |

---

## 2. 当前最新成果

目前已完成一个最小版 **Gazebo + TurtleBot3 + SLAM + Nav2 自动导航 demo**：

```text
Gazebo 自定义环境
    ↓
TurtleBot3 小车仿真
    ↓
Cartographer SLAM 建图
    ↓
保存地图文件
    ↓
Nav2 自动导航到目标点
```

当前已经完成：

- 成功在 Gazebo 中加载 TurtleBot3 和自定义障碍环境；
- 小车可以通过键盘控制在环境中移动；
- 使用 Cartographer 完成 SLAM 建图；
- 保存地图为 `.yaml` 和 `.pgm` 文件；
- 启动 Nav2，并通过 AMCL 完成定位；
- 在 RViz 中使用 `Nav2 Goal` 发送目标点，小车可以自动规划路径并导航。

## 3. 当前进展概览

详细过程写在 `docs/00_weekly.md` 中。README 只保留主线概览。

| 阶段                       | 状态   | 简要说明                                                        |
| -------------------------- | ------ | --------------------------------------------------------------- |
| Habitat 最小冒烟测试       | 已完成 | 启动 Habitat-Sim，运行 no-sensor random episode                 |
| ROS2 turtlesim 手动控制    | 已完成 | 启动小乌龟仿真，并用键盘控制移动                                |
| ROS2 turtlesim 自动到点    | 已完成 | 使用 P-controller 控制小乌龟移动到 `(8.0, 8.0)`               |
| Qwen 自然语言解析          | 已完成 | 将“让小乌龟去右上角”解析为 `{"goal_x": 8.0, "goal_y": 8.0}` |
| Qwen + ROS2 turtlesim 闭环 | 已完成 | 将自然语言解析结果接入小乌龟自动导航程序                        |
| Gazebo TurtleBot3 仿真     | 已完成 | 成功启动 TurtleBot3，并在自定义环境中移动                       |
| Cartographer SLAM 建图     | 已完成 | 使用激光雷达扫描环境并生成地图                                  |
| 地图保存                   | 已完成 | 保存建图结果为 `.yaml` 和 `.pgm` 文件                       |
| Nav2 自动导航              | 已完成 | 在 RViz 中发送 Nav2 Goal，小车自动规划路径并到达目标点          |
| 学习 Habitat PointNav      | 进行中 | 理解 PointNav 任务结构和 RL 导航基本流程                        |
| RL Navigation baseline     | 待开始 | 后续计划从简单 GridWorld / PointNav 开始做强化学习导航实验      |

## 4. 项目目标 / 项目规划

短期目标：

- 跑通 ROS2 经典导航完整流程：建图、定位、路径规划、自动导航；
- 将 Nav2 作为后续导航 baseline；
- 继续学习 Habitat PointNav 和基础强化学习导航任务。

中期目标：

- 在简单环境中实现 RL navigation baseline；
- 设计基础 reward，包括到达目标奖励、碰撞惩罚、路径长度惩罚；
- 对比经典 Nav2 方法和 RL 方法的表现。

后续方向：

- 尝试将自然语言目标转换为导航目标点；
- 探索 LLM + Nav2 / RL Navigation 的结合方式；
- 为最终展示准备一个清晰的可运行 demo。

---

## 5. 阅读资料

正在读：

**1. VLN-R2R:** https://openaccess.thecvf.com/content_cvpr_2018/papers/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.pdf

**2. Q-Learning:** https://link.springer.com/content/pdf/10.1007/BF00992698.pdf

阅读计划：

**1. R2R benchmark:** [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html)
The classic benchmark that made instruction-following navigation concrete and measurable.

**2. Speaker-Follower:** [Speaker-Follower Models for Vision-and-Language Navigation](https://arxiv.org/abs/1806.02724)
A strong early baseline with data augmentation and pragmatic training ideas.

**3. PREVALENT:** [PREVALENT: Learning Representations for Vision and Language Navigation](https://arxiv.org/abs/2001.10266)
Useful for understanding pretraining and representation learning in VLN.

**4. RxR:** [Room-Across-Room: Multilingual Vision-and-Language Navigation](https://arxiv.org/abs/2010.07954)
Important if you care about multilingual or richer instruction descriptions.

**5. VLN-CE:** [Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2004.02857)
Bridges graph-based VLN benchmarks and more realistic continuous navigation.

---

## 6. 当前总结

目前项目已经从早期的 `turtlesim` 自然语言控制，推进到真实机器人导航流程的仿真阶段。

当前最重要的成果是：

```text
Gazebo 仿真环境中，TurtleBot3 已完成 SLAM 建图，并成功进入 Nav2 自动导航阶段。
```

这说明项目已经具备了一个可展示的经典导航 baseline。后续可以在此基础上继续加入自然语言目标解析、RL 导航实验和方法对比。
