# WB GPT MVP 工具仓库

这个仓库用于集中管理和归档我与 ChatGPT 一起生成的 WB / 俄罗斯电商相关 MVP 工具。

仓库目标：

- 一个仓库管理多个工具；
- 每个工具保留多个版本；
- 每个版本都有说明、变更记录和测试记录；
- 方便以后把新工具、新版本、使用说明继续放进来。

## 当前工具索引

| 工具 | 当前版本 | 用途 | 路径 |
|---|---:|---|---|
| WB 选品分析工具 | v0.5.1 | 分析 WB 搜索请求表，生成类目词簇、属性表现、品牌维度、下单/搜索对比和选品报告 | `tools/wb-selection-mvp/` |
| Yandex Wordstat MVP | v0.6 | 分析 Yandex Wordstat 关键词、特征词、生活场景和扩展种子词 | `tools/yandex-wordstat-mvp/` |

## 当前目录结构

```text
wb-gpt-mvp/
├─ README.md
├─ docs/
│  └─ repository-guide.md
├─ tools/
│  ├─ wb-selection-mvp/
│  │  ├─ README.md
│  │  ├─ CHANGELOG.md
│  │  ├─ latest.json
│  │  └─ versions/
│  │     └─ v0.5.1/
│  │        ├─ README.md
│  │        ├─ RELEASE_NOTES.md
│  │        ├─ QA_TEST_REPORT.md
│  │        ├─ ARTIFACT.md
│  │        └─ api_settings.example.json
│  └─ yandex-wordstat-mvp/
│     ├─ README.md
│     ├─ CHANGELOG.md
│     ├─ latest.json
│     └─ versions/
│        └─ v0.6/
│           ├─ README.md
│           ├─ RELEASE_NOTES.md
│           └─ LEGACY_FILES.md
├─ yandex_wordstat_mvp.py        # Yandex 旧版兼容入口，暂保留
├─ run_windows.bat               # Yandex 旧版兼容入口，暂保留
└─ .gitignore
```

## 版本管理规则

每个工具建议使用：

```text
tools/<tool-name>/versions/v<major>.<minor>.<patch>/
```

例如：

```text
tools/wb-selection-mvp/versions/v0.5.1/
tools/yandex-wordstat-mvp/versions/v0.6/
```

每个版本至少保留：

- `README.md`：版本使用说明；
- `RELEASE_NOTES.md`：本版本变化；
- `QA_TEST_REPORT.md`：已测试内容，如适用；
- 如通过本地方式上传完整工具包，可放置对应 zip 或源码目录。

## 关于根目录旧文件

Yandex Wordstat MVP v0.6 的实际可运行文件仍保留在根目录，避免破坏旧入口：

```text
yandex_wordstat_mvp.py
run_windows.bat
source_parts/
seeds_lifestyle_ru.txt
seeds_product_ru.txt
seeds_context_ru.txt
seed_bank_ru_cn.csv
README_使用说明.txt
```

对应说明已整理到：

```text
tools/yandex-wordstat-mvp/versions/v0.6/LEGACY_FILES.md
```

## 安全提醒

不要提交以下内容：

- API Key；
- `api_settings.json` 中带真实密钥的版本；
- WB 原始业务数据；
- 工具运行生成的 `results/`、`input/`、`category_cache/` 等本地缓存；
- 含客户、订单、广告后台隐私信息的文件。

## 当前说明

最新 WB 选品工具版本为 **v0.5.1**。由于当前连接器写入 GitHub 时更适合文本文件，完整 zip 包建议通过本地 Git / GitHub 网页 Release 上传；本仓库已先建立长期维护结构、版本说明和上传规范。
