# AGENTS.md

## Purpose

This repository defines and maintains the `development-plugin-for-avalonia` plugin, its repo-local wrapper skill, and its focused Avalonia skills.

Primary goals:
- keep guidance accurate to the pinned Avalonia release,
- split broad Avalonia guidance into granular, reusable skills,
- keep app-development references shared instead of duplicated across skills,
- maintain clear navigation across `.agents/skills/development-plugin-for-avalonia/SKILL.md`, `SKILL.md`, `skills/*/SKILL.md`, `README.md`, and `references/`.

## Source of Truth

Use these files in this order:
1. `.agents/skills/development-plugin-for-avalonia/SKILL.md` (repo-local discovery entrypoint)
2. `SKILL.md` (canonical umbrella routing workflow and default behavior)
3. `skills/*/SKILL.md` (focused workflows for the active lane)
4. `references/compendium.md` (reference index and task navigation)
5. `references/00-api-map.md` (curated app-facing API map)
6. `references/api-index-generated.md` (broad signature lookup)

If they conflict, align all skills and docs to the pinned version and update the conflicting files.

## Version Pinning

- Target Avalonia version: `11.3.12`
- Do not introduce default guidance that depends on Avalonia `master` unless explicitly requested.
- Keep version statements in top-level docs (`README.md`, `SKILL.md`), not repeated everywhere.

Regenerate API index with the pinned ref:

```bash
python3 scripts/generate_api_index.py \
  --repo <path-to-avalonia-repo> \
  --git-ref 11.3.12 \
  --output references/api-index-generated.md
```

## Skill Authoring Rules

- Repo-local skill entrypoints live under `.agents/skills/<skill-name>/`.
- Specialist skills live under `skills/<skill-name>/`.
- Keep skill names lower-case hyphen-case.
- Each discovered skill entrypoint should have:
  - `SKILL.md`
  - `agents/openai.yaml`
- Keep the repo-local wrapper thin and route into the canonical umbrella workflow or focused plugin skills.
- Keep `SKILL.md` bodies short and route to shared references instead of copying large content into each skill.
- Put trigger conditions in frontmatter descriptions, not in long body sections.
- When adding, renaming, or removing a skill, update all relevant navigation points:
  - `.agents/skills/development-plugin-for-avalonia/SKILL.md`
  - `SKILL.md`
  - `README.md`
  - any other skill that routes to it

## Reference Authoring Rules

- Reference docs live under the `references/` folder using `NN-topic-name` filename patterns.
- Keep numbering and filenames stable and sequential.
- When adding or renaming a reference, update all relevant navigation:
  - `references/compendium.md`
  - any specialist skill that links to that reference
  - `README.md` when the lane is part of the published catalog
- Prefer relative paths in docs and examples inside this repo.
- Keep content app-development-focused; avoid low-value API tail coverage unless needed for practical usage.

## Reference Content Standard

Each new or expanded reference should include:
- clear scope and primary APIs,
- realistic XAML and/or C# examples,
- AOT/trimming notes where relevant,
- practical do/don't guidance,
- troubleshooting or edge-case notes for common mistakes.

Default guidance bias:
- compiled bindings + `x:DataType`,
- XAML-first patterns unless the user requests code-only,
- explicit UI-thread and dispatcher behavior for async/reactive flows.

## API Coverage Workflow

Use coverage tooling after significant reference updates.

1. Recompute gaps:

```bash
python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
```

2. Run parser tests:

```bash
python3 -m unittest scripts.test_find_uncovered_apis
```

3. Refresh planning/report docs as needed:
- `plan/api-coverage-detailed-report.md`
- `plan/api-coverage-reference-update-plan.md`

Coverage target is practical completeness for app development, not 100% signature parity.

## Change Review Checklist

Before finalizing changes:
1. Verify repo-local, root, and specialist skill routing still matches the current skill catalog.
2. Verify new or renamed skills are reflected in `README.md` and any routing skill that mentions them.
3. Verify examples use APIs available in Avalonia `11.3.12` unless the skill explicitly targets the Avalonia 12 lane.
4. Re-run coverage tooling when API-focused references changed.
5. Ensure no accidental drift to `master`-only APIs.

## Commits

- Keep commits granular and topic-based (one logical change set per commit).
- Avoid mixing script changes, coverage artifacts, and large doc rewrites in a single commit when separable.
