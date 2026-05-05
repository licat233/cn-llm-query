---
name: cn-llm-query
description: '查询国内主流大模型的官方地址、模型标识、体验入口、免费权益等信息，支持场景化推荐和调用代码生成。触发词：国内大模型、API地址、base_url、模型标识、调用示例、大模型推荐、免费大模型、LongCat、MiMo、DeepSeek、通义千问、智谱、Kimi、豆包、混元、文心一言、零一万物、InclusionAI、MiniMax'
license: MIT
metadata:
  author: licat
  version: "1.4.0"
  update_time: "2026-05-05"
  data_source: 各厂商官方公开开发者文档
---

# 国内主流大模型 API 信息查询

查询国内主流大模型的官方 API 地址、模型标识、体验入口、免费权益等信息。支持按厂商查询、按场景推荐、生成调用代码。

**核心特性：** 全量数据内置，离线可用，无数据泄露风险，纯本地计算。

## 使用方式

用户可能提出以下类型的问题：
- **查询信息**：「LongCat 的 API 地址是什么」「DeepSeek 有哪些模型」
- **场景推荐**：「推荐一个免费的大模型」「代码开发用哪个模型好」
- **调用示例**：「给我 MiMo 的 OpenAI 调用代码」「DeepSeek 怎么接入」
- **自动配置**：「这是我的 DeepSeek API Key，帮我配好」「我买了 Kimi 的 API，帮我写进 .env」

默认协议为 OpenAI，付费类型为通用按量（general）。如用户指定 Anthropic 协议或企业包量，按需切换。

---

## 核心数据（12 家厂商）

### 1. 美团 LongCat（龙猫）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `longcat-2.0-preview` | 旗舰万亿参数版 | 1M Token 上下文，Agent/长文本能力突出，需申请测试资格 |
| `longcat-flash-thinking-2601` | 重思考智能体版 | 开源，推理能力开源 SOTA |
| `longcat-flash-chat-560b` | 轻量高性价比版 | 开源，平均激活参数仅 270 亿，推理速度快 |
| `longcat-image` | 图像生成编辑版 | 开源，中文渲染精度领先 |
| `longcat-video` | 视频生成版 | 开源，支持 5 分钟级长视频生成 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.longcat.chat/openai` | 官方文档企业服务板块查询 |
| Anthropic | `https://api.longcat.chat/anthropic` | 官方文档企业服务板块查询 |

- **官网：** https://longcat.ai / https://longcat.chat（开发者文档）
- **体验入口：** https://longcat.ai
- **标签：** 国产算力、长上下文、Agent 优化、开源、多模态、视频生成、免费测试额度
- **备注：** 全系列模型全流程依托国产算力训练，测试阶段个人用户可领取免费调用额度，开源模型可在 ModelScope/Hugging Face 下载权重本地化部署

---

### 2. 小米 Xiaomi MiMo

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `mimo-v2.5-instruct` | 通用对话版 | 日常场景通用 |
| `mimo-v2.5-pro` | 旗舰性能版 | 复杂任务适用 |
| `mimo-v2.5-vision` | 多模态视觉版 | 图像理解/解析 |
| `mimo-v2.5-coder` | 代码专属版 | 代码开发/调试 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.xiaomimimo.com/v1` | `https://token-plan-cn.xiaomimimo.com/v1` |
| Anthropic | `https://api.xiaomimimo.com/anthropic` | `https://token-plan-cn.xiaomimimo.com/anthropic` |

- **官网：** https://www.xiaomimimo.com
- **体验入口：** https://chat.xiaomimimo.com
- **标签：** 免费额度、多模态、代码强、个人易接入
- **备注：** 新用户注册送 1000 万 Token 免费额度，支持个人/企业零门槛开通

---

### 3. DeepSeek（深度求索）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `deepseek-v4-flash` | 免费极速版 | 日常场景通用，每天 50 万免费 Token |
| `deepseek-v4-pro` | 旗舰版 | 复杂推理/编程场景适用 |
| `deepseek-v4-coder` | 代码专属版 | 代码开发/调试能力业内领先 |
| `deepseek-v4-vision` | 多模态视觉版 | 图像理解/解析 |
| `deepseek-r1` | 数学/逻辑推理专属版 | 奥数/逻辑题能力突出 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.deepseek.com/cn/v1` | `https://enterprise-api.deepseek.com/cn/v1` |
| Anthropic | `https://api.deepseek.com/cn/anthropic` | `https://enterprise-api.deepseek.com/cn/anthropic` |

- **官网：** https://www.deepseek.com
- **体验入口：** https://chat.deepseek.com/cn
- **标签：** 免费、代码强、推理强、多模态、个人易接入
- **备注：** V4-Flash 模型每天提供 50 万免费 Token，无调用频率限制，国内业务请使用带 /cn 的合规节点

---

### 4. 智谱 AI（清华系）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `glm-5.1-preview` | 新一代预览版 | 综合能力全面升级 |
| `glm-4.6-flagship` | 旗舰版 | 编码/Agent 能力突出，适配国产算力 |
| `glm-4.6-air` | 高性价比版 | 平衡性能与成本，通用场景适用 |
| `glm-4.6-flash` | 免费极速版 | 日常场景通用，每天 100 万免费 Token |
| `glm-4.6-vision` | 多模态视觉版 | 图像理解/解析 |
| `glm-4-long` | 超长输入版 | 1M 上下文，4K 最大输出 |

**图像/视频生成：** `cogview-4`（图像生成）、`cogview-3-flash`（免费图像生成）、`cogvideox-3`（视频生成旗舰）、`cogvideox-flash`（免费视频生成）

**其他：** `codegeex-4`（代码，128K/32K）、`embedding-3`（向量）、`rerank`（重排序）

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://open.bigmodel.cn/api/paas/v4` | `https://enterprise.bigmodel.cn/api/paas/v4` |
| Anthropic | `https://open.bigmodel.cn/api/paas/anthropic` | `https://enterprise.bigmodel.cn/api/paas/anthropic` |

- **官网：** https://www.zhipuai.cn
- **体验入口：** https://chatglm.cn
- **标签：** 免费、国产算力适配、代码强、Agent 优化、多模态、视频生成
- **备注：** GLM-4.6-Flash 每天提供 100 万免费 Token，教育用户享额外 30% 额度补贴，支持国产硬件部署

---

### 5. 阿里云通义千问（Qwen 系列）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `qwen3.6-72b-instruct` | 旗舰版 | 复杂任务适用，综合能力领先 |
| `qwen3.6-27b-instruct` | 高性价比版 | 平衡性能与成本，通用场景适用 |
| `qwen3.6-7b-instruct` | 轻量版 | 低资源场景适用，推理速度快 |
| `qwen3.6-vision` | 多模态视觉版 | 图像理解/解析 |
| `qwen3.6-coder` | 代码专属版 | 代码开发/调试 |
| `qwen3.5-omni-plus` | 全模态版 | 支持文本、图像、语音理解与生成 |
| `qwen-long` | 长文本版 | 超长上下文处理 |

**向量与重排序：** `text-embedding-v4`、`tongyi-embedding-vision-plus`、`qwen3-rerank`

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `https://{资源池ID}.dashscope.aliyuncs.com/compatible-mode/v1` |
| Anthropic | `https://dashscope.aliyuncs.com/anthropic` | `https://{资源池ID}.dashscope.aliyuncs.com/anthropic` |

- **官网：** https://tongyi.aliyun.com
- **体验入口：** https://tongyi.aliyun.com/qianwen
- **标签：** 免费额度、代码强、多模态、开源、企业级高并发
- **备注：** 新用户送 500 万 Token 免费额度，支持离线部署 License 申请，全系列模型开源可本地化部署

---

### 6. 月之暗面 Kimi

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `kimi-k2.6` | 通用旗舰版 | 综合能力领先，长文本处理能力突出 |
| `kimi-k2.6-vision` | 多模态视觉版 | 图像理解/解析 |
| `kimi-k2.6-coder` | 代码专属版 | 代码开发/调试 |
| `kimi-k2.6-long` | 长上下文版 | 支持 1000 万 Token 上下文，单次可处理千万字文档 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.moonshot.cn/v1` | `https://enterprise-api.moonshot.cn/v1` |
| Anthropic | `https://api.moonshot.cn/anthropic` | `https://enterprise-api.moonshot.cn/anthropic` |

- **官网：** https://www.moonshot.cn
- **体验入口：** https://kimi.moonshot.cn
- **标签：** 免费额度、长上下文、多模态、代码强
- **备注：** 免费额度为每月 1000 万 Token，支持最长 1 亿 Token 上下文调用，长文本处理能力业内领先

---

### 7. 字节跳动豆包

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `doubao-4.0-pro` | 旗舰版 | 综合能力领先，中文理解能力突出 |
| `doubao-4.0-flash` | 极速版 | 高并发场景适用，推理速度快 |
| `doubao-4.0-vision` | 多模态视觉版 | 图像理解/解析 |
| `doubao-4.0-coder` | 代码专属版 | 代码开发/调试 |
| `doubao-4.0-long` | 长上下文版 | 支持 500 万 Token 上下文 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.doubao.com/v1` | `https://enterprise-api.doubao.com/v1` |
| Anthropic | `https://api.doubao.com/anthropic` | `https://enterprise-api.doubao.com/anthropic` |

- **官网：** https://www.doubao.com
- **体验入口：** https://www.doubao.com/chat
- **标签：** 免费额度、中文理解强、多模态、代码强、企业级高并发
- **备注：** 新用户注册送 2000 万 Token 免费额度，支持字节生态工具一键打通，抖音/飞书数据联动

---

### 8. 腾讯混元

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `hunyuan-5.0-preview` | 新一代预览版 | 综合能力全面升级 |
| `hunyuan-4.0` | 通用旗舰版 | 综合能力领先，金融级安全合规 |
| `hunyuan-4.0-vision` | 多模态视觉版 | 图像理解/解析 |
| `hunyuan-4.0-coder` | 代码专属版 | 代码开发/调试 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.hunyuan.tencent.com/v1` | `https://{资源组ID}.hunyuan.tencent.com/v1` |
| Anthropic | `https://api.hunyuan.tencent.com/anthropic` | `https://{资源组ID}.hunyuan.tencent.com/anthropic` |

- **官网：** https://hunyuan.tencent.com
- **体验入口：** https://hunyuan.tencent.com/chat
- **标签：** 免费额度、金融合规、多模态、代码强、企业级高并发
- **备注：** 新用户送 1500 万 Token 免费额度，金融级数据安全合规，支持腾讯云生态联动

---

### 9. 百度文心一言（千帆平台）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `ernie-5.0-preview` | 新一代预览版 | 综合能力全面升级 |
| `ernie-4.5-pro` | 旗舰版 | 中文理解能力突出，支持搜索实时接入 |
| `ernie-4.5-turbo` | 极速版 | 高并发场景适用，推理速度快 |
| `ernie-4.5-vision` | 多模态视觉版 | 图像理解/解析 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://qianfan.baidubce.com/compatible/v1` | `https://{实例ID}.qianfan.baidubce.com/compatible/v1` |
| Anthropic | `https://qianfan.baidubce.com/anthropic` | `https://{实例ID}.qianfan.baidubce.com/anthropic` |

- **官网：** https://yiyan.baidu.com
- **体验入口：** https://yiyan.baidu.com
- **标签：** 免费额度、中文理解强、搜索联动、多模态、企业级高并发
- **备注：** 新用户送 800 万 Token 免费额度，支持百度搜索实时接入，国内合规性领先

---

### 10. 零一万物（Yi 大模型）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `yi-4.0-34b-instruct` | 旗舰版 | 综合能力突出，长文本处理能力强 |
| `yi-4.0-9b-instruct` | 轻量版 | 低资源场景适用，可端侧部署 |
| `yi-4.0-vision` | 多模态视觉版 | 图像理解/解析 |
| `yi-4.0-long` | 长上下文版 | 支持 2000 万 Token 上下文 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.lingyiwanwu.com/v1` | `https://enterprise-api.lingyiwanwu.com/v1` |
| Anthropic | `https://api.lingyiwanwu.com/anthropic` | `https://enterprise-api.lingyiwanwu.com/anthropic` |

- **官网：** https://www.lingyiwanwu.com
- **体验入口：** https://chat.lingyiwanwu.com
- **标签：** 免费额度、长上下文、开源、端侧部署
- **备注：** 免费额度为每月 500 万 Token，支持轻量化端侧部署，全系列模型开源可本地化部署

---

### 11. InclusionAI（灵犀大模型）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `ling-2.6-1t-instruct` | 旗舰文本生成版 | 1T 参数，长文本/文学创作能力突出 |
| `ling-2.6-vision` | 多模态视觉版 | 图像理解/解析 |
| `ling-2.6-code` | 代码专属版 | 代码开发/调试 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.inclusionai.com/v1` | `https://enterprise-api.inclusionai.com/v1` |
| Anthropic | `https://api.inclusionai.com/anthropic` | `https://enterprise-api.inclusionai.com/anthropic` |

- **官网：** https://www.inclusionai.cn
- **体验入口：** https://chat.inclusionai.cn
- **标签：** 免费额度、长文本创作、多模态、代码强
- **备注：** 新用户注册送 200 万 Token 免费额度，主打长文本/文学创作场景，中文生成能力领先

---

### 12. MiniMax（稀宇科技 / 海螺 AI）

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `abab-7` | 通用旗舰版 | 综合能力领先，多模态能力突出 |
| `minimax-01` | 轻量高性价比版 | 低资源场景适用，推理速度快 |
| `minimax-vision` | 多模态视觉版 | 图像理解/解析 |
| `minimax-video` | 视频生成版 | 支持短视频生成，效果业内领先 |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `https://api.minimax.chat/v1` | 官方文档企业服务板块查询 |
| Anthropic | `https://api.minimax.chat/anthropic` | 官方文档企业服务板块查询 |

- **官网：** https://www.minimax.chat
- **体验入口：** https://hailuoai.com（海螺 AI）
- **标签：** 免费额度、多模态、视频生成、代码强
- **备注：** 新用户送 500 万 Token 免费额度，视频生成能力突出，支持多模态混合输入

---

## 场景推荐

当用户请求推荐时，按以下场景匹配标签：

| 场景 | 匹配标签 | 推荐（优先级从高到低） |
|------|---------|----------------------|
| 免费日常使用 | 免费 | DeepSeek V4-Flash（50万/天）> 智谱 GLM-4.6-Flash（100万/天）> 其他有免费额度厂商 |
| 代码开发 | 代码强 | DeepSeek Coder > 小米 MiMo Coder > 智谱 CodeGeeX-4 |
| 长上下文处理 | 长上下文 | Kimi K2.6-Long（1000万Token）> 零一万物 Yi-4.0-Long（2000万Token）> LongCat（1M）> 智谱 GLM-4-Long（1M） |
| 多模态/视觉 | 多模态 | 智谱 GLM-4.6-V > 通义千问 Qwen3.6-Vision > DeepSeek Vision |
| 视频生成 | 视频生成 | MiniMax Video > LongCat Video > 智谱 CogVideoX |
| 开源本地化部署 | 开源 | LongCat 开源系列 > 通义千问 Qwen 开源 > 零一万物 Yi 开源 |
| 企业级高并发 | 企业级高并发 | 通义千问 > 豆包 > 腾讯混元 > 百度千帆 |
| 推理/数学计算 | 推理强 | DeepSeek R1 > LongCat Flash Thinking |
| 文学/长文本创作 | 长文本创作 | InclusionAI 灵犀（1T参数）> Kimi K2.6-Long |

---

## 调用代码生成

### OpenAI 协议模板（适用于所有厂商）

```python
from openai import OpenAI

client = OpenAI(
    api_key="<在厂商官网申请的 API Key>",
    base_url="{base_url}"
)

response = client.chat.completions.create(
    model="{model_id}",
    messages=[{"role": "user", "content": "你的问题"}]
)
print(response.choices[0].message.content)
```

### Anthropic 协议模板

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="<在厂商官网申请的 API Key>",
    base_url="{base_url}"
)

response = client.messages.create(
    model="{model_id}",
    max_tokens=1024,
    messages=[{"role": "user", "content": "你的问题"}]
)
print(response.content[0].text)
```

### 生成规则

当用户请求调用代码时：
1. 确认厂商、模型 ID、协议（默认 OpenAI）、付费类型（默认 general）
2. 从上方数据表中查找对应的 base_url
3. 将 base_url 和 model_id 填入模板
4. 在代码注释中标注 API Key 获取来源

---

## 自动配置能力

当用户提供 API Key 并要求配置时，按以下流程操作：

### 识别厂商

根据用户声明或 API Key 特征识别厂商：

| 厂商 | Key 特征（参考） |
|------|-----------------|
| DeepSeek | `sk-` 开头 |
| 智谱 AI | `glm-` 或 `zhipuai-` 开头 |
| 通义千问 | `sk-` 开头（阿里云 DashScope） |
| Kimi | `sk-` 开头（Moonshot） |
| 豆包 | 火山方舟格式 |
| 其他 | 以用户声明为准 |

如果无法自动识别，直接询问用户是哪家厂商。

### 配置写入

根据项目类型，选择合适的配置方式：

**方式一：`.env` 文件（最常见）**

```env
# {厂商名} API 配置
OPENAI_API_KEY={用户提供的Key}
OPENAI_BASE_URL={对应厂商的base_url}
DEFAULT_MODEL={推荐的模型ID}
```

如用户需要 Anthropic 协议：

```env
# {厂商名} API 配置（Anthropic 协议）
ANTHROPIC_API_KEY={用户提供的Key}
ANTHROPIC_BASE_URL={对应厂商的anthropic base_url}
DEFAULT_MODEL={推荐的模型ID}
```

**方式二：项目配置文件**

根据项目实际使用的框架，写入对应配置文件：
- Python 项目：`.env` 或 `config.py` 或 `settings.yaml`
- Node.js 项目：`.env` 或 `config.json`
- Claude Code 项目：`.claude/settings.json` 中的 `env` 字段

### 操作步骤

1. **识别厂商和协议**：从用户输入中提取，或询问
2. **查找 base_url 和推荐模型**：从上方核心数据表中获取
3. **检查项目结构**：用 `ls` 和 `Read` 确认项目类型和已有配置文件
4. **写入配置**：用 `Edit` 或 `Write` 工具写入，保留已有配置不覆盖
5. **告知用户**：写入后显示写入了哪些字段、对应什么值，方便用户确认

### 注意事项

- **不要在回复中回显完整的 API Key**，只显示前 4 位和后 4 位（如 `sk-a1b2...x8y9`）
- 如果 `.env` 已存在，用 `Edit` 追加而非覆盖
- 如果 `.gitignore` 中没有 `.env`，提醒用户添加
- 企业地址含占位符的（如 `{资源池ID}`），提醒用户替换

---

## 自学习能力（自动扩充数据库）

当用户查询的厂商/模型在上方数据中找不到时，自动触发在线查询并更新 skill，下次直接命中。

### 触发条件

以下情况触发自学习：
- 用户查询的厂商名称不在 12 家已知厂商中
- 用户查询的模型 ID 在已知厂商中找不到
- 用户主动要求添加新厂商/新模型

### 处理流程

1. **在线搜索**：用 WebSearch 搜索该厂商的官方开发者文档，获取：
   - 官方 API base_url（OpenAI / Anthropic 协议）
   - 主流模型列表及 model ID
   - 免费额度政策
   - 官方网站和体验入口
2. **信息验证**：优先从厂商官方文档获取，交叉验证关键字段（base_url 必须是 https 官方域名）
3. **写入 skill 文件**：用 Edit 工具将新厂商数据追加到 SKILL.md 的「核心数据」章节，格式与已有厂商一致
4. **同步 Hermes**：如果 Hermes 侧也有对应 skill，同步更新 `~/.hermes/skills/mlops/models/cn_llm_query/main.py` 中的 `LLM_DATABASE`
5. **回复用户**：告知查询结果，并说明已自动更新 skill，下次可直接查询

### 新厂商数据模板

```markdown
### {序号}. {厂商名称}

| 模型 ID | 名称 | 说明 |
|---------|------|------|
| `{model_id}` | {名称} | {说明} |

| 协议 | 通用（general） | 企业（enterprise） |
|------|----------------|-------------------|
| OpenAI | `{base_url}` | `{enterprise_url}` |
| Anthropic | `{base_url}` | `{enterprise_url}` |

- **官网：** {url}
- **体验入口：** {url}
- **标签：** {标签}
- **备注：** {备注}
```

### 注意事项

- 只写入从官方文档确认的信息，不确定的字段标注「待确认」
- base_url 必须是厂商官方域名，不使用第三方代理地址
- 更新后在 frontmatter 中递增 version 号
- 如果搜索不到可靠信息，告知用户「未找到该厂商的官方 API 信息，请提供官方文档链接」

---

## 使用规范

1. **数据准确性**：所有信息来自各厂商官方公开文档，如用户反馈信息过时，建议用户核实官方最新文档
2. **合规提示**：返回结果时提醒用户「国内业务请使用备案节点，API Key 需自行在官方申请」
3. **海外节点**：仅 DeepSeek 明确提供海外节点（`https://api.deepseek.com/v1`，无 /cn），且仅适用于出海业务
4. **免费额度**：各厂商免费政策可能调整，建议用户以官方最新公告为准
5. **企业地址**：含 `{资源池ID}`、`{资源组ID}`、`{实例ID}` 占位符的地址，需用户在对应云控制台创建后替换
