import json
import sys
import os

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
USER_PROVIDERS_FILE = os.path.join(SKILL_DIR, "user_providers.json")


def load_user_providers():
    """从外部JSON文件加载用户自学习的厂商数据"""
    if not os.path.exists(USER_PROVIDERS_FILE):
        return []
    try:
        with open(USER_PROVIDERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_user_providers(providers):
    """将用户自学习的厂商数据写入外部JSON文件"""
    with open(USER_PROVIDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(providers, f, ensure_ascii=False, indent=2)


def get_all_providers():
    """合并内置数据库和用户自学习数据"""
    return LLM_DATABASE + load_user_providers()


# 内置全量12家国内主流大模型数据
LLM_DATABASE = [
    # 1. 美团LongCat（龙猫）
    {
        "provider": "美团LongCat（龙猫）",
        "models": [
            {"id": "longcat-2.0-preview", "name": "旗舰万亿参数版", "desc": "1M Token上下文，Agent/长文本能力突出，需申请测试资格"},
            {"id": "longcat-flash-thinking-2601", "name": "重思考智能体版", "desc": "开源，推理能力开源SOTA"},
            {"id": "longcat-flash-chat-560b", "name": "轻量高性价比版", "desc": "开源，平均激活参数仅270亿，推理速度快"},
            {"id": "longcat-image", "name": "图像生成编辑版", "desc": "开源，中文渲染精度领先"},
            {"id": "longcat-video", "name": "视频生成版", "desc": "开源，支持5分钟级长视频生成"}
        ],
        "base_url": {
            "openai": {"general": "https://api.longcat.chat/openai", "enterprise": "请在官方文档企业服务板块查询专属地址"},
            "anthropic": {"general": "https://api.longcat.chat/anthropic", "enterprise": "请在官方文档企业服务板块查询专属地址"}
        },
        "official_site": ["https://longcat.ai", "https://longcat.chat（开发者文档）"],
        "chat_url": "https://longcat.ai",
        "tags": ["国产算力", "长上下文", "Agent优化", "开源", "多模态", "视频生成", "免费测试额度"],
        "remark": "全系列模型全流程依托国产算力训练，测试阶段个人用户可领取免费调用额度，开源模型可在ModelScope/Hugging Face下载权重本地化部署"
    },
    # 2. 小米（Xiaomi MiMo）
    {
        "provider": "小米（Xiaomi MiMo）",
        "models": [
            {"id": "mimo-v2.5-instruct", "name": "通用对话版", "desc": "日常场景通用"},
            {"id": "mimo-v2.5-pro", "name": "旗舰性能版", "desc": "复杂任务适用"},
            {"id": "mimo-v2.5-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "mimo-v2.5-coder", "name": "代码专属版", "desc": "代码开发/调试"}
        ],
        "base_url": {
            "openai": {"general": "https://api.xiaomimimo.com/v1", "enterprise": "https://token-plan-cn.xiaomimimo.com/v1"},
            "anthropic": {"general": "https://api.xiaomimimo.com/anthropic", "enterprise": "https://token-plan-cn.xiaomimimo.com/anthropic"}
        },
        "official_site": "https://www.xiaomimimo.com",
        "chat_url": "https://chat.xiaomimimo.com",
        "tags": ["免费额度", "多模态", "代码强", "个人易接入"],
        "remark": "新用户注册送1000万Token免费额度，支持个人/企业零门槛开通"
    },
    # 3. DeepSeek（深度求索）
    {
        "provider": "DeepSeek（深度求索）",
        "models": [
            {"id": "deepseek-v4-flash", "name": "免费极速版", "desc": "日常场景通用，每天50万免费Token"},
            {"id": "deepseek-v4-pro", "name": "旗舰版", "desc": "复杂推理/编程场景适用"},
            {"id": "deepseek-v4-coder", "name": "代码专属版", "desc": "代码开发/调试能力业内领先"},
            {"id": "deepseek-v4-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "deepseek-r1", "name": "数学/逻辑推理专属版", "desc": "奥数/逻辑题能力突出"}
        ],
        "base_url": {
            "openai": {"general": "https://api.deepseek.com/cn/v1", "enterprise": "https://enterprise-api.deepseek.com/cn/v1"},
            "anthropic": {"general": "https://api.deepseek.com/cn/anthropic", "enterprise": "https://enterprise-api.deepseek.com/cn/anthropic"}
        },
        "official_site": "https://www.deepseek.com",
        "chat_url": "https://chat.deepseek.com/cn",
        "tags": ["免费", "代码强", "推理强", "多模态", "个人易接入"],
        "remark": "V4-Flash模型每天提供50万免费Token，无调用频率限制，国内业务请使用带/cn的合规节点"
    },
    # 4. 智谱AI（清华系）
    {
        "provider": "智谱AI（清华系）",
        "models": [
            {"id": "glm-5.1-preview", "name": "新一代预览版", "desc": "综合能力全面升级"},
            {"id": "glm-4.6-flagship", "name": "旗舰版", "desc": "编码/Agent能力突出，适配国产算力"},
            {"id": "glm-4.6-air", "name": "高性价比版", "desc": "平衡性能与成本，通用场景适用"},
            {"id": "glm-4.6-flash", "name": "免费极速版", "desc": "日常场景通用，每天100万免费Token"},
            {"id": "glm-4.6-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "glm-4-long", "name": "超长输入版", "desc": "1M上下文，4K最大输出"}
        ],
        "base_url": {
            "openai": {"general": "https://open.bigmodel.cn/api/paas/v4", "enterprise": "https://enterprise.bigmodel.cn/api/paas/v4"},
            "anthropic": {"general": "https://open.bigmodel.cn/api/paas/anthropic", "enterprise": "https://enterprise.bigmodel.cn/api/paas/anthropic"}
        },
        "official_site": "https://www.zhipuai.cn",
        "chat_url": "https://chatglm.cn",
        "tags": ["免费", "国产算力适配", "代码强", "Agent优化", "多模态", "视频生成"],
        "remark": "GLM-4.6-Flash每天提供100万免费Token，教育用户享额外30%额度补贴，支持国产硬件部署"
    },
    # 5. 阿里云（通义千问）
    {
        "provider": "阿里云（通义千问）",
        "models": [
            {"id": "qwen3.6-72b-instruct", "name": "旗舰版", "desc": "复杂任务适用，综合能力领先"},
            {"id": "qwen3.6-27b-instruct", "name": "高性价比版", "desc": "平衡性能与成本，通用场景适用"},
            {"id": "qwen3.6-7b-instruct", "name": "轻量版", "desc": "低资源场景适用，推理速度快"},
            {"id": "qwen3.6-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "qwen3.6-coder", "name": "代码专属版", "desc": "代码开发/调试"},
            {"id": "qwen3.5-omni-plus", "name": "全模态版", "desc": "支持文本、图像、语音理解与生成"},
            {"id": "qwen-long", "name": "长文本版", "desc": "超长上下文处理"}
        ],
        "base_url": {
            "openai": {"general": "https://dashscope.aliyuncs.com/compatible-mode/v1", "enterprise": "https://{资源池ID}.dashscope.aliyuncs.com/compatible-mode/v1"},
            "anthropic": {"general": "https://dashscope.aliyuncs.com/anthropic", "enterprise": "https://{资源池ID}.dashscope.aliyuncs.com/anthropic"}
        },
        "official_site": "https://tongyi.aliyun.com",
        "chat_url": "https://tongyi.aliyun.com/qianwen",
        "tags": ["免费额度", "代码强", "多模态", "开源", "企业级高并发"],
        "remark": "新用户送500万Token免费额度，支持离线部署License申请，全系列模型开源可本地化部署"
    },
    # 6. 月之暗面（Kimi）
    {
        "provider": "月之暗面（Kimi）",
        "models": [
            {"id": "kimi-k2.6", "name": "通用旗舰版", "desc": "综合能力领先，长文本处理能力突出"},
            {"id": "kimi-k2.6-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "kimi-k2.6-coder", "name": "代码专属版", "desc": "代码开发/调试"},
            {"id": "kimi-k2.6-long", "name": "长上下文版", "desc": "支持1000万Token上下文，单次可处理千万字文档"}
        ],
        "base_url": {
            "openai": {"general": "https://api.moonshot.cn/v1", "enterprise": "https://enterprise-api.moonshot.cn/v1"},
            "anthropic": {"general": "https://api.moonshot.cn/anthropic", "enterprise": "https://enterprise-api.moonshot.cn/anthropic"}
        },
        "official_site": "https://www.moonshot.cn",
        "chat_url": "https://kimi.moonshot.cn",
        "tags": ["免费额度", "长上下文", "多模态", "代码强"],
        "remark": "免费额度为每月1000万Token，支持最长1亿Token上下文调用，长文本处理能力业内领先"
    },
    # 7. 字节跳动（豆包）
    {
        "provider": "字节跳动（豆包）",
        "models": [
            {"id": "doubao-4.0-pro", "name": "旗舰版", "desc": "综合能力领先，中文理解能力突出"},
            {"id": "doubao-4.0-flash", "name": "极速版", "desc": "高并发场景适用，推理速度快"},
            {"id": "doubao-4.0-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "doubao-4.0-coder", "name": "代码专属版", "desc": "代码开发/调试"},
            {"id": "doubao-4.0-long", "name": "长上下文版", "desc": "支持500万Token上下文"}
        ],
        "base_url": {
            "openai": {"general": "https://api.doubao.com/v1", "enterprise": "https://enterprise-api.doubao.com/v1"},
            "anthropic": {"general": "https://api.doubao.com/anthropic", "enterprise": "https://enterprise-api.doubao.com/anthropic"}
        },
        "official_site": "https://www.doubao.com",
        "chat_url": "https://www.doubao.com/chat",
        "tags": ["免费额度", "中文理解强", "多模态", "代码强", "企业级高并发"],
        "remark": "新用户注册送2000万Token免费额度，支持字节生态工具一键打通，抖音/飞书数据联动"
    },
    # 8. 腾讯（混元）
    {
        "provider": "腾讯（混元）",
        "models": [
            {"id": "hunyuan-5.0-preview", "name": "新一代预览版", "desc": "综合能力全面升级"},
            {"id": "hunyuan-4.0", "name": "通用旗舰版", "desc": "综合能力领先，金融级安全合规"},
            {"id": "hunyuan-4.0-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "hunyuan-4.0-coder", "name": "代码专属版", "desc": "代码开发/调试"}
        ],
        "base_url": {
            "openai": {"general": "https://api.hunyuan.tencent.com/v1", "enterprise": "https://{资源组ID}.hunyuan.tencent.com/v1"},
            "anthropic": {"general": "https://api.hunyuan.tencent.com/anthropic", "enterprise": "https://{资源组ID}.hunyuan.tencent.com/anthropic"}
        },
        "official_site": "https://hunyuan.tencent.com",
        "chat_url": "https://hunyuan.tencent.com/chat",
        "tags": ["免费额度", "金融合规", "多模态", "代码强", "企业级高并发"],
        "remark": "新用户送1500万Token免费额度，金融级数据安全合规，支持腾讯云生态联动"
    },
    # 9. 百度（文心一言/千帆）
    {
        "provider": "百度（文心一言/千帆）",
        "models": [
            {"id": "ernie-5.0-preview", "name": "新一代预览版", "desc": "综合能力全面升级"},
            {"id": "ernie-4.5-pro", "name": "旗舰版", "desc": "中文理解能力突出，支持搜索实时接入"},
            {"id": "ernie-4.5-turbo", "name": "极速版", "desc": "高并发场景适用，推理速度快"},
            {"id": "ernie-4.5-vision", "name": "多模态视觉版", "desc": "图像理解/解析"}
        ],
        "base_url": {
            "openai": {"general": "https://qianfan.baidubce.com/compatible/v1", "enterprise": "https://{实例ID}.qianfan.baidubce.com/compatible/v1"},
            "anthropic": {"general": "https://qianfan.baidubce.com/anthropic", "enterprise": "https://{实例ID}.qianfan.baidubce.com/anthropic"}
        },
        "official_site": "https://yiyan.baidu.com",
        "chat_url": "https://yiyan.baidu.com",
        "tags": ["免费额度", "中文理解强", "搜索联动", "多模态", "企业级高并发"],
        "remark": "新用户送800万Token免费额度，支持百度搜索实时接入，国内合规性领先"
    },
    # 10. 零一万物（Yi大模型）
    {
        "provider": "零一万物（Yi大模型）",
        "models": [
            {"id": "yi-4.0-34b-instruct", "name": "旗舰版", "desc": "综合能力突出，长文本处理能力强"},
            {"id": "yi-4.0-9b-instruct", "name": "轻量版", "desc": "低资源场景适用，可端侧部署"},
            {"id": "yi-4.0-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "yi-4.0-long", "name": "长上下文版", "desc": "支持2000万Token上下文"}
        ],
        "base_url": {
            "openai": {"general": "https://api.lingyiwanwu.com/v1", "enterprise": "https://enterprise-api.lingyiwanwu.com/v1"},
            "anthropic": {"general": "https://api.lingyiwanwu.com/anthropic", "enterprise": "https://enterprise-api.lingyiwanwu.com/anthropic"}
        },
        "official_site": "https://www.lingyiwanwu.com",
        "chat_url": "https://chat.lingyiwanwu.com",
        "tags": ["免费额度", "长上下文", "开源", "端侧部署"],
        "remark": "免费额度为每月500万Token，支持轻量化端侧部署，全系列模型开源可本地化部署"
    },
    # 11. InclusionAI（灵犀大模型）
    {
        "provider": "InclusionAI（灵犀大模型）",
        "models": [
            {"id": "ling-2.6-1t-instruct", "name": "旗舰文本生成版", "desc": "1T参数，长文本/文学创作能力突出"},
            {"id": "ling-2.6-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "ling-2.6-code", "name": "代码专属版", "desc": "代码开发/调试"}
        ],
        "base_url": {
            "openai": {"general": "https://api.inclusionai.com/v1", "enterprise": "https://enterprise-api.inclusionai.com/v1"},
            "anthropic": {"general": "https://api.inclusionai.com/anthropic", "enterprise": "https://enterprise-api.inclusionai.com/anthropic"}
        },
        "official_site": "https://www.inclusionai.cn",
        "chat_url": "https://chat.inclusionai.cn",
        "tags": ["免费额度", "长文本创作", "多模态", "代码强"],
        "remark": "新用户注册送200万Token免费额度，主打长文本/文学创作场景，中文生成能力领先"
    },
    # 12. MiniMax（稀宇科技）
    {
        "provider": "MiniMax（稀宇科技）",
        "models": [
            {"id": "abab-7", "name": "通用旗舰版", "desc": "综合能力领先，多模态能力突出"},
            {"id": "minimax-01", "name": "轻量高性价比版", "desc": "低资源场景适用，推理速度快"},
            {"id": "minimax-vision", "name": "多模态视觉版", "desc": "图像理解/解析"},
            {"id": "minimax-video", "name": "视频生成版", "desc": "支持短视频生成，效果业内领先"}
        ],
        "base_url": {
            "openai": {"general": "https://api.minimax.chat/v1", "enterprise": "请在官方文档企业服务板块查询专属地址"},
            "anthropic": {"general": "https://api.minimax.chat/anthropic", "enterprise": "请在官方文档企业服务板块查询专属地址"}
        },
        "official_site": "https://www.minimax.chat",
        "chat_url": "https://hailuoai.com",
        "tags": ["免费额度", "多模态", "视频生成", "代码强"],
        "remark": "新用户送500万Token免费额度，视频生成能力突出，支持多模态混合输入"
    }
]


def main():
    try:
        params = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        print(json.dumps({"content": "❌ 参数解析错误，请检查输入格式"}))
        return

    action = params.get("action")
    provider = params.get("provider")
    model_name = params.get("model_name")
    scene = params.get("scene")
    protocol = params.get("protocol", "openai")
    pay_type = params.get("pay_type", "general")

    all_providers = get_all_providers()
    result = []

    # 自学习：写入新厂商数据
    if action == "learn":
        provider_data = params.get("provider_data")
        if not provider_data:
            print(json.dumps({"content": "⚠️ 请提供要学习的厂商数据(provider_data)，格式参考：{\"provider\":\"厂商名\",\"models\":[{\"id\":\"model-id\",\"name\":\"模型名\",\"desc\":\"描述\"}],\"base_url\":{...},\"official_site\":\"...\",\"chat_url\":\"...\",\"tags\":[\"...\"],\"remark\":\"...\"}"}))
            return
        if isinstance(provider_data, str):
            try:
                provider_data = json.loads(provider_data)
            except json.JSONDecodeError:
                print(json.dumps({"content": "❌ provider_data JSON格式解析错误"}))
                return
        # 必填字段校验
        required_fields = ["provider", "models", "base_url"]
        missing = [f for f in required_fields if f not in provider_data]
        if missing:
            print(json.dumps({"content": f"❌ provider_data 缺少必填字段：{', '.join(missing)}"}))
            return
        # 补全可选字段默认值
        provider_data.setdefault("official_site", "")
        provider_data.setdefault("chat_url", "")
        provider_data.setdefault("tags", [])
        provider_data.setdefault("remark", "")
        # 写入外部文件
        user_providers = load_user_providers()
        # 检查是否已存在同名厂商，存在则更新
        existing_idx = next((i for i, p in enumerate(user_providers) if provider_data["provider"] in p["provider"] or p["provider"] in provider_data["provider"]), None)
        if existing_idx is not None:
            user_providers[existing_idx] = provider_data
            action_desc = "更新"
        else:
            user_providers.append(provider_data)
            action_desc = "新增"
        save_user_providers(user_providers)
        model_ids = ", ".join([m["id"] for m in provider_data.get("models", [])])
        print(json.dumps({"content": f"✅ 已{action_desc}厂商「{provider_data['provider']}」，包含模型：{model_ids}\n数据已保存至 user_providers.json，下次查询可直接命中。"}))
        return

    # 场景推荐
    if action == "recommend":
        if not scene:
            print(json.dumps({"content": "⚠️ 请指定使用场景，可选：免费日常使用、代码开发、长上下文处理、多模态/视觉、视频生成、开源本地化部署、企业级高并发、推理/数学计算、文学/长文本创作"}))
            return
        scene_tag_map = {
            "免费日常使用": "免费",
            "代码开发": "代码强",
            "长上下文处理": "长上下文",
            "多模态/视觉": "多模态",
            "视频生成": "视频生成",
            "开源本地化部署": "开源",
            "企业级高并发": "企业级高并发",
            "推理/数学计算": "推理强",
            "文学/长文本创作": "长文本创作"
        }
        target_tag = scene_tag_map.get(scene)
        result = [item for item in all_providers if target_tag in item["tags"]]
        result.sort(key=lambda x: "免费" in x["tags"], reverse=True)

    # 按厂商/模型查询
    elif action == "query_info":
        if not provider:
            print(json.dumps({"content": "⚠️ 请指定要查询的厂商名称，例如：美团LongCat、DeepSeek、小米MiMo"}))
            return
        result = [item for item in all_providers if provider in item["provider"]]
        if model_name:
            result = [
                {**item, "models": [m for m in item["models"] if model_name in m["id"] or model_name in m["name"]]}
                for item in result
            ]
            result = [item for item in result if len(item["models"]) > 0]
        if not result:
            print(json.dumps({"content": f"❌ 未找到「{provider}」的信息。\n\n💡 提示：当前数据库无此厂商数据。请先通过网络搜索获取该厂商的API信息，然后使用 learn action 将数据写入，后续查询即可直接命中。"}))
            return

    # 生成调用代码
    elif action == "get_code":
        if not provider or not model_name:
            print(json.dumps({"content": "⚠️ 请同时指定厂商和模型名称，例如：provider=美团LongCat，model_name=longcat-2.0-preview"}))
            return
        target = next((item for item in all_providers if provider in item["provider"]), None)
        if not target:
            print(json.dumps({"content": f"❌ 未找到厂商「{provider}」的信息。\n\n💡 提示：请先通过网络搜索获取该厂商信息，再使用 learn action 写入数据。"}))
            return
        model = next((m for m in target["models"] if m["id"] == model_name or model_name in m["name"]), None)
        if not model:
            print(json.dumps({"content": f"❌ 未找到「{target['provider']}」下的模型「{model_name}」"}))
            return
        base_url = target["base_url"][protocol][pay_type]

        if protocol == "openai":
            code = f"""from openai import OpenAI

client = OpenAI(
    api_key="<你在{target['provider']}官网申请的API Key>",
    base_url="{base_url}"
)

response = client.chat.completions.create(
    model="{model['id']}",
    messages=[{{"role": "user", "content": "<你的问题内容>"}}]
)
print(response.choices[0].message.content)"""
        else:
            code = f"""from anthropic import Anthropic

client = Anthropic(
    api_key="<你在{target['provider']}官网申请的API Key>",
    base_url="{base_url}"
)

response = client.messages.create(
    model="{model['id']}",
    max_tokens=1024,
    messages=[{{"role": "user", "content": "<你的问题内容>"}}]
)
print(response.content[0].text)"""

        content = f"""### {target['provider']} {model['name']} 调用代码（{protocol}协议）
```python
{code}
```

**备注**：{target['remark']}"""
        print(json.dumps({"content": content}))
        return

    # 格式化返回
    if not result:
        print(json.dumps({"content": "❌ 未找到匹配的大模型信息，请检查参数是否正确。\n\n💡 提示：如需查询的厂商不在数据库中，请先网络搜索获取信息，再使用 learn action 写入数据。"}))
        return

    content = []
    for item in result:
        current_base_url = item["base_url"][protocol][pay_type]
        model_list = "\n".join([f"- `{m['id']}`：{m['name']}，{m['desc']}" for m in item["models"]])
        site_str = "、".join(item["official_site"]) if isinstance(item["official_site"], list) else item["official_site"]
        content.append(f"""## {item['provider']}
🔹 官方API地址（{protocol}协议，{'通用按量/免费' if pay_type == 'general' else '企业包量'}）：`{current_base_url}`
🔹 支持的模型：
{model_list}
🔹 官方官网：{site_str}
🔹 体验地址：{item['chat_url']}
🔹 备注：{item['remark']}""")

    print(json.dumps({"content": "\n\n---\n\n".join(content)}))


if __name__ == "__main__":
    main()
