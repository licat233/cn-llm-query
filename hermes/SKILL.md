---
name: cn-llm-query
description: 查询国内主流大模型的官方地址、模型标识、免费权益，支持场景推荐、调用代码生成和自学习扩展
version: 1.4.0
author: licat
metadata:
  hermes:
    tags: [mlops, models, LLM, API, 国内大模型, 中国]
---

# 国内大模型查询工具

查询国内 12 家主流大模型厂商的 API 地址、模型列表、免费额度，支持场景推荐和调用代码生成。

## When to Use

用户询问以下内容时触发：
- 国内大模型 API 地址、base_url
- 某个厂商的模型列表（如 DeepSeek、小米 MiMo、通义千问）
- 免费大模型推荐
- 特定场景的模型推荐（代码开发、长上下文、多模态等）
- 如何调用某个国内大模型
- 模型标识（model id）查询

## 数据库

内置 12 家厂商数据：
- 美团 LongCat、小米 MiMo、DeepSeek、智谱 AI、阿里云通义千问
- 月之暗面 Kimi、字节跳动豆包、腾讯混元、百度文心一言
- 零一万物 Yi、InclusionAI 灵犀、MiniMax

数据文件：`main.py` 中的 `LLM_DATABASE` 和 `user_providers.json`（自学习数据）

## Quick Reference

```bash
# 查询厂商信息
python main.py <<< '{"action":"query_info","provider":"DeepSeek"}'

# 按场景推荐
python main.py <<< '{"action":"recommend","scene":"免费日常使用"}'

# 生成调用代码
python main.py <<< '{"action":"get_code","provider":"小米MiMo","model_name":"mimo-v2.5-pro"}'

# 自学习：写入新厂商数据
python main.py <<< '{"action":"learn","provider_data":{...}}'
```

## Procedure

### 1. 查询厂商/模型信息

```bash
cd ~/.hermes/skills/mlops/models/cn_llm_query
echo '{"action":"query_info","provider":"厂商名"}' | python main.py
```

可选参数：
- `provider`: 厂商名称（必填）
- `model_name`: 具体模型标识（选填，用于筛选）
- `protocol`: API 协议，`openai` 或 `anthropic`（默认 openai）
- `pay_type`: 付费类型，`general` 或 `enterprise`（默认 general）

### 2. 场景推荐

```bash
echo '{"action":"recommend","scene":"代码开发"}' | python main.py
```

可选场景：
- 免费日常使用、代码开发、长上下文处理
- 多模态/视觉、视频生成、开源本地化部署
- 企业级高并发、推理/数学计算、文学/长文本创作

### 3. 生成调用代码

```bash
echo '{"action":"get_code","provider":"DeepSeek","model_name":"deepseek-v4-flash"}' | python main.py
```

### 4. 自学习（写入新厂商数据）

```bash
echo '{"action":"learn","provider_data":{"provider":"新厂商","models":[{"id":"model-id","name":"模型名","desc":"描述"}],"base_url":{"openai":{"general":"url"}}}}' | python main.py
```

数据保存在 `user_providers.json`，下次查询自动合并。

## Pitfalls

- 厂商名称需要包含关键词匹配（如"DeepSeek"可以匹配"DeepSeek（深度求索）"）
- `learn` action 的 `provider_data` 必须包含 `provider`、`models`、`base_url` 三个字段
- 国内业务请使用带 `/cn` 的合规节点（如 DeepSeek）

## Verification

查询成功会返回格式化的厂商信息，包含 API 地址、模型列表、官网和备注。
查询失败会返回提示信息，引导用户使用 `learn` action 补充数据。
