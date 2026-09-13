# Contributing to Boluobao / 参与贡献

感谢你帮助 Boluobao 变得更稳定、清楚和易于复用。Boluobao 已进入稳定维护阶段：贡献应解决真实需求或可复现问题，同时保护既有视觉识别、调用契约、文字与数据准确性，以及素材授权边界。

Thank you for helping make Boluobao more reliable, understandable, and reusable. Boluobao is in stable maintenance: contributions should address a real need or reproducible problem while preserving its visual identity, invocation contract, text and data accuracy, and asset-licensing boundaries.

## 开始之前 / Before You Start

- 小型文档修正、拼写修正和明确的脚本错误可以直接提交 Pull Request。
- 新输出模式、共享画风规则、依赖、授权策略或大型素材变更，请先创建 Issue，说明使用场景、当前行为、期望行为和最小复现。
- 一个 Pull Request 只解决一个清楚的问题；避免同时重构无关文件。
- 请勿提交密钥、个人信息、私有提示词、未公开内容或无法确认授权的素材。

- Small documentation fixes, typo corrections, and clearly scoped script bugs may go directly to a pull request.
- Open an issue first for a new output mode, shared style rule, dependency, licensing policy, or large asset change. Include the use case, current behavior, expected behavior, and a minimal reproduction.
- Keep each pull request focused on one clear problem; avoid unrelated refactors.
- Never submit secrets, personal information, private prompts, unpublished content, or assets whose publication rights cannot be confirmed.

## 适合本项目的贡献 / Contributions That Fit

欢迎以下贡献：

- 带有可复现输入、失败现象和期望结果的调用回归报告；
- 不增加无关约束的针对性规则修正；
- 包校验、同步脚本和跨平台兼容性改进；
- 安装、调用、可访问性、翻译和示例文档改进；
- 经授权、能够替换旧基线的生成测试素材。

Good contributions include:

- invocation regressions with reproducible input, observed failure, and expected behavior;
- focused rule corrections that do not add unrelated constraints;
- package validation, synchronization, and cross-platform compatibility improvements;
- installation, invocation, accessibility, translation, and example documentation;
- authorized generated test assets that replace an older baseline.

以下内容通常不接受：

- 只针对一次生成事故增加的通用规则；
- 没有真实调用证据的新画风或平台模式；
- 写实修图、干净矢量化、密集电子表格等偏离项目边界的能力；
- 要求模仿在世艺术家，或复制参考图中的独特文字、角色、故事和版式；
- 未授权的图片、字体、Logo、商标、数据集或私有内容。

The following are normally out of scope:

- universal rules added for a one-off generation accident;
- new visual or platform modes without real invocation evidence;
- photorealistic retouching, clean vectorization, dense spreadsheet reporting, or other work outside the project boundary;
- instructions to imitate a living artist or copy distinctive text, characters, stories, or layouts from reference images;
- unlicensed images, fonts, logos, trademarks, datasets, or private content.

## 开发流程 / Development Workflow

1. Fork 仓库并创建简短、清楚的分支，例如 `fix/japanese-text-lock`、`docs/codex-install` 或 `feat/chart-validation`。
2. 阅读根目录 [SKILL.md](SKILL.md)，并只读取当前模式需要的 `references/` 文件。修改共享规则前请同时阅读 [references/forward-tests.md](references/forward-tests.md)。
3. 保持 `SKILL.md` 为精简入口；模式细节放入现有的对应 reference，避免在多个文件维护重复规则。
4. 为可复现行为补充或更新 `assets/tests/invocation-cases.json`。只有在旧样张已不再代表边界时才替换样张，不要不断累积近似图片。
5. 更新清单、哈希、尺寸、README 和 CHANGELOG 中与改动直接相关的部分。
6. 运行全部校验后再提交 Pull Request。

1. Fork the repository and create a short, descriptive branch such as `fix/japanese-text-lock`, `docs/codex-install`, or `feat/chart-validation`.
2. Read the root [SKILL.md](SKILL.md) and only the `references/` files needed for the active mode. Also read [references/forward-tests.md](references/forward-tests.md) before changing a shared rule.
3. Keep `SKILL.md` a concise entry point. Put mode-specific detail in the existing matching reference instead of maintaining duplicated rules.
4. Add or update `assets/tests/invocation-cases.json` for reproducible behavior. Replace a retained sample only when the old sample no longer represents the boundary; do not accumulate near-duplicate images.
5. Update only the directly affected manifest, hashes, dimensions, README, and CHANGELOG entries.
6. Run all checks before opening a pull request.

## 不可破坏的项目约束 / Project Invariants

- 保留用户意图、主体身份、精确文字、数据值、单位、排序和映射关系。
- 继续使用最终成品制；不得提交 `output/`、`working/`、`candidate/`、生成缓存或过程稿。
- 共享画风规则应保持渐进披露，不能让所有调用都加载无关模式说明。
- 暖纸、深色手绘轮廓、半透明彩铅、功能性留白和局部受控不规则感仍是稳定视觉基因。
- 包体必须不超过 `60 MB`，不得包含重复图片哈希。新的展示图使用 WebP，并遵守清单中的尺寸和文件大小边界。
- 不引入第三方字体或外部服务依赖，除非先在 Issue 中说明必要性、许可、失败模式和无依赖回退路径。

- Preserve user intent, subject identity, exact text, data values, units, order, and mappings.
- Keep final-only retention. Never commit `output/`, `working/`, `candidate/`, generator caches, or intermediate drafts.
- Shared style rules must preserve progressive disclosure and must not make every invocation load unrelated mode guidance.
- Warm paper, dark hand-drawn contours, translucent colored pencil, functional whitespace, and locally controlled imperfection remain stable visual DNA.
- The package must stay at or below `60 MB` and contain no duplicate image hashes. New showcase images must use WebP and follow the dimensions and size limits in the manifest.
- Do not introduce a third-party font or external service dependency without first documenting its need, license, failure modes, and dependency-free fallback in an issue.

## 素材与授权 / Assets and Licensing

提交任何图片、字体、Logo 或参考素材前，请先阅读 [ASSETS-LICENSE.md](ASSETS-LICENSE.md)。

Before contributing any image, font, logo, or reference material, read [ASSETS-LICENSE.md](ASSETS-LICENSE.md).

- 项目原创代码、规则和文档按 [Apache License 2.0](LICENSE) 发布。
- `assets/tests/` 中获准保留的生成测试图按 [CC BY 4.0](LICENSES/CC-BY-4.0.txt) 发布。
- Boluobao 名称、菠萝包图标和 `assets/brand/` 保留所有权；未经维护者同意不要修改或替换。
- `docs/showcase/` 仅供项目展示，不能作为可自由复用素材提交。
- `assets/references/` 不属于开源授权范围。新增或替换参考图必须提供来源、权利人、允许公开分发的依据和适用限制。
- 贡献者有责任移除 EXIF、位置、账号和其他隐私元数据，并确认画面中的人物、品牌和受保护内容可以公开展示。

- Project-authored code, rules, and documentation are distributed under the [Apache License 2.0](LICENSE).
- Approved generated test images retained under `assets/tests/` are distributed under [CC BY 4.0](LICENSES/CC-BY-4.0.txt).
- The Boluobao name, pineapple-bun icon, and `assets/brand/` are all rights reserved; do not modify or replace them without maintainer agreement.
- `docs/showcase/` is display-only and must not be submitted as freely reusable material.
- `assets/references/` is outside the open-source grant. A new or replacement reference requires its source, rightsholder, evidence of permission for public redistribution, and applicable restrictions.
- Contributors are responsible for removing EXIF, location, account, and other private metadata and for confirming that depicted people, brands, and protected content may be displayed publicly.

## 验证 / Validation

在仓库根目录至少运行：

Run at least the following commands from the repository root:

```powershell
python -m json.tool assets/tests/test-manifest.json > $null
python -m json.tool assets/tests/invocation-cases.json > $null
python -m py_compile scripts/validate_package.py scripts/sync_claude_skill.py
python -X utf8 scripts/validate_package.py
python -X utf8 scripts/sync_claude_skill.py --target "$env:TEMP/boluobao" --dry-run
git diff --check
```

macOS 或 Linux 请使用 `python3`，并把临时目标改为 `/tmp/boluobao`。如果本机安装了 Codex 的 `skill-creator`，还应运行其 `quick_validate.py` 检查 Skill frontmatter 与结构。

On macOS or Linux, use `python3` and change the temporary target to `/tmp/boluobao`. If Codex's `skill-creator` is installed locally, also run its `quick_validate.py` to check the Skill frontmatter and structure.

图片或清单变更还必须通过以下检查：尺寸与比例正确、SHA-256 与清单一致、展示图小于清单上限、没有重复图片哈希、包体不超过 `60 MB`。

Image or manifest changes must also pass these checks: correct dimensions and ratios, SHA-256 matching the manifest, showcase files below their size limits, no duplicate image hashes, and a total package size no greater than `60 MB`.

## Pull Request 内容 / Pull Request Contents

Pull Request 描述请包含：

- 问题与最小复现，或文档需求；
- 改动范围和明确未改动的部分；
- 运行过的测试及输出摘要；
- 对调用契约、兼容性、包体和授权的影响；
- 视觉改动的前后对照或质量评分，但不要上传未接受的候选稿。

Include the following in the pull request description:

- the problem and minimal reproduction, or the documentation need;
- the scope of the change and what intentionally remains unchanged;
- tests run and a concise result summary;
- effects on invocation contracts, compatibility, package size, and licensing;
- before-and-after evidence or quality scores for visual changes, without uploading rejected candidates.

提交前检查 / Before submitting:

- [ ] 改动针对真实需求或可复现问题。 / The change addresses a real need or reproducible issue.
- [ ] 用户意图、文字和数据锁定没有被弱化。 / User intent and text or data locks are not weakened.
- [ ] 没有提交过程稿、缓存、秘密或私有内容。 / No drafts, caches, secrets, or private content are committed.
- [ ] 所有素材均有清楚、兼容的发布授权。 / Every asset has clear, compatible publication permission.
- [ ] README、CHANGELOG、manifest 和版本信息按需更新。 / README, CHANGELOG, manifests, and version information are updated when needed.
- [ ] 所有校验通过，包体仍不超过 `60 MB`。 / All checks pass and the package remains at or below `60 MB`.

## 审查原则 / Review Principles

维护者会优先评估可复现性、用户意图、文字与数据准确性、视觉一致性、上下文成本、向后兼容和授权安全。无法复现、扩大范围过多或缺少素材权利证明的贡献可能会被要求缩小范围或关闭。

Maintainers prioritize reproducibility, user intent, text and data accuracy, visual consistency, context cost, backward compatibility, and licensing safety. Contributions that cannot be reproduced, expand scope excessively, or lack asset-rights evidence may be asked to narrow their scope or may be closed.

提交项目原创代码、规则或文档即表示你同意这些贡献可按 Apache-2.0 分发；图片及品牌素材仍遵守 [ASSETS-LICENSE.md](ASSETS-LICENSE.md) 的独立条款。

By submitting project-authored code, rules, or documentation, you agree that those contributions may be distributed under Apache-2.0. Images and brand material remain subject to the separate terms in [ASSETS-LICENSE.md](ASSETS-LICENSE.md).
