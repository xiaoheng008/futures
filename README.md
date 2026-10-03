# 数字资产永续合约交易系统

**副标题：从一笔委托推导撮合、账本与风险处置**

一本面向有后端开发基础读者的演进式系统设计教程，聚焦中心化交易所的数字资产线性永续合约。全书以一笔 BTC-USDT 委托和一个账户为主线，推导规格校验、订单接入、撮合、账本、保证金、标记价格、强平与故障恢复。交割合约和期权不在本教程范围内；学习路径是概念因果重建，不是交易所历史叙事，也不声称披露交易所内部架构。

## 内容状态

第 1–11 章均已有工作初稿和配套实验，仍待统一技术审校。在线首页和[课程路线](content/roadmap.md)标出当前稿件状态。OINK 从 `content/book/` 自动生成 Book 导航，目录树是唯一章节顺序来源。

## 本地阅读

固定工具链：Hugo Extended 0.165.0、Go 1.27.0、OINK v1.1.0。无需 Node/npm。

```sh
go mod download github.com/pgsty/oink
hugo server
```

发布前严格构建：

```sh
hugo --cleanDestinationDir --gc --minify --environment production \
  --printPathWarnings --panicOnWarning
```

## GitHub Pages

仓库已包含 `.github/workflows/github-pages.yaml`：push 到 `main` 后会用 Hugo Extended 0.165.0 和锁定的 Go/OINK 依赖运行警告严格的生产构建并部署 Pages。首次使用前，在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。本地构建成功与远端部署成功是两个独立状态；部署工作流要在 push 后确认。

## 资料边界

公开交易规则和 API 用于核验外部产品契约；内部撮合、账本和风险部署设计均作为教学参考架构明确标注。参见[资料与引用纪律](content/docs/sources.md)。
