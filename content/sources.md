---
title: 研究资料与使用边界
weight: 11
---

# 研究资料与使用边界

本书用公开文档观察外部规则、API 请求/响应、推送语义和产品说明。它们不能证明交易所内部采用了某一种数据库、撮合算法实现、分片拓扑或一致性协议。系统内部方案均标为参考设计、推演或实验模型。

## 主要公开资料

资料核对日期：2026-10-03。交易规则和 API 可能变化；具体章节应记录访问日期、产品类型、地区/账户适用范围及引用页面版本。

- [Binance USDⓈ-M Futures Funding Rates](https://www.binance.com/en/support/faq/detail/360033525031)：资金费率组成、结算频率可能调整、资金扣款账户等。
- [Binance Futures User Data Streams](https://developers.binance.com/en/docs/products/derivatives-trading-coin-futures/user-data-streams)：订单/账户事件推送与消息排序信息（该页面针对 COIN-M；写作时须避免把差异不加核对地推广到 USDⓈ-M）。
- [Bybit Place Order API](https://bybit-exchange.github.io/docs/v5/order/create-order)：下单请求为异步处理、订单状态确认方式等。
- [Bybit Orderbook WebSocket](https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook)：快照、增量消息和本地簿维护约定。
- [Bybit Mark Price Calculation](https://www.bybit.com/en/help-center/article/?id=000001117)：标记价格的参考构造及其在未实现盈亏/强平中的用途。
- [Bybit Funding Fee Calculation](https://www.bybit.com/en/help-center/article/Funding-fee-calculation)：资金费率与费用计算示例及频率说明。
- [OKX API v5](https://app.okx.com/docs-v5/en/)：下单、订单频道、WebSocket 行情和限流契约。
- [OKX Perpetual Funding Fee Mechanism](https://www.okx.com/en-us/help/perps-funding-fee-mechanism)：永续合约资金费机制及可能变化的结算间隔。
- [OKX Mark, Last, and Index Price](https://www.okx.com/en-us/help/okx-x-perps-eea-mark-last-index-price)：区分价格用途；适用范围是页面所述 X-Perps，不能替代其他产品规则。
- [OINK Theme](https://github.com/pgsty/oink)：书稿站点主题。项目固定 v1.1.0，要求 Hugo Extended 0.160.1+、Go 1.27+。

## 引用纪律

1. 用交易所帮助中心/开发者文档作为产品规则的一手来源；不把论坛、营销文章或逆向猜测写成事实。
2. 同一术语在不同币本位/稳定币本位、逐仓/全仓/组合保证金和不同账户体系中可能对应不同公式与语义。
3. 公开文档只描述对外契约。内部撮合、账本、风控部署拓扑若无公开的一手证据，明确标为教学参考架构。
4. 公式旁写出假设、单位和舍入规则。发生差异时做并列表，而不是强行抽象成唯一“行业公式”。
5. 每章记录资料访问日期；API 变更要更新相关章节及实验。
