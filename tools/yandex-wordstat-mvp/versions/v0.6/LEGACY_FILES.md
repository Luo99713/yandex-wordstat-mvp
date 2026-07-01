# Legacy root files

Yandex Wordstat MVP v0.6 的实际可运行文件目前仍保留在仓库根目录。

## 根目录旧文件

```text
yandex_wordstat_mvp.py
run_windows.bat
source_parts/source.b64.part01
source_parts/source.b64.part02
source_parts/source.b64.part03
source_parts/source.b64.part04
source_parts/source.b64.part05
seeds_lifestyle_ru.txt
seeds_product_ru.txt
seeds_context_ru.txt
seed_bank_ru_cn.csv
README_使用说明.txt
```

## 为什么暂时不移动

`yandex_wordstat_mvp.py` 当前会从自身所在目录读取：

```text
source_parts/source.b64.partXX
```

如果直接移动文件，旧入口可能失效。因此本次整理先建立标准版本目录和索引，同时保留根目录旧入口。

## 后续完全迁移方案

如果需要彻底迁移，可以：

1. 将上面的旧文件复制到 `tools/yandex-wordstat-mvp/versions/v0.6/`；
2. 修改 launcher 里的 `parts_dir` 路径；
3. 更新根目录 `run_windows.bat` 为跳转到新路径；
4. 再删除根目录旧文件。
