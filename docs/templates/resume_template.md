# 職務経歴書

**2026 年 1 月 10 日現在**  
**氏名 西部 倖平**

---

## 職務要約

TypeScript/Python を中心としたフルスタック開発 5 年目のエンジニアです。

直近では、**生成 AI を活用した SaaS プロダクト開発**に 3 案件連続で携わり、
OpenAI API・Gemini API との連携実装や、AWS Bedrock Transcribe を活用した音声認識システムの開発経験があります。

フロントエンド（Next.js/TypeScript）、バックエンド（FastAPI/Python）、
インフラ（AWS ECS/Lambda）を一貫して担当でき、0→1 フェーズでの PdM・デザイナーとの協業経験もあります。

また、自社サービス開発では GitLab CI/CD 導入によるコスト削減や、
PdM・デザイナーとの協業を通じた要件定義・仕様策定にも携わってきました。

今後は、特定ドメインで深い知見を築き、
技術とビジネスを繋ぐエンジニアとしてキャリアを構築したいと考えています。

---

## 活かせる経験・知識・技術

- Web アプリケーションにおけるフロントエンドおよびバックエンド一貫した開発経験
- AWS によるクラウドインフラ運用経験
- 自社プロダクト開発・運用経験
- デザイナーとの協業を通じたフロントエンド 0 -> 1 開発
- データサイエンティストとの協業を通じた PoC 経験
- Cursor や ClaudeCode, Next.js、Go などモダンな技術スタックへの関心

---

## テクニカルスキル

### フロントエンド

- TypeScript(4 年), React, Next.js
- JavaScript(5 年)
- Tailwind CSS
- Shadcn/ui
- Chakra UI V2, V3

### バックエンド

- Python(5 年), Flask, FastAPI, Streamlit
- PHP(3 年), (Laravel)
- Java(4 ヶ月), Spring Boot
- C#(6 ヶ月), .Net
- Go(1 年)

### インフラ／環境構築

- Amazon Web Services（2 年）※EC2, ECS, Lambda, SQS, EventBridge, RDS, S3 など
- Docker / Docker Compose（5 年）
- Linux コマンド(3 年)

### データベース

- MySQL（3 年）
- PostgreSQL(1 年半)
- SQLServer(1 年)

### CI/CD／開発管理

- Gitlab（5 年）、GitHub（2 年）GitHub Actions, Gitlab CI/CD

### AI ツール活用

#### コーディング

- Cursor（2024 年 4 月〜）
- ClaudeCode（2025 年 8 月〜）

#### 仕様整理など

- Gemini Pro, Claude（有料プラン）

---

## 職務経歴

{% for company in companies %}

### {{ company.period }}　{{ company.company_name }}

**事業内容:** {{ company.business_content }}  
**資本金:** {{ company.capital }}  
**従業員数:** {{ company.employees }}  
**上場:** {{ company.listed }}

{% for project in company.projects %}

#### {{ project.name }}

| 項目               | 内容                         |
| ------------------ | ---------------------------- |
| **期間**           | {{ project.table.period }}   |
| **職種**           | {{ project.table.role }}     |
| **役割**           | {{ project.table.position }} |
| **体制・組織規模** | {{ project.table.team }}     |

**プロジェクト概要**

{{ project.summary }}

**担当業務**

{% for task in project.tasks -%}

- {{ task }}
  {% endfor %}

**実績・取り組み**

{% for achievement in project.achievements -%}

- {{ achievement }}
  {% endfor %}

**利用技術**

{{ project.tech_stack }}
{% endfor %}

---

{% endfor %}

## 自己 PR

### 課題への着眼と改善推進力

自社プロダクトの開発では特にコスト意識を強く持ち、コストに対する改善に貢献してきました。

見えないコスト対するアプローチ  
AWS EC2 へ手動でデプロイ、テストの実施をしており、属人化、目視確認による作業工数増加という業務課題がありました。  
Gitlab CI/CD を活用し、 eslint によるコードの静的解析、 jest によるテストの自動化、 AWS SAM によるデプロイの自動化を導入することでこれらの作業工数を削減しました。
新規機能の開発を急ぐ経営陣やマネージャーへ、これらを導入する必要性を論理的に伝えることでチーム内の業務効率化と品質担保に貢献しました。

サーバーコストに対するアプローチ  
サービスリリース後からユーザー増加に伴い、AWS サーバーコストが増大していました。
すべて EC2 でデプロイされていたサーバーを ECS, Lambda を活用することによるコスト改善。  
Develop 環境や Staging 環境のサーバーコストを自動起動、自動停止を導入しコスト削減。

### チーム貢献と学習スタンス

開発業務の中での気づきや、ナレッジを横連携することを意識してきました。

開発環境構築やエラーログの分析、VSCode の拡張機能や Node.js のバージョン管理などを Gitlab Wiki や README, Redmine や Notion に共有し、自分自身が困ったことはチームメンバーも困っていることを前提としてチーム内での情報連携を意識してきました。

業務で利用している技術スタックを中心に代替できる技術やライブラリをキャッチアップし、新規プロジェクトや技術選定に関わる場合に提案することを心がけています。

### 今後の展望

これまで、生成 AI を活用した SaaS プロダクトや Web アプリケーションの開発に携わってきました。
硝子業界向け図面読み取り AI Platform, SES 営業向けマッチングサービス、介護業界ケアマネージャー向け Web アプリケーション、建築業界向け SCM システムなど。  
これらの経験を活かし、今後はドメインに対する深い知見を付け、よりビジネスに近い視点からエンジニアとして社会課題の解決に携わっていきたいと考えています。
