---
title: 三家主流交易所的公开接口观察
weight: 12
---

# 这张对照表能说明什么？

Binance、Bybit、OKX 对外暴露的 API 和流协议，是我们能核验的系统行为。它们不能反推出撮合引擎使用的线程模型、存储引擎或服务拓扑。把“公开 API 契约”与“架构推论”分开，避免把书中的参考设计误写成交易所内部事实。

资料核对日期：2026-10-03。具体适用合约类型、账户地区和产品版本，请以每个源页面的范围为准。

| 观察面 | Binance USDⓈ-M Futures | Bybit V5 | OKX API V5 |
|---|---|---|---|
| 创建订单接口 | REST 与 WebSocket 接口均按其合约 API 文档定义；部署/路由细节可能升级 | REST `POST /v5/order/create`；文档明确响应是异步接受确认 | REST `POST /api/v5/trade/order`；另有私有 WS 订单频道 |
| 后续状态观察 | 2026 年公告将 USDⓈ-M WebSocket 分为 `/public`、`/market`、`/private` 类别；私有流承载用户事件 | 文档要求通过 WebSocket 确认订单状态；公共与私有流分离 | 私有 `/ws/v5/private` 的 `orders` 频道；首次订阅不推存量快照，只推新订单/更新 |
| 订单簿数据 | 以 USDⓈ-M 产品对应的 market stream 文档为准，留意公告中的迁移和路由变化 | 公共订单簿发 snapshot 后持续推 delta；新 snapshot 要重置本地簿 | 不同频道有快照/增量与不同频率；2026 年日志要求指定频道用 `seqId/prevSeqId` 检查连续性，不再依赖旧 checksum |
| 从中可推导的工程要求 | 接口适配层不能把所有 WS 流假设为同一业务类型；升级需要兼容与迁移计划 | 客户端须区分命令 ACK、订单状态、成交事件，并实现本地簿恢复 | 订阅 orders 不能当作首次状态查询；需组合 REST 快照/查询与后续推送，并用序号检测缺口 |

来源：[Binance USDⓈ-M WS 升级公告](https://www.binance.com/en/support/announcement/detail/ebf9b0aa9eca4ff3804eef6fb09ba32a)、[Binance USDⓈ-M Futures API 文档入口](https://developers.binance.com/en/docs/derivatives/usds-margined-futures/Introduction)、[Bybit 创建订单](https://bybit-exchange.github.io/docs/v5/order/create-order)、[Bybit 私有订单流](https://bybit-exchange.github.io/docs/v5/websocket/private/order)、[Bybit 订单簿流](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook)、[OKX API v5](https://app.okx.com/docs-v5/en/)、[OKX API 变更日志](https://app.okx.com/docs-v5/log_en/)。

# 从外部契约到内部系统：哪些是推论？

**直接可观察的事实**包括 URL、请求字段、订单状态字段、推送时机、快照/增量格式、序号规则、限流和产品适用范围。应引用官方文档，并注明核对日期。

**参考架构推论**包括“服务端要维护幂等键”“客户端需要序号重同步”“命令确认和最终订单结果必须分开建模”。这些是由可观察契约与分布式系统故障模型推出的工程结论，不代表交易所公开承认内部使用了某种实现。

**不可据此断言**某交易所采用单线程撮合、Kafka、Raft、特定数据库、微服务或某种分片键。除非一手资料明确披露，否则书中一律写作教学参考方案。

# 练习

选一个公开产品（例如 Binance USDⓈ-M BTCUSDT 永续、Bybit linear BTCUSDT 永续、OKX BTC-USDT-SWAP），建立一页“契约卡”：

- 产品标识和地区/账户适用性；
- 创建、查询、撤单的 REST/WS 接口；
- 哪个响应只代表接受，哪个事件代表订单更新，哪个事件代表成交；
- 订阅后是否先给快照，如何检测丢包/序号缺口；
- 文档访问日期；
- 一项你能确认的事实和一项不能从公开文档推出的内部猜测。

# 新问题

产品接口会变，但交易系统必须守住不变量。最终问题是：无论上游接口如何差异化，内部如何把规范化命令、订单状态和成交事实连接起来？回到第 10 章重建。
