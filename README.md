# 合约交易所核心系统：从一笔委托到风险闭环

一本面向有后端开发基础读者的演进式系统设计书。我们从“如何可靠地接受一笔限价单”出发，让撮合、账户记账、保证金、标记价格、强平、清算和恢复能力逐步成为必须解决的问题。

> 学习路线是按概念因果重建的教学顺序，不是任何一家交易所的历史或内部架构披露。公开交易规则/API 用于观察外部契约；系统内部实现是明确标注的参考设计。

## 本地阅读

项目使用 Hugo + OINK。要求 Hugo Extended 0.160.1+、Go 1.27+；主题固定为 OINK v1.1.0（Hugo Module），不需要 Node/npm。之后运行 `hugo server`。

```sh
hugo mod get github.com/pgsty/oink@v1.1.0
hugo mod tidy
hugo server
```

## 阅读顺序

从 [课程总览](content/_index.md) 开始，也可查看 [演进地图](evolution-map.md)、[章节导航](content/SUMMARY.md) 和 [研究资料及使用边界](sources/README.md)。每章包含一个系统压力、一个可操作实验、验证问题和重建任务。
