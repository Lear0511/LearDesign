#!/usr/bin/env python3
"""スキルの基本検証。

SKILL.md の存在・frontmatter・行数（500行以下を推奨）と、
references/ scripts/ assets/ の有無を確認する。

使い方:
    python3 validate_skill.py <スキルディレクトリ>
    例: python3 validate_skill.py .claude/skills/content-writing
"""
import sys
import pathlib


def main(target: str) -> int:
    base = pathlib.Path(target)
    skill = base / "SKILL.md"
    ok = True

    if not skill.exists():
        print(f"[NG] SKILL.md が見つかりません: {skill}")
        return 1

    text = skill.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not text.startswith("---"):
        print("[NG] frontmatter (---) がありません")
        ok = False
    else:
        print("[OK] frontmatter あり")

    if len(lines) > 500:
        print(f"[WARN] {len(lines)} 行: 500行以下を推奨")
    else:
        print(f"[OK] {len(lines)} 行 (<=500)")

    for d in ("references", "scripts", "assets"):
        mark = "[OK]" if (base / d).is_dir() else "[--]"
        print(f"  {mark} {d}/")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
