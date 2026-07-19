# Changelog

All notable changes to this repository are documented here. Each skill keeps its own `CHANGELOG.md` for version history.

## [1.3.0] - 2026-07-19

### Added
- First five production-ready new media skills, finalized at v1.3.0:
  - R01 industry-research
  - R02 competitor-positioning-analysis
  - R03 competitor-content-analysis
  - R04 competitor-marketing-strategy-analysis
  - R05 user-comment-analysis
- Authoritative spec set: `docs/design-spec.md`, `docs/test-spec.md`, `docs/skill-inventory.md`.
- Quality docs: `docs/compatibility.md`, `docs/publishing-guide.md`, `docs/skill-quality-playbook.md`.
- Reusable templates and `templates/skill-review-checklist.md`.
- Repository scripts: `scripts/build_dist.py`, `scripts/validate_repository.py`, `scripts/generate_catalog.py`.
- GitHub Actions workflow `validate-skills.yml` (runs on push and pull_request).
- Public catalog: `catalog/SKILLS.md` and `catalog/skills.json` (generated from the inventory).

### Notes
- License not yet granted; the repository is public but not open-source. See README.
- The 45 remaining skills are listed as planned in the inventory and catalog; no empty skill folders are created.
