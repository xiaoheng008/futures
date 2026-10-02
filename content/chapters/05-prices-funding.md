---
title: 最新成交价为什么不能单独触发强平？
weight: 6
---

# 问题

薄弱市场的一笔小成交让最后成交价瞬间下跌 8%，但外部现货价格几乎没变。若马上据此强平，系统会制造怎样的风险？

# 发现

把价格用途分开：最后成交价描述本市场最近一次成交；指数价综合外部现货参考；标记价为盈亏/风险计算构造较稳健的参考值。不同交易所、产品和账户模式的具体构造及用途不同，须查规则，不可互换。[Bybit 标记价说明](https://www.bybit.com/en/help-center/article/?id=000001117)；[OKX 价格说明](https://www.okx.com/en-us/help/okx-x-perps-eea-mark-last-index-price)

永续合约还需要资金费率把合约价格锚定现货。资金费是持仓者之间按结算规则转移的费用，不是撮合手续费；费率、间隔、上限可能按产品或市场状况变化。[OKX 资金费机制](https://www.okx.com/en-us/help/perps-funding-fee-mechanism)；[Bybit 资金费计算](https://www.bybit.com/en/help-center/article/Funding-fee-calculation)

# 实验

制作一个时间序列：现货指数稳定、合约最后成交价短暂偏离、基差逐步回归。分别用 Last、Index、Mark 计算盈亏，标出哪种价格变化会触发本章假设的风险阈值。

# 新问题

更稳健的价格也不能消除真实亏损。当权益低于维持要求，系统如何减少仓位并处理穿仓缺口？

# 重建

解释三种价格各自回答什么问题。假设你忘记了资金费率公式，能否从“永续没有到期日、价格可能偏离现货”重新推导它需要解决的压力？
