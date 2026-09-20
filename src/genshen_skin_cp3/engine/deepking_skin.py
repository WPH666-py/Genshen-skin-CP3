# -*- coding: utf-8 -*-
"""
原神CP3 · 米提亚×奥黛塔×沃雅妮莎 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshen-cp3.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     夜景保留群像插画的深青蓝, 而不是派生算法给出的中性灰。

安装器(genshen-cp3 deepking)会把本调色板写成 genshen-cp3.skin.json,
并生成可视化预览 genshen-cp3-preview.html, 方便导入前先看效果。
"""
try:  # 本文件有两份副本: 包根(与 engine/ 平级)和 engine/ 内。
    from ..characters import cp3_trio as C      # 包根那份
except ImportError:                             # pragma: no cover
    from .characters import cp3_trio as C       # 极端情况下被当成顶层包

SKIN_ID = C.DEEPKING_SKIN_ID
SKIN_NAME = C.DEEPKING_SKIN_NAME
SKIN_DESC = C.DEEPKING_SKIN_DESC

# ─────────────────────────────────────────────── 亮色 · 净白浅灰(群像底)
LIGHT = {
    "bg": "#ffffff",
    "bgText": "#122b28",
    "sidebarBg": "#eaf5f3",
    "sidebarText": "#1b3a36",
    "sidebarHover": "#dcefec",
    "sidebarSelected": "#c3e3de",
    "sidebarHeader": "#6f918d",
    "editorBg": "#ffffff",
    "tabsBg": "#eef7f5",
    "tabBg": "#e3f1ee",
    "tabText": "#4d6f6b",
    "tabActiveBg": "#ffffff",
    "tabActiveText": "#122b28",
    "aiBg": "#f2f9f8",
    "aiText": "#122b28",
    "aiTabText": "#4d6f6b",
    "userBubbleBg": "#c9e7e2",
    "userBubbleText": "#122b28",
    "aiBubbleBg": "#ffffff",
    "aiBubbleText": "#122b28",
    "aiBubbleBorder": "#beddd8",
    "systemBubbleBg": "#fff8e6",
    "systemBubbleText": "#8a6a00",
    "inputBg": "#ffffff",
    "inputText": "#122b28",
    "inputBorder": "#9dcfc8",
    "accent": "#2f9e8f",
    "accentText": "#ffffff",
    "border": "#beddd8",
    "chipBg": "#d5ece8",
    "chipText": "#1f6d62",
    "chipBorder": "#9dcfc8",
}

# ─────────────────────────────────────────────── 夜景 · 深青蓝(发色深处)
DARK = {
    "bg": "#0f1f26",
    "bgText": "#e0eef0",
    "sidebarBg": "#16292f",
    "sidebarText": "#bcd6da",
    "sidebarHover": "#1f373f",
    "sidebarSelected": "#2a4650",
    "sidebarHeader": "#749499",
    "editorBg": "#0f1f26",
    "tabsBg": "#132329",
    "tabBg": "#16292f",
    "tabText": "#82a2a7",
    "tabActiveBg": "#1f373f",
    "tabActiveText": "#e0eef0",
    "aiBg": "#16292f",
    "aiText": "#e0eef0",
    "aiTabText": "#82a2a7",
    "userBubbleBg": "#245157",
    "userBubbleText": "#e8f4f5",
    "aiBubbleBg": "#1a3038",
    "aiBubbleText": "#e0eef0",
    "aiBubbleBorder": "#2c4a52",
    "systemBubbleBg": "#38301a",
    "systemBubbleText": "#e6d7a2",
    "inputBg": "#172b32",
    "inputText": "#e0eef0",
    "inputBorder": "#2c4a52",
    "accent": "#4fc0b0",
    "accentText": "#08161a",
    "border": "#2c4a52",
    "chipBg": "#22424a",
    "chipText": "#c6e4e6",
    "chipBorder": "#3d7580",
}

PALETTE_SLOTS = (
    "bg", "bgText", "sidebarBg", "sidebarText", "sidebarHover", "sidebarSelected",
    "sidebarHeader", "editorBg", "tabsBg", "tabBg", "tabText", "tabActiveBg",
    "tabActiveText", "aiBg", "aiText", "aiTabText", "userBubbleBg", "userBubbleText",
    "aiBubbleBg", "aiBubbleText", "aiBubbleBorder", "systemBubbleBg", "systemBubbleText",
    "inputBg", "inputText", "inputBorder", "accent", "accentText", "border",
    "chipBg", "chipText", "chipBorder",
)


def definition(mascot_light=None, mascot_dark=None, source=None):
    """返回完整的 DeepKing SkinDefinition(手工校色版)。"""
    skin = {
        "id": SKIN_ID,
        "name": SKIN_NAME,
        "builtin": False,
        "description": SKIN_DESC,
        "palettes": {"light": dict(LIGHT), "dark": dict(DARK)},
    }
    if source:
        skin["source"] = source
    if mascot_light or mascot_dark:
        skin["mascot"] = {
            "light": mascot_light or mascot_dark,
            "dark": mascot_dark or mascot_light,
        }
    return skin


def validate():
    """自检: 槽位齐全、色值合法、亮暗确实一浅一深、文字对比度够。"""
    from . import _color as col

    problems = []
    for label, pa in (("light", LIGHT), ("dark", DARK)):
        missing = [k for k in PALETTE_SLOTS if k not in pa]
        extra = [k for k in pa if k not in PALETTE_SLOTS]
        if missing:
            problems.append("%s 缺少槽位: %s" % (label, ", ".join(missing)))
        if extra:
            problems.append("%s 多余槽位: %s" % (label, ", ".join(extra)))
        for k, v in pa.items():
            if not col.is_hex(v):
                problems.append("%s.%s 不是合法 # 十六进制: %r" % (label, k, v))
    if not col.is_light_color(LIGHT["bg"]):
        problems.append("light.bg 不是浅色: %s" % LIGHT["bg"])
    if col.is_light_color(DARK["bg"]):
        problems.append("dark.bg 不是深色: %s" % DARK["bg"])
    for label, pa in (("light", LIGHT), ("dark", DARK)):
        for fg, bg in (("bgText", "bg"), ("sidebarText", "sidebarBg"),
                       ("aiBubbleText", "aiBubbleBg"), ("tabText", "tabsBg")):
            lf = sum(col.to_rgb(pa[fg])) / 3.0
            lb = sum(col.to_rgb(pa[bg])) / 3.0
            if abs(lf - lb) < 60:
                problems.append("%s: %s 与 %s 亮度太接近(%d), 文字可能看不清"
                                % (label, fg, bg, abs(lf - lb)))
    return problems
