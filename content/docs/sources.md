---
type: docs
title: 研究资料与使用边界
---

# 研究资料与使用边界

本书用公开文档观察外部规则、API 请求/响应、推送语义和产品说明。它们不能证明交易所内部采用了某一种数据库、撮合算法实现、分片拓扑或一致性协议。系统内部方案均标为参考设计、推演或实验模型。

## 主要公开资料

资料核对日期：2026-10-03。交易规则和 API 可能变化；具体章节应记录访问日期、产品类型、地区/账户适用范围及引用页面版本。

- [Binance USDⓈ-M Futures Funding Rates](https://www.binance.com/en/support/faq/detail/360033525031)：资金费率组成、结算频率可能调整、资金扣款账户等。
- [Binance USDⓈ-M WebSocket Upgrade Notice (2026-03-06)](https://www.binance.com/en/support/announcement/detail/ebf9b0aa9eca4ff3804eef6fb09ba32a)：public/market/private 三类 WebSocket 地址与迁移日期；仅说明公开接口结构。
- [Binance USDⓈ-M Futures API Introduction](https://developers.binance.com/en/docs/derivatives/usds-margined-futures/Introduction)：USDⓈ-M 接口入口。
- [Binance Futures User Data Streams](https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/user-data-streams)：订单/账户事件推送与消息排序信息（该页面针对 COIN-M；写作时须避免把差异不加核对地推广到 USDⓈ-M）。
- [Bybit Instruments Info](https://bybit-exchange.github.io/docs/v5/market/instrument)：tickSize、qtyStep、最小名义价值、合约状态与资金费间隔等规格字段。
- [Bybit Place Order API](https://bybit-exchange.github.io/docs/v5/order/create-order)：下单请求为异步处理、订单状态确认方式等。
- [Bybit Orderbook WebSocket](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook)：快照、增量消息和本地簿维护约定。
- [Bybit Mark Price Calculation](https://www.bybit.com/en/help-center/article/?id=000001117)：标记价格的参考构造及其在未实现盈亏/强平中的用途。
- [Bybit Funding Fee Calculation](https://www.bybit.com/en/help-center/article/Funding-fee-calculation)：资金费率与费用计算示例及频率说明。
- [OKX API v5](https://app.okx.com/docs-v5/en/)：下单、订单频道、WebSocket 行情和限流契约。
- [OKX Mark, Last, and Index Price](https://www.okx.com/en-us/help/okx-x-perps-eea-mark-last-index-price)：X-Perps 产品范围内各价格用途说明，注意其适用产品限制。
- [OKX API change log](https://app.okx.com/docs-v5/log_en/)：2026-06 订单簿频道使用 `seqId/prevSeqId` 校验连续性的变更说明。
- [Bybit Set Leverage](https://bybit-exchange.github.io/docs/v5/position/leverage)：杠杆与风险限额下最大持仓价值的关系。
- [Bybit Risk Limit](https://bybit-exchange.github.io/docs/v5/market/risk-limit)：公开风险档位和维持保证金参数。
- [Bybit Position WebSocket](https://bybit-exchange.github.io/docs/v5/websocket/private/position)：仓位和保证金字段的公开语义及模式差异。
- [OKX Perpetual Funding Fee Mechanism](https://www.okx.com/en-us/help/perps-funding-fee-mechanism)：永续合约资金费机制及可能变化的结算间隔。
- [OKX Mark, Last, and Index Price](https://www.okx.com/en-us/help/okx-x-perps-eea-mark-last-index-price)：区分价格用途；适用范围是页面所述 X-Perps，不能替代其他产品规则。
- [Bybit Insurance Fund](https://www.bybit.com/en/help-center/article/Insurance-Fund)：破产价与实际执行价、保险基金增减及 ADL 关系。
- [Bybit Risk Limit](https://www.bybit.com/en/help-center/article/Risk-Limit-Perpetual-and-Expiry-Contracts)：风险档位与分层清算说明。
- [Bybit UTA Liquidation Process](https://www.bybit.com/en/help-center/article/UTA-Trading-Rules-Liquidation-Process)：UTA 风险处置规则，注意账户模式适用边界。
- [Bybit ADL](https://www.bybit.com/nl-NL/help-center/article?id=000001124)：保险基金不足时 ADL 的公开说明。
- [Binance Futures Insurance Funds](https://www.binance.com/en/support/faq/detail/360033525371)：Binance 期货保险基金适用范围和风险池说明。
- [Binance ADL](https://www.binance.com/en-AE/support/faq/detail/360033525471)：保险基金不足时 ADL 的公开说明。
- [OINK Theme](https://github.com/pgsty/oink)：书稿站点主题。项目固定 v1.1.0，要求 Hugo Extended 0.160.1+、Go 1.27+。

## 引用纪律

1. 用交易所帮助中心/开发者文档作为产品规则的一手来源；不把论坛、营销文章或逆向猜测写成事实。
2. 同一术语在不同币本位/稳定币本位、逐仓/全仓/组合保证金和不同账户体系中可能对应不同公式与语义。
3. 公开文档只描述对外契约。内部撮合、账本、风控部署拓扑若无公开的一手证据，明确标为教学参考架构。
4. 公式旁写出假设、单位和舍入规则。发生差异时做并列表，而不是强行抽象成唯一“行业公式”。
5. 每章记录资料访问日期；API 变更要更新相关章节及实验。
