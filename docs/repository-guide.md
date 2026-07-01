# 仓库维护规范

这个仓库用于集中保存多个 WB / 俄罗斯电商相关 MVP 工具。

## 一、工具目录规范

每个工具使用一个独立目录：

```text
tools/<tool-name>/
```

示例：

```text
tools/wb-selection-mvp/
tools/yandex-wordstat-mvp/
```

每个工具目录建议包含：

```text
README.md
CHANGELOG.md
latest.json
versions/
```

## 二、版本目录规范

每个版本放在：

```text
tools/<tool-name>/versions/v<major>.<minor>.<patch>/
```

例如：

```text
tools/wb-selection-mvp/versions/v0.5.1/
```

版本目录至少包含：

- `README.md`：本版本使用说明；
- `RELEASE_NOTES.md`：版本变化；
- `QA_TEST_REPORT.md`：测试记录；
- 可选：完整 zip 包、源码目录或安装包。

## 三、命名规范

工具名称建议使用英文短横线：

```text
wb-selection-mvp
yandex-wordstat-mvp
```

版本号使用：

```text
v0.5.1
v0.6.0
v1.0.0
```

## 四、不要提交的内容

以下内容不要提交到仓库：

- API Key；
- 带真实密钥的 `api_settings.json`；
- WB 原始导出表；
- 运行结果 `results/`；
- 本地缓存 `category_cache/`；
- 待分析文件夹 `input/`；
- 任何客户、订单、广告后台隐私数据。

## 五、推荐上传流程

新增工具版本时：

1. 在本地确认工具可以运行；
2. 删除运行结果、缓存、API Key；
3. 添加版本目录；
4. 更新工具目录下的 `latest.json`；
5. 更新 `CHANGELOG.md`；
6. 更新根目录 `README.md` 的工具索引。

## 六、二进制文件建议

zip、exe、图片等二进制文件建议优先用 GitHub Release 上传。

如果必须放入仓库，应注意：

- 不要提交过大的运行结果；
- 不要提交含密钥的配置；
- 保持版本命名清晰。
