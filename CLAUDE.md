# CLAUDE.md

このリポジトリは GitHub プロフィール兼、職務経歴書の管理リポジトリです。

## リポジトリ概要

- `README.md` (ルート) - GitHub プロフィールページに表示されるプロフィール
- `docs/` - 職務経歴書の管理ディレクトリ

## 職務経歴書の構成

```
docs/
├── data/
│   └── career.json          # 職務経歴データ（単一の編集対象）
├── templates/
│   ├── resume_template.md   # Markdown テンプレート（Jinja2）
│   └── resume_template.html # HTML テンプレート（Jinja2）
├── scripts/
│   └── build_resume.py      # ビルドスクリプト
├── README.md                # 生成された Markdown 職務経歴書（自動生成）
└── resume.html              # 生成された HTML 職務経歴書（自動生成）
```

## ワークフロー

職務経歴を更新する場合は **`docs/data/career.json` のみを編集** し、ビルドスクリプトで出力を再生成する。

```bash
# venv を有効化してビルド
source env/bin/activate && python docs/scripts/build_resume.py
```

生成物（`docs/README.md`, `docs/resume.html`）は **直接編集しない**。テンプレートか JSON データを修正すること。

## データ構造（career.json）

プロジェクトには **2種類のフォーマット**が混在している。テンプレートは `situation` の有無で分岐している。

**フォーマット A（STAR形式）** — `situation` キーがある場合

```json
{
  "project_id": 12,
  "name": "プロジェクト名",
  "table": { "period": "", "role": "", "position": "", "team": "" },
  "summary": "概要（\\n で改行可）",
  "situation": ["背景・課題"],
  "task": ["自分のタスク"],
  "action": ["具体的なアクション"],
  "result": ["成果・影響"],
  "tech_stack": "技術スタック（スラッシュ区切り）"
}
```

**フォーマット B（シンプル形式）** — `situation` キーがない場合

```json
{
  "project_id": 1,
  "name": "プロジェクト名",
  "table": { "period": "", "role": "", "position": "", "team": "" },
  "summary": "概要（\\n で改行可）",
  "tasks": ["担当業務"],
  "achievements": ["実績・取り組み"],
  "tech_stack": "技術スタック（スラッシュ区切り）"
}
```

**`project_id` のルール**

- 全プロジェクトでフラットに採番（会社をまたいで一意）
- 古い案件ほど小さい番号、新しい案件ほど大きい番号
- 新案件追加時は現在の最大値 +1 を付与
- テンプレートは `project_id` 降順でソートして表示（`| sort(attribute='project_id', reverse=True)`）
- 画面には表示しない

## JSON 構造を変更するときの注意

**キーの追加・削除・リネームを行う場合は、必ず以下を確認・修正すること。**

| ファイル | 確認ポイント |
|---|---|
| `docs/templates/resume_template.md` | `{{ project.新キー }}` や `{% if project.新キー %}` の追加が必要か |
| `docs/templates/resume_template.html` | 同上 |
| `docs/scripts/build_resume.py` | データ変換や前処理が必要な場合のみ修正。現状はテンプレートに渡すだけなので通常は変更不要 |

変更後は必ずビルドを実行してエラーがないか確認すること。

## 注意事項

- `docs/README.md` と `docs/resume.html` は自動生成ファイルのため直接編集しない
- 新案件は `career.json` の先頭の会社エントリに追加し、`project_id` は現在の最大値 +1 を付与する
- HTML の `editor.formatOnSave` は無効化済み（`.setting.json`）
