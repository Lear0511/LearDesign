# Skills

このディレクトリは Claude Code のスキルを置く場所。各スキルは以下の構造に従う。

```
skill-name/
  SKILL.md         → 常に読み込む。役割と基本ルールだけ (500行以下推奨)
  references/      → タスクに応じて読み込む。知識・制約・品質基準
  scripts/         → 実行可能コード。繰り返し処理やデータ変換
  assets/          → 出力用テンプレートやアイコン
```

## 収録スキル

| スキル | 用途 |
|---|---|
| `skill-template/` | 新規スキルを作るための雛形（コピーして使う） |
| `content-writing/` | 編集なしで公開できる記事・長文コンテンツを書く |
| `email-writing/` | 行動を促す150語以内のビジネスメールを書く（2トーン） |
| `content-repurposing/` | 1つの元コンテンツを5フォーマットに展開する（X/LinkedIn/ニュースレター/SNS/動画台本） |
| `blog-outline/` | ブログ記事の詳細アウトライン（見出し案・メタ・リンク候補付き） |

## 新しいスキルの作り方

1. `skill-template/` をコピーして `skill-name/` にリネーム
2. `SKILL.md` の frontmatter（`name` / `description`）を書く。`description` は
   「いつ・何のために使うか」を具体的に書く（トリガー条件になる）
3. 詳細知識は `references/`、繰り返し処理は `scripts/`、出力雛形は `assets/` へ
4. 検証: `python3 skill-template/scripts/validate_skill.py <skill-name>`

詳細は `skill-template/references/AUTHORING_GUIDE.md` を参照。
