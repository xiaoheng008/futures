# 合约交易所核心系统：从一笔委托到风险闭环

一本面向有后端开发基础读者的演进式系统设计书。课程从合约单位和规格开始，逐步推导订单校验、撮合、账本、保证金、价格参考、强平与故障恢复。学习路径是概念因果重建，不是交易所历史叙事或对任何交易所内部架构的声称。

## 内容状态

第 1–9 章已有工作初稿，待技术审校；第 10 章容量与运营、第 11 章端到端重建仍在规划中。在线首页和[课程路线](content/roadmap.md)会区分现有稿件与计划内容。OINK 从 `content/book/` 自动生成 Book 导航，目录树是唯一章节顺序来源。

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
