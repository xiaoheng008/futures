---
type: docs
title: 研究资料与使用边界
---

# 研究资料与使用边界

本书用公开文档观察外部规则、API 请求/响应、推送语义和产品说明。它们不能证明交易所内部采用了某一种数据库、撮合算法实现、分片拓扑或一致性协议。系统内部方案均标为参考设计、推演或实验模型。

## 主要公开资料

资料复核日期：2026-10-05。已复核本书引用的核心规则与 API 页面；日期表示访问核对时间，不保证规则此后不变。各章记录日期，产品/账户/地区范围以源页面为准。

- [Binance USDⓈ-M Futures Funding Rates](https://www.binance.com/en/support/faq/detail/360033525031)：资金费率组成、结算频率可能调整、资金扣款账户等。
- [Binance USDⓈ-M WebSocket Upgrade Notice (2026-03-06)](https://www.binance.com/en/support/announcement/detail/ebf9b0aa9eca4ff3804eef6fb09ba32a)：public/market/private 三类 WebSocket 地址与迁移日期；仅说明公开接口结构。
- [Binance USDⓈ-M Futures General Info](https://developers.binance.com/en/docs/products/derivatives-trading-usds-futures/general-info)：USDⓈ-M 接口入口。
- [Bybit Instruments Info](https://bybit-exchange.github.io/docs/v5/market/instrument)：tickSize、qtyStep、最小名义价值、合约状态与资金费间隔等规格字段。
- [Bybit Place Order API](https://bybit-exchange.github.io/docs/v5/order/create-order)：下单请求为异步处理、订单状态确认方式等。
- [Bybit Orderbook WebSocket](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook)：快照、增量消息和本地簿维护约定。
- [Bybit Mark Price Calculation](https://www.bybit.com/en/help-center/article/Mark-Price-Calculation-Perpetual-Expiry-Contracts)：标记价格的参考构造及其在未实现盈亏/强平中的用途。
- [Bybit Funding Fee Calculation](https://www.bybit.com/en/help-center/article/Funding-fee-calculation)：资金费率与费用计算示例及频率说明。
- [OKX API v5](https://app.okx.com/docs-v5/en/)：下单、订单频道、WebSocket 行情和限流契约。
- [OKX X-Perps Price References](https://www.okx.com/en-us/help/okx-x-perps-eea-mark-last-index-price)：仅用于该页面限定的产品价格职责对照。
- [OKX API change log](https://app.okx.com/docs-v5/log_en/)：2026-06 订单簿频道使用 `seqId/prevSeqId` 校验连续性的变更说明。
- [Bybit Set Leverage](https://bybit-exchange.github.io/docs/v5/position/leverage)：杠杆与风险限额下最大持仓价值的关系。
- [Bybit Risk Limit](https://bybit-exchange.github.io/docs/v5/market/risk-limit)：公开风险档位和维持保证金参数。
- [Bybit Position WebSocket](https://bybit-exchange.github.io/docs/v5/websocket/private/position)：仓位和保证金字段的公开语义及模式差异。
- [OKX Perpetual Funding Fee Mechanism](https://www.okx.com/en-us/help/perps-funding-fee-mechanism)：永续合约资金费机制及可能变化的结算间隔。
- [Bybit Insurance Fund](https://www.bybit.com/en/help-center/article/Insurance-Fund)：破产价与实际执行价、保险基金增减及 ADL 关系。
- [Bybit Risk Limit](https://www.bybit.com/en/help-center/article/Risk-Limit-Perpetual-and-Expiry-Contracts)：风险档位与分层清算说明。
- [Bybit UTA Liquidation Process](https://www.bybit.com/en/help-center/article/UTA-Trading-Rules-Liquidation-Process)：UTA 风险处置规则，注意账户模式适用边界。
- [Binance Futures Insurance Funds](https://www.binance.com/en/support/faq/detail/360033525371)：Binance 期货保险基金适用范围和风险池说明。
- [Binance ADL](https://www.binance.com/en-AE/support/faq/detail/360033525471)：保险基金不足时 ADL 的公开说明。
- [OINK Theme](https://github.com/pgsty/oink)：书稿站点主题。项目固定 v1.1.0，要求 Hugo Extended 0.160.1+、Go 1.27+。

## 引用纪律

1. 用交易所帮助中心/开发者文档作为产品规则的一手来源；不把论坛、营销文章或逆向猜测写成事实。
2. 同一术语在不同币本位/稳定币本位、逐仓/全仓/组合保证金和不同账户体系中可能对应不同公式与语义。
3. 公开文档只描述对外契约。内部撮合、账本、风控部署拓扑若无公开的一手证据，明确标为教学参考架构。
4. 公式旁写出假设、单位和舍入规则。发生差异时做并列表，而不是强行抽象成唯一“行业公式”。
5. 每章记录资料访问日期；API 变更要更新相关章节及实验。


## 复核定位

| 章节 | 对照页面与观察点 |
|---|---|
| 1 | Bybit instruments-info；OKX Get instruments：价格/数量单位与面值字段 |
| 2–3 | Bybit Place Order / Orderbook；OKX Order channel：异步确认、订单策略、首次订阅行为 |
| 4、8、11 | 账本与内部恢复架构为教学推演；不引用外部 API 来证明内部数据库或原子提交方式 |
| 5 | Bybit Leverage / Risk Limit / Position；OKX Balance：账户模式、字段单位与风险范围 |
| 6 | Bybit Mark / Funding、OKX Funding / X-Perps Prices、Binance Funding：角色与结算间隔 |
| 7 | Bybit Insurance Fund / UTA Liquidation / Risk Limit；Binance Insurance / ADL：客户结算与市场执行、基金和处置范围 |
| 9 | Bybit Orderbook / Connect；OKX Order channel / Order Book；Binance WS公告：快照、前驱、重置、路由 |
| 10 | Binance USDⓈ-M General Info / Common Definitions、Bybit Rate Limit、OKX Rate Limits：限流作用域与响应 |

已将失效的 Bybit 查询参数式 Mark 链接改为正文页面，将旧 Binance 文档入口改为当前 USDⓈ-M General Info。Bybit ADL 的旧地区链接改用本轮可核对的 Insurance Fund 页面；该页面直接说明基金不足后的 ADL 关系。

Binance 保险基金 FAQ 自身注明为教育说明并提示规则可能过时；本书只将其作为公开机制概览，不据此实施客户结算或确定法律义务。实际产品须另查适用条款与合约规格。
