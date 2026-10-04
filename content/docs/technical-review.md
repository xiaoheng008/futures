---
title: 技术审校记录
type: docs
weight: 25
---

# 2026-10-05：单位与协议边界

本轮审校集中在第 4、5、9 章，并同步实验、术语表与公开接口对照。全书 11 章仍为草稿；本记录不代表全书引用和图示已完成最终审校。

| 问题 | 修订 | 学习位置 |
|---|---|---|
| 钱包余额与含浮盈亏权益混称 | 平仓入账描述统一为钱包余额 | 第 4 章 |
| 部分成交后撤单释放多少 | 60 预留转为 36 订单预留与 24 持仓占用；撤单只释放 36 | 第 5 章正文与实验 |
| 金额、费率、比率混读 | 区分 MM 金额、r 比例、E/MM 比率，以及 OKX mmr 的 USD 单位 | 第 5 章 |
| 风险档位模型被误用于实际产品 | 说明全名义价值分档的跳变与真实参数核验边界 | 第 5 章实验 |
| 所有深度频道都套用快照加增量 | 补充 Bybit 一档快照例外 | 第 3、9 章 |
| 所有序号回退都当作异常 | 增加 OKX 前驱衔接、空心跳、维护重置的逐步算例 | 第 9 章 |

## 算例之间的参数边界

第 6 章的逐仓保证金 40 USDT 与第 7 章的 60 USDT 属于独立场景。第 7–8 章的两笔强平产生 0.516 USDT 缺口；第 11 章采用另一成交路径，缺口为 0.496 USDT。价格和成交路径改变，结果也随之改变；比较时应先核对参数。

## 本轮核对的公开文档

- [Bybit Orderbook](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook)：快照、增量、一档频道例外。
- [OKX Account Balance](https://app.okx.com/docs-v5/en/#trading-account-rest-api-get-balance)：字段单位与适用账户模式。
- [OKX Order Book](https://app.okx.com/docs-v5/en/#order-book-trading-market-data-ws-order-book-channel)：前驱序号、维护重置、弃用 checksum。

后续继续逐章核对引用、实验答案和图示表达，再决定哪些章节可以结束草稿状态。
