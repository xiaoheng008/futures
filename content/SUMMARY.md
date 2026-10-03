# 章节导航

1. [一张合约到底代表什么？](chapters/01-contract-spec.md)
2. [你说“下单成功”时，系统究竟承诺了什么？](chapters/02-order-acceptance.md)
3. [为什么一张订单簿还不够？](chapters/03-order-book.md)
4. [成交了，钱和仓位怎样只变化一次？](chapters/04-ledger-position.md)
5. [余额够下单，为什么仍会被拒绝？](chapters/05-margin-risk.md)
6. [最新成交价为什么不能单独触发强平？](chapters/06-prices-funding.md)
7. [强平如何把账户风险转成市场订单？](chapters/07-liquidation.md)
8. [断电、重连、重放后，状态凭什么可信？](chapters/08-recovery.md)
9. [行情推送如何在断线后重新连续？](chapters/09-streaming.md)
10. [高峰期系统如何保护核心状态？](chapters/10-scale-operations.md)
11. [从空白重建合约交易核心](chapters/11-reconstruction.md)

## 参考与实验

- [三家主流交易所的公开接口观察](exchange-behavior.md)
- [订单簿实验：价格优先与队列顺序](experiments/order-book.md)
- [委托状态与重试实验](experiments/order-lifecycle.md)
- [成交与账本实验](experiments/ledger-position.md)
- [保证金与并发预留实验](experiments/margin-risk.md)
- [价格与资金费实验](experiments/prices-funding.md)
- [强平与保险基金实验](experiments/liquidation.md)
- [故障恢复实验](experiments/recovery.md)
- [流连续性实验](experiments/stream-recovery.md)
