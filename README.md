# cn-llm-query

国内主流大模型 API 信息查询 Skill，支持 Claude Code 和 Hermes Agent。

## 功能

- **信息查询**：查询 12 家国内主流大模型的官方 API 地址、模型标识、免费权益
- **场景推荐**：按使用场景（免费、代码、长上下文、多模态等）推荐最佳模型
- **代码生成**：一键生成 OpenAI / Anthropic 协议的调用代码
- **自动配置**：提供 API Key 后自动写入 .env 配置
- **自学习**：查不到的厂商会提示在线搜索，搜索后自动写入数据库

## 内置厂商（12 家）

| 厂商 | 代表模型 | 特色 |
|------|---------|------|
| 美团 LongCat | longcat-2.0-preview | 国产算力、Agent 优化 |
| 小米 MiMo | mimo-v2.5-pro | 免费额度、代码强 |
| DeepSeek | deepseek-v4-flash | 免费 50 万/天、推理强 |
| 智谱 AI | glm-4.6-flash | 免费 100 万/天、Agent 优化 |
| 通义千问 | qwen3.6-72b-instruct | 开源、企业级高并发 |
| Kimi | kimi-k2.6-long | 1000 万 Token 上下文 |
| 豆包 | doubao-4.0-pro | 中文理解强、字节生态 |
| 腾讯混元 | hunyuan-4.0 | 金融合规 |
| 百度文心 | ernie-4.5-pro | 搜索联动 |
| 零一万物 | yi-4.0-34b-instruct | 端侧部署 |
| InclusionAI | ling-2.6-1t-instruct | 长文本创作 |
| MiniMax | abab-7 | 视频生成 |

## 使用方式

### Claude Code

将 `claude-code/SKILL.md` 复制到 `~/.claude/skills/cn-llm-query/SKILL.md`：

```bash
mkdir -p ~/.claude/skills/cn-llm-query
cp claude-code/SKILL.md ~/.claude/skills/cn-llm-query/
```

### Hermes Agent

将 `hermes/` 下的文件复制到 `~/.hermes/skills/mlops/models/cn_llm_query/`：

```bash
mkdir -p ~/.hermes/skills/mlops/models/cn_llm_query
cp hermes/* ~/.hermes/skills/mlops/models/cn_llm_query/
```

## 版本

- v1.4.0 — 新增自学习能力（learn action），查不到的厂商可在线搜索后写入数据库
