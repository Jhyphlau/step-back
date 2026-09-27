# 来源研究与贡献边界

日期：2026-09-27。检索意图：stage closure；scope creep stop；step-back agent skill。公开 GitHub 源码已读取，未执行候选代码。

| 来源 | 学到什么 | 采用位置 | 不采用 |
| --- | --- | --- | --- |
| [555cider/agent-skills step-back](https://github.com/555cider/agent-skills/blob/main/skills/step-back/SKILL.md) | 交付前回看原要求、判断下一步是否增加有用信息 | SKILL 的收口与失焦分支 | 固定工具调用次数与次数型触发，避免机械打断 |
| [JetXu-LLM/smallest-complete](https://github.com/JetXu-LLM/smallest-complete/blob/main/skills/smallest-complete/SKILL.md) | 必需工作完成后停止、关联改进不自动升级为交付门槛 | SKILL 的原任务/新需求区分 | 架构、测试策略、发布与交接体系，不是本 Skill 的职责 |
| [Swallow100/gpt-5.6-stop-overengineering](https://github.com/Swallow100/gpt-5.6-stop-overengineering/blob/main/skills/gpt56-stop-overengineering/SKILL.md) | 范围内阻塞与可选改进分开 | 作为对照，不直接复制 | 编程专用流程与额外四行合同 |

keep：基于结果和证据判断收口；adapt：工程检查点转为跨领域自然节点；reject：后台监控、硬计数、复杂架构流程；invent：完成后用户仅询问关联问题时标明换题，但明确执行新任务或计划内后续时不重复要求授权。

新增分支是设计差异，不是优于上游的实证结论。原始问题已转为匿名跨领域案例，不公开私人会话或项目路径。

缺失证据：本轮未调用 skills.sh/SkillsMP 目录（已有用户选定来源，沿用直接 GitHub 核源）；无安装量、评分、遥测、模型对照效果或长期用户收益数据。不按星数判断质量。许可证与版本核查另见 THIRD_PARTY_NOTICES.md。
