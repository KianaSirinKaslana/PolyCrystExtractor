# PolyCrystExtractor

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **从 PDF 文献到 MD 参数：聚合物晶体学数据的自动化提取与物理校验系统**

---

## 🔬 科学背景

聚合物晶体学数据高度碎片化，1990年前文献多为扫描版，且现有工具（如 ChemDataExtractor 2.0）未覆盖聚合物特有的半晶结构、链构象、纤维轴周期等关键参数。本项目构建**五层可观测流水线**，实现从异构文献到计算就绪数据的端到端贯通。

## 🏗️ 五层架构

| 层级 | 功能 | 核心组件 | 状态 |
|:----:|:-----|:---------|:----:|
| **L0** | 文献摄入与自适应路由 | 出版商识别、动态路由分发器 | 🚧 |
| **L0.5** | VLM 领域适配 | 聚合物晶体学微调视觉模型 | 🚧 |
| **L1** | 版面解析与文档树重建 | MinerU/Marker/PDFMiner 统一接口 | 🚧 |
| **L2** | 本体映射与三引擎联合抽取 | 规则引擎 / Snowball ML / LLM 语义引擎 | 🚧 |
| **L3** | 三源融合与物理自洽校验 | V-Z-M-ρ 循环、空间群-晶系匹配 | 🚧 |
| **L4** | 数据库落盘与 ChemAgent 联动 | PostgreSQL + RESTful API + MD 参数预生成 | 🚧 |

> 🚧 = 开发中　✅ = 已完成　🧪 = 测试中

---

## 📁 仓库结构

```
PolyCrystExtractor/
├── data/                    # 数据目录（已加入 .gitignore，不上传 Git）
│   ├── raw_seed_50/         # Phase 0: 50 篇种子文献（PDF + CIF）
│   ├── vlm_finetune/        # Phase 1: VLM 微调数据集
│   ├── golden_standard/     # Phase 2: 双盲标注真值
│   └── processed/           # 中间产物（标准化表格、提取记录）
├── src/                     # 核心源代码（按层组织）
│   ├── layer0_ingest/       # L0: 文献摄入
│   ├── layer1_parse/        # L1: 版面解析
│   ├── layer2_extract/      # L2: 信息抽取
│   ├── layer3_validate/     # L3: 物理校验
│   ├── layer4_export/       # L4: 数据导出与 API
│   └── common/              # 共享组件（本体定义、单位换算、日志）
├── notebooks/               # Jupyter 实验记录
├── scripts/                 # 自动化批处理脚本
├── tests/                   # 单元测试（每层独立）
├── docs/                    # 架构文档与 Prompt 模板
└── docker/                  # 容器化部署配置
```

---

## 🚀 快速开始

### 环境准备

```bash
# 1. 克隆仓库
git clone https://github.com/yourname/PolyCrystExtractor.git
cd PolyCrystExtractor

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 安装开发依赖（可选）
pip install -r requirements-dev.txt

# 5. 运行测试
pytest tests/ -v
```

### 单篇文献测试（示例）

```bash
python -m src.layer0_ingest.download \
    --doi "10.1021/ma00123" \
    --output data/raw_seed_50/
```

---

## 📊 发刊计划

| 轨道 | 目标期刊 | 核心贡献 | 时间节点 |
|:----:|:---------|:---------|:--------:|
| **A** | *Journal of Cheminformatics* | 五层架构方法学 + 三引擎调度 + 物理校验 | Month 4 |
| **B** | *Scientific Data* | PolyCryst-1K 数据集（1000+ 篇物理校验记录） | Month 4 |

---

## 📦 数据获取

本项目数据分层管理，**核心数据不上传 GitHub**：

| 数据层级 | 位置 | 获取方式 |
|:---------|:-----|:---------|
| 种子文献 | `data/raw_seed_50/` | 通过机构订阅或 Sci-Hub 自行下载 |
| 微调数据集 | `data/vlm_finetune/` | 构建脚本生成（见 `scripts/`） |
| 黄金标准 | `data/golden_standard/` | Zenodo DOI 发布（待上传） |
| 完整数据库 | PostgreSQL / Zenodo | 论文发表后公开 |

---

## 🤝 贡献指南

1. **Issue 优先**：发现 bug 或新需求，先开 Issue 讨论
2. **分层测试**：每层代码必须附带 `tests/test_layerX/` 单元测试
3. **物理校验**：任何提取逻辑变更，需通过 L3 校验层回归测试
4. **文档同步**：架构调整需同步更新 `docs/architecture.md`

---

## 📄 许可证

- **代码**：MIT License（见 [LICENSE](LICENSE)）
- **数据集**：CC-BY 4.0（Zenodo 发布时声明）

---

## 📮 联系

- 问题反馈：[GitHub Issues](https://github.com/yourname/PolyCrystExtractor/issues)
- 预印本：待发布（ChemRxiv / arXiv）
- 邮件：your.email@example.com

---

> *"从尘封的 PDF 到超算集群，让每一条聚合物晶体数据都可追溯、可校验、可计算。"*
