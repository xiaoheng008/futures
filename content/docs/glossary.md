---
type: docs
title: 中英专业术语表
weight: 15
---

# 使用说明

本表覆盖正文和配套实验中的合约产品、订单、账务、风险、行情、恢复、容量及常用接口术语。中文词是本书统一译法；英文列给出常见行业表达，括号中的缩写在正文和 API 中可能直接出现。各交易所字段名不完全相同，API 字段应保留原名，不要只凭翻译推断语义。

正文关键概念首次出现时标注英文或缩写；配套实验和图表使用的术语也在本表按章节收录。术语表覆盖的是本书范围，不是交易行业所有词汇。

## 第 1 章：合约规格与单位

| 中文术语 | English | 说明 |
|---|---|---|
| 合约规格 | contract specifications | 定义产品单位、精度、结算和交易状态的一组规则 |
| 标的资产 | underlying asset | 合约价格或敞口所跟踪的资产 |
| 报价币 | quote currency | 价格中用于报价的币种，如 USDT/BTC 中的 USDT |
| 结算币 | settlement currency / settlement asset | 盈亏、费用或保证金最终计量/结算所用资产 |
| 线性合约 | linear contract | 常见教学模型中，标的数量乘价格得到报价币名义价值 |
| 反向合约 | inverse contract | 常见产品中以固定报价币面值计张数、以标的币结算的合约类型；须核验具体规则 |
| 永续合约 | perpetual contract / perpetual swap | 没有固定到期日的合约 |
| 交割合约 | dated futures / delivery futures | 有到期或交割日的合约 |
| 合约乘数 | contract multiplier | 将合约数量换算为标的数量或名义价值的系数 |
| 合约面值 | contract value / contract face value | 每张合约代表的约定价值 |
| 名义价值 | notional value | 按产品规则和价格计算的仓位参考价值 |
| 名义敞口 | notional exposure | 仓位所对应的名义市场暴露；不等同于本金或保证金 |
| 盈亏 / P&L | profit and loss (P&L) | 仓位或账户的损益；毛盈亏为 gross P&L |
| 价格刻度 | tick size | 订单价格允许变动的最小单位 |
| 数量步长 | quantity step / lot size | 订单数量允许变动的最小单位；交易所字段名可能不同 |
| 最小名义价值 | minimum notional value | 订单允许提交的最低名义价值要求 |
| 合约规格版本 | contract specification version | 订单接受、计算和重放时采用的规则版本 |
| 整数刻度 | integer ticks / integer lots | 用整数表示价格刻度或数量单位，避免浮点误差 |

## 第 2 章：订单接受与生命周期

| 中文术语 | English | 说明 |
|---|---|---|
| 订单 / 委托 | order | 用户提交的买卖指令及其服务端状态 |
| 限价单 | limit order | 指定可接受最高买价或最低卖价的订单 |
| 市价单 | market order | 按产品规则尽快成交、通常不指定限价的订单 |
| 订单生命周期 | order lifecycle | 订单从接收、接受/拒绝到成交、撤销或过期的状态过程 |
| 命令 | command | 请求系统执行的操作，如创建或撤销订单 |
| 状态 | state / status | 订单当前累计成交量、剩余量及生命周期位置 |
| 事件 / 事实 | event / fact | 已发生的业务变化，如订单接受、成交或撤单 |
| 接受确认 | acknowledgment (ACK) | 服务端确认收到/接受命令；不表示订单已成交 |
| 已接受 | accepted | 请求通过相应校验并进入后续处理；不等于完全成交 |
| 已拒绝 | rejected | 请求未被接受或订单被规则拒绝 |
| 部分成交 | partially filled | 已有部分数量成交，订单仍有剩余量 |
| 累计成交量 | cumulative filled quantity (CumQty) | 订单至今实际成交的数量 |
| 活动剩余量 | working leaves quantity | 仍可继续撮合的订单余量；实际 LeavesQty 的终态语义依接口定义 |
| 已撤销量 | canceled quantity | 被取消而未成交的数量，用于解释终态数量守恒 |
| 完全成交 | filled | 原订单数量全部成交 |
| 撤销 | cancel / canceled | 阻止剩余未成交数量继续参与交易；不回滚已成交部分 |
| 有效期 | time in force (TIF) | 限定订单何时失效及未成交余量如何处理的规则 |
| 撤销前有效 | Good Till Canceled (GTC) | 持续有效至成交、撤销或产品规则规定的终止条件 |
| 立即成交或撤销 | Immediate or Cancel (IOC) | 立即撮合可成交部分，并按规则取消余量 |
| 全部成交或取消 | Fill or Kill (FOK) | 通常要求立即全部成交，否则整体取消；以产品定义为准 |
| 只做 Maker | Post Only | 若会立即成为 taker，通常拒绝或取消订单；具体行为按产品定义 |
| 幂等性 | idempotency | 同一业务请求重复处理不会重复产生效果的性质 |
| 幂等键 | idempotency key | 将重试请求映射回原业务操作的标识 |
| 客户端订单 ID | client order ID | 客户端提供的订单关联标识；不一定等同于幂等键 |
| 只减仓 | reduce-only | 只允许减少或关闭已有仓位、不增加仓位风险的订单约束；交易所定义可能不同 |
| 新建 / 已接受 / 已拒绝 / 已成交 / 已撤销 | NEW / ACCEPTED / REJECTED / FILLED / CANCELED | 教学状态名；真实 API 的枚举、终态和迁移规则因交易所而异 |

## 第 3 章：订单簿与撮合

| 中文术语 | English | 说明 |
|---|---|---|
| 订单簿 | order book | 按价格和优先规则组织的活动委托集合 |
| 买盘 / 卖盘 | bids / asks (offers) | 买方和卖方活动报价的一侧 |
| 买一 / 卖一 | best bid / best ask | 当前最高买价和最低卖价 |
| 价位档 | price level | 订单簿中同一价格上的订单或汇总数量 |
| 撮合引擎 | matching engine | 按产品规则选择并执行相互匹配订单的组件 |
| 价格优先、时间优先 | price-time priority | 先按更优价格，再按同价先后排序的优先规则 |
| 先进先出 | First In, First Out (FIFO) | 同一队列中先进入者先处理的顺序 |
| 做市方 | maker | 为簿中增加流动性的订单角色；定义依交易所规则 |
| 吃单方 | taker | 与簿中流动性立即成交的订单角色；定义依交易所规则 |
| 流动性 | liquidity | 在一定价格范围内成交而不产生过大价格冲击的能力 |
| 市场深度 | market depth / order book depth | 各价格档位可交易的数量规模 |
| 买卖价差 | bid-ask spread | 最低卖价与最高买价之间的差 |
| 滑点 | slippage | 实际成交价格相对预期价格的偏差 |
| 自成交保护 | self-trade prevention (STP) | 防止同一受益方订单彼此成交的规则 |

## 第 4 章：成交、账本与仓位

| 中文术语 | English | 说明 |
|---|---|---|
| 成交记录 | fill / execution | 一次撮合产生的价格、数量、双方订单等事实 |
| 成交 ID | fill ID / execution ID / trade ID | 唯一标识成交事实的 ID；不同接口命名不同 |
| 加权平均成交价 | weighted average execution price | 各成交价格按成交数量加权后得到的平均价格 |
| 账本 | ledger | 按业务事实记录资产增减的权威账务记录 |
| 日记账批次 | journal entry / journal batch | 一组关联的账务分录 |
| 账本分录 | ledger entry / posting | 对某账户、资产和账务类别记录的金额变化 |
| 双重记账 | double-entry bookkeeping | 以借贷或对应科目记录一项业务的账务方法；具体科目依系统设计 |
| 仓位 | position | 按账户和产品汇总的持仓方向、数量、均价等状态 |
| 仓位投影 | position projection | 由成交与结算事实计算出的当前仓位视图 |
| 已实现盈亏 | realized P&L | 由平仓或结算确定的盈亏 |
| 未实现盈亏 | unrealized P&L (UPL) | 按参考价格估算、尚未通过平仓结算的盈亏 |
| 钱包余额 | wallet balance | 账户中账务记录得到的资产余额 |
| 权益 | equity | 按账户规则将余额、盈亏和其他项目合并后的风险计量值 |
| 可用余额 | available balance | 扣除相应占用后可用于新业务的额度；公式随模式变化 |
| 保证金预留 | margin reservation | 为仓位或未成交订单风险保留的额度 |
| 冲正 / 补偿分录 | reversal / compensating entry | 用新的相反或修正记录纠正历史账务，不覆盖原记录 |
| 幂等消费者 | idempotent consumer | 可安全接收重复事件而不重复应用效果的消费者 |

## 第 5 章：保证金与风险额度

| 中文术语 | English | 说明 |
|---|---|---|
| 保证金 | margin | 支持衍生品仓位风险的抵押或风险额度 |
| 初始保证金 | initial margin (IM) | 建立或增加风险敞口所需的初始保证金要求 |
| 维持保证金 | maintenance margin (MM) | 持仓继续维持所需的最低风险权益要求 |
| 逐仓保证金 | isolated margin | 风险额度主要限定在单个仓位或指定隔离范围内的模式 |
| 全仓保证金 | cross margin | 账户范围共享抵押品与盈亏的保证金模式 |
| 组合保证金 | portfolio margin | 按多个仓位组合风险计算保证金的模式 |
| 杠杆 | leverage | 名义敞口相对所占用保证金的比例；并非风险上限本身 |
| 风险限额 | risk limit | 对仓位规模、风险档位或保证金要求设置的限制 |
| 风险档位 | risk tier / risk limit tier | 随仓位或名义价值变化的分级风险规则 |
| 抵押品折扣 | collateral haircut | 对抵押资产价值施加的风险折减 |
| 风险预算 | risk budget | 在指定账户或产品范围内允许分配的风险额度 |
| 原子预留 | atomic reservation | 检查额度并占用额度作为一个不可被并发穿插的操作 |
| 线性化 | linearizability | 并发操作表现得像按某个单一顺序瞬间完成的正确性性质 |
| 乐观并发控制 | optimistic concurrency control (OCC) | 先读取和计算，再用版本检查提交，冲突时重试的并发方法 |
| 比较并交换 | compare-and-swap (CAS) | 仅当状态版本符合预期时更新状态的原子操作 |

## 第 6 章：价格与资金费

| 中文术语 | English | 说明 |
|---|---|---|
| 最新成交价 | last traded price (Last) | 本市场最近一笔成交价格 |
| 指数价 | index price (Index) | 按产品规则由现货或其他参考源构造的价格 |
| 标记价 | mark price (Mark) | 用于估值或风险判断的规则化参考价格 |
| 基差 | basis | 合约价格与现货/指数参考价之间的差异 |
| 资金费率 | funding rate | 永续合约周期性资金转移所使用的费率 |
| 资金费用 | funding fee / funding payment | 由资金费率和结算规则计算出的账户收付 |
| 价格新鲜度 | price freshness | 价格数据距离采集/更新时间的状态 |
| 价格源 | price source / market data source | 提供价格输入的市场或数据提供方 |
| 价格偏差 | price deviation | 某价格相对指数、其他来源或产品阈值的偏离 |

## 第 7 章：强平与缺口处理

| 中文术语 | English | 说明 |
|---|---|---|
| 强平 | liquidation | 因风险边界被触发而由系统接管减仓或平仓的流程 |
| 强平触发条件 | liquidation trigger | 启动风险处置所依据的条件 |
| 强平触发价 | liquidation trigger price | 在特定模型下与强平触发对应的价格值；不一定单独定义 |
| 破产价 | bankruptcy price | 仓位可用风险权益耗尽的参考价，产品算法各异 |
| 执行价 | execution price | 强平订单实际成交的价格 |
| 强平引擎 | liquidation engine | 监控风险并协调清算/减仓动作的系统组件 |
| 子订单 | child order | 为执行一条处置或策略指令而创建的具体市场订单 |
| 在途订单 | in-flight order | 已发送或正在执行、最终结果尚未确认的订单 |
| 保险基金 | insurance fund | 按产品规则用于处理特定强平盈亏差额或缺口的资金池 |
| 自动减仓 | auto-deleveraging (ADL) | 按规则减少特定对手方仓位以处理系统性缺口的机制 |
| 亏损缺口 | loss deficit / liquidation deficit | 仓位可承担权益不足以覆盖执行损失时的差额 |

## 第 8 章：故障恢复

| 中文术语 | English | 说明 |
|---|---|---|
| 事件日志 | event log | 按序追加保存业务事实或状态变化的记录 |
| 事件溯源 | event sourcing | 以事件作为权威记录、由事件构建当前状态的一种设计方式 |
| 重放 | replay | 按顺序重新应用已记录事实以恢复状态投影 |
| 快照 | snapshot | 某个明确水位上的状态副本，用于缩短恢复时间 |
| 检查点 | checkpoint | 标记处理进度或恢复起点的位置 |
| 水位 | watermark / high-water mark | 表示事件或状态处理到达的序号边界 |
| 对账 | reconciliation | 比较独立数据视角并定位遗漏、重复或差异 |
| 事务发件箱 | transactional outbox | 在同一事务记录业务状态和待发布消息，再异步可靠投递的模式 |
| 确定性重放 | deterministic replay | 相同输入事实和规则版本产生相同恢复结果 |

## 第 9 章：实时数据流

| 中文术语 | English | 说明 |
|---|---|---|
| WebSocket | WebSocket | 支持双向持续通信的网络协议 |
| REST API | Representational State Transfer API (REST API) | 常见基于 HTTP 资源和方法的接口风格 |
| 行情流 | market data stream | 推送订单簿、成交或价格等公开市场数据的流 |
| 私有流 | private stream / user data stream | 面向已认证用户推送订单、成交或账户变化的流 |
| 快照 | snapshot | 某时点完整或限定深度的状态基线 |
| 增量 | delta / update | 相对既有状态描述变化的数据消息 |
| 序号 | sequence number / sequence ID | 用于检测消息先后、重复或缺口的标识 |
| 游标 | cursor | 客户端续读或恢复消费位置的标识 |
| 心跳 | heartbeat / ping-pong | 用于检测连接存活的周期消息机制 |
| 序号缺口 | sequence gap | 预期连续的消息序号中缺失一段 |
| 重同步 | resynchronization / resync | 丢弃不可信状态并通过新快照/事件恢复一致性的过程 |
| 校验和 | checksum | 对数据内容计算的摘要；须按具体协议解释和验证 |
| 消费滞后 | consumer lag | 消费位置落后于生产位置或最新水位的距离 |

## 第 10 章：容量与过载保护

| 中文术语 | English | 说明 |
|---|---|---|
| 吞吐量 | throughput | 单位时间内完成的工作量 |
| 延迟 | latency | 请求或事件从开始到完成所经过的时间 |
| 突发流量 | traffic burst | 短时间内显著高于常态的到达流量 |
| 积压 | backlog | 尚未处理的请求或事件数量 |
| 有界队列 | bounded queue | 最大容量有限、满载时可触发明确策略的队列 |
| 背压 | backpressure | 下游变慢时向上游传递减速或暂停信号的机制 |
| 准入控制 | admission control | 在昂贵处理之前判断是否接受新工作 |
| 限流 | rate limiting | 限制指定主体或资源范围内请求速率的机制 |
| 限流键 | rate limit key | 决定配额归属的身份或资源键，如 IP、用户或产品 |
| 扇出 | fan-out | 一项数据向多个订阅者或下游消费者分发 |
| 慢消费者 | slow consumer | 消息处理速度低于生产速度的订阅者 |
| 过载 | overload | 输入工作量超过系统当前处理能力的状态 |
| 优雅降级 | graceful degradation | 过载时降低非核心功能，同时保护核心事实与风险不变量 |
| 重试退避 | retry backoff | 失败后逐步延长重试间隔以缓解拥塞的方法 |
| 百分位延迟 | percentile latency | 如 p50、p95、p99 所表示的延迟分布分位值 |

## 通用接口与工程词汇

| 中文术语 | English | 说明 |
|---|---|---|
| 应用程序接口 | Application Programming Interface (API) | 软件组件之间约定的调用界面 |
| 表述性状态转移接口 | Representational State Transfer API (REST API) | 常见基于 HTTP 资源与方法的接口风格；REST 不等于某个固定传输格式 |
| 超文本传输协议 | Hypertext Transfer Protocol (HTTP) | 常见 Web 请求/响应传输协议 |
| WebSocket 协议 | WebSocket Protocol (WS) | 支持持久双向通信的协议 |
| 请求载荷 | payload / request body | 请求或消息中承载业务字段的数据部分 |
| API 密钥 | API key | 用于识别或认证 API 调用方的凭据之一 |
| 网际协议地址 | Internet Protocol address (IP address) | 网络请求来源或目的端的地址标识 |
| 用户标识 | user ID (UID) | 识别账户或调用主体的标识；作用域由接口定义 |
| 用户界面 | user interface (UI) | 面向使用者展示状态和操作入口的界面 |
| 中央处理器 | central processing unit (CPU) | 执行通用计算指令的处理器；CPU 使用率不能单独代表系统容量 |
| 买入方向 | buy / bid side | 订单或仓位的买入方向；字段值以 API 约定为准 |
| 卖出方向 | sell / ask side | 订单或仓位的卖出方向；字段值以 API 约定为准 |
| 数量字段 | quantity (qty) | 订单或成交数量；单位取决于合约规格 |
| 价格字段 | price | 价格数值；必须连同产品、币种和价格类型理解 |
| 创建时间 | creation time / created_at | 记录被创建或系统记录的时间字段；不必然等于撮合顺序 |

## 常见 API 字段与枚举

| 字段或枚举 | English / 常见含义 | 说明 |
|---|---|---|
| `tickSize` / `tickSz` | tick size | 最小价格变动单位；字段名依交易所而异 |
| `qtyStep` / `lotSz` | quantity step / lot size | 最小下单数量单位；字段名依产品而异 |
| `ctVal` | contract value | OKX 等接口中的合约面值字段，须结合 `ctType`、`ctValCcy`、`ctMult` 和产品规则读取 |
| `ctType` | contract type | 合约计价/类型标识，枚举含义以接口文档为准 |
| `seqId` / `prevSeqId` | sequence ID / previous sequence ID | OKX 等流协议用于检查增量连续性的序号字段 |
| `checksum` | checksum | 部分协议中的数据校验字段；是否有效及算法依当前文档 |
| `REQUEST_WEIGHT` | request weight | Binance API 请求权重限额类别 |
| `ORDERS` | order count limit | Binance API 订单数量限额类别 |
| `429 Too Many Requests` | rate limit response | 常见 HTTP 限流响应码；重试范围和等待策略应以具体接口为准 |

## 第 11 章：端到端重建

| 中文术语 | English | 说明 |
|---|---|---|
| 权威事实 | authoritative fact | 后续投影和恢复应以之为依据的已持久化业务记录 |
| 端到端链路 | end-to-end flow | 从输入请求直到结算、恢复和客户端状态更新的完整路径 |
| 不变量 | invariant | 在所有合法状态和转换中都必须持续成立的条件 |
| 数量守恒 | quantity conservation | 原订单数量能由累计成交、活动余量及已撤销/过期数量解释的约束 |
| 账户投影 | account projection | 从账本、成交和资金事件计算出的账户查询视图 |
| 重建 | reconstruction | 从问题、事实和规则重新推导系统状态或概念的过程 |


## 字段与单位补充

| 中文术语 | English | 说明 |
|---|---|---|
| 维持保证金要求金额 | maintenance margin requirement | 金额；OKX 账户余额接口的 `mmr` 以 USD 计，须核对账户模式 |
| 维持保证金率 | maintenance margin rate | 比例；本书模型使用 `r`，不能直接替换为同名缩写的 API 金额字段 |
| 保证金比率 | margin ratio | 无量纲比率；分子、分母与触发方向必须按账户模式核验 |
| 预留转换 | reservation conversion | 成交将订单预留转为持仓占用，撤销只释放尚未成交部分 |
| 序号重置 | sequence reset | 协议允许的水位重新编号；应按前驱关系衔接 |


## 定稿补充术语

| 中文术语 | English | 说明 |
|---|---|---|
| 单向持仓模式 | one-way position mode | 同产品多空按规则净额抵消 |
| 双向持仓模式 | hedge mode / two-way position mode | 按独立多空作用域维护仓位 |
| 净敞口 / 总敞口 | net exposure / gross exposure | 净方向规模与绝对规模合计，不能混用 |
| 持仓平均入场价 | average entry price | 仓位的成本参考价；不一定等于某一张订单的平均执行价 |
| 结算批次 | settlement batch | 一组有明确完成边界的结算义务 |
| 清算对手科目 | clearing counterparty account | 用于记录结算对应方与待履行义务的会计作用域 |
| 待结算义务 | unsettled obligation | 已有事实依据但尚未完成结算的资产责任 |
| 手续费率 / 返佣 | trading fee rate / rebate | 实际费用和可能的负费用，须记录角色、版本和币种 |
| 整数溢出 | integer overflow | 超出数值表示范围导致错误的情况 |
| 定点数 / 舍入 | fixed-point number / rounding | 金额精度表示与不能精确落在结算单位上的数值处理 |
| 前驱序号 | previous sequence ID | 用于衔接本条消息与上一水位的协议字段 |
| 连接代次 | connection generation | 区分新旧连接消息、防止旧消息混入新基线的客户端标识 |
| 截止时间 | deadline | 请求必须完成或在承诺前拒绝的时间边界 |
| 重试抖动 | retry jitter | 为退避等待引入随机分散，减轻集中重连 |
| 恰好一次业务效果 | exactly-once effect | 重复投递下每个业务用途只产生一次效果，并非保证消息只送一次 |
| 服务等级目标 | service level objective (SLO) | 在指定负载和范围内可衡量的服务目标 |
| 统一交易账户 | Unified Trading Account (UTA) | Bybit 账户体系名称；内部风险范围依具体模式定义 |
| 零权益参考价 | zero-equity reference price | 本书简化模型中权益为零的价格，不代替真实破产结算规则 |
